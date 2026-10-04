"""12-TRICKSTER-FORESIGHT §2.4a / §2.9: the echo API. Only allocated echoes export; the budget (8 mod-wide, 1 per route,
2 per chapter) and the registry axes (sense + misstep unique) are enforced; an exported echo is appended last, gated on the
page, costs something, and continues with the host node's own choices. Run: python -m unittest tests.test_foresight_echo"""
from pathlib import Path
import copy
import json
import os
import sys
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import expansion  # noqa: E402
from storylines import foresight, wenduag_echo  # noqa: E402
from story_format import c, n, scene  # noqa: E402

PROPOSED = {"devarra": "devarra.trickster.flight.pact", "terendelev": "terendelev.trickster.late.the_wound_calls"}


def _payload(scenes):
    return {"Scenes": scenes}


def _host(id, rel, chapter):
    return scene(id, "T", "X", chapter, "e", [n("start", "Narrator", "Text.", c("Go", "end"), c("Leave", abort=True)),
                                               n("end", "Narrator", "End.", c("Done"))], Relationship=rel, Chapters=[chapter])


class EchoApiTests(unittest.TestCase):
    def setUp(self):
        self._echoes, self._entries, self._alloc = list(foresight.ECHOES), set(foresight.ECHO_ENTRIES), dict(foresight.ALLOCATED)

    def tearDown(self):
        foresight.ECHOES[:] = self._echoes
        foresight.ECHO_ENTRIES.clear()
        foresight.ECHO_ENTRIES.update(self._entries)
        foresight.ALLOCATED.clear()
        foresight.ALLOCATED.update(self._alloc)

    def _register(self, rel, host, entry, sense="sight", misstep="m", requires=()):
        foresight.echo(rel, host, "start", entry, foresight.variant("Shyka's page: text.", requires=requires),
                       sense=sense, wrong="w", misstep=misstep, cost=("Favors", -10))

    def test_proposals_are_registered_but_not_exported(self):
        hosts = {e["rel"]: e["host"] for e in foresight.ECHOES}
        self.assertEqual(hosts, {**PROPOSED, "wenduag": "wenduag.trickster.echo.abyss.prepare"})
        self.assertTrue(set(PROPOSED).isdisjoint(foresight.ALLOCATED))
        self.assertEqual([e["rel"] for e in foresight.active_echoes()], ["wenduag"])
        story = expansion.make_expansion()
        self.assertFalse(any(nd["Id"].startswith("echo.") for s in story["Scenes"] for nd in s["Nodes"]))

    def test_allocated_echo_is_appended_gated_and_neutral(self):
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        self._register("a", "t.a", "[Act.]")
        foresight.ALLOCATED["a"] = "t.a"
        host = _host("t.a", "a", 3)
        original = copy.deepcopy(host["Nodes"][0]["Choices"])
        foresight.integrate_echoes(_payload([host]))
        start = host["Nodes"][0]
        self.assertEqual(start["Choices"][:2], original)
        entry = start["Choices"][2]
        self.assertIn(foresight.PAGE_TAKEN, entry["Requires"])
        self.assertIn("trickster.now", entry["Requires"])
        self.assertEqual(entry["Crusade"], {"Resource": "Favors", "Amount": -10})
        self.assertEqual(entry["Set"], [])
        echo_node = next(nd for nd in host["Nodes"] if nd["Id"] == entry["Next"])
        self.assertEqual(echo_node["Choices"], original)

    def test_route_cap(self):
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        self._register("a", "t.a1", "[One.]")
        self._register("a", "t.a2", "[Two.]", sense="sound")
        foresight.ALLOCATED.update({"a": "t.a1"})
        foresight.integrate_echoes(_payload([_host("t.a1", "a", 3), _host("t.a2", "a", 5)]))   # only the allocated one
        foresight.ECHOES[1]["host"] = "t.a1"
        with self.assertRaises(ValueError):
            foresight.integrate_echoes(_payload([_host("t.a1", "a", 3)]))

    def test_chapter_and_total_caps(self):
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        hosts = []
        for i, rel in enumerate("abc"):
            self._register(rel, "t." + rel, "[E%d.]" % i, sense=foresight.SENSES[i])
            foresight.ALLOCATED[rel] = "t." + rel
            hosts.append(_host("t." + rel, rel, 3))
        with self.assertRaises(ValueError):                     # three in Chapter 3
            foresight.integrate_echoes(_payload(hosts))
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        foresight.ALLOCATED.clear()
        hosts = []
        for i in range(9):
            rel = "r%d" % i
            self._register(rel, "t." + rel, "[E%d.]" % i, sense=foresight.SENSES[i % 5], misstep="m%d" % i)
            foresight.ALLOCATED[rel] = "t." + rel
            hosts.append(_host("t." + rel, rel, 1 + i // 2))
        with self.assertRaises(ValueError):                     # nine mod-wide
            foresight.integrate_echoes(_payload(hosts))

    def test_registry_axes(self):
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        self._register("a", "t.a", "[A.]")
        with self.assertRaises(ValueError):                     # same sense and misstep
            self._register("b", "t.b", "[B.]")
        with self.assertRaises(ValueError):                     # entry reused
            self._register("c", "t.c", "[A.]", sense="taste")
        with self.assertRaises(ValueError):                     # no sense
            foresight.echo("d", "t.d", "start", "[D.]", foresight.variant("x"), sense="", wrong="w", misstep="z",
                           cost=("Favors", -1))

    def test_normalized_registry_axes(self):
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        self._register("a", "t.a", "[A.]", sense=" Sight + SOUND + sight ",
                       misstep=" Paid runner searches the WRONG-place! ")
        for sense, misstep in (
            ("sound + sight", "paid runner searches the wrong place"),
            ("sound, sight.", "paid   runner searches the wrong place"),
            ("SOUND / Sight / sound", "PAID runner searches the wrong_place."),
        ):
            with self.subTest(sense=sense, misstep=misstep):
                with self.assertRaisesRegex(ValueError, "repeats a sense and misstep"):
                    self._register("b", "t.b", "[B.]", sense=sense, misstep=misstep)
        self.assertEqual(len(foresight.ECHOES), 1)
        self.assertNotIn("[B.]", foresight.ECHO_ENTRIES)

    def test_integrate_rechecks_normalized_registry_axes(self):
        foresight.ECHOES[:] = []
        foresight.ECHO_ENTRIES.clear()
        self._register("a", "t.a", "[A.]", sense="sight + sound", misstep="wrong place")
        self._register("b", "t.b", "[B.]", sense="touch", misstep="different")
        foresight.ECHOES[1].update(sense=" SOUND / Sight / sound ", misstep=" Wrong-place! ")
        foresight.ALLOCATED.update(a="t.a", b="t.b")
        hosts = [_host("t." + rel, rel, 3) for rel in "ab"]
        original = copy.deepcopy(hosts)
        with self.assertRaisesRegex(ValueError, "repeats a sense and misstep"):
            foresight.integrate_echoes(_payload(hosts))
        self.assertEqual(hosts, original)


class ForesightSurfaceTests(unittest.TestCase):
    def test_registered_consumer_contract_matches_export(self):
        story = expansion.make_expansion()
        consumers = {s["Id"]: foresight.PAGE_TAKEN for s in story["Scenes"] if foresight.PAGE_TAKEN in s["Requires"]}
        self.assertEqual(consumers, foresight.CONSUMERS)
        self.assertEqual(story["ForesightConsumers"], foresight.CONSUMERS)
        self.assertEqual(story["Derived"]["household.stance_eligible"], [[foresight.PAGE_TAKEN, "trickster.now"]])
        for key in (foresight.PAGE_TAKEN, foresight.GATE_BELIEVED):
            self.assertTrue(all("trickster.now" in group for group in story["Derived"][key]))
        for key in (foresight.GONE_SQUARE, foresight.GONE_CAVES):
            self.assertTrue(all("trickster.ever" in group and "trickster.now" not in group for group in story["Derived"][key]))

    def test_late_consumer_registration_is_serialized(self):
        story = expansion.make_expansion()
        consumer = "acceptance.fate.late_registration"
        try:
            foresight.CONSUMERS[consumer] = foresight.PAGE_TAKEN
            exported = json.loads(json.dumps(story))
            self.assertEqual(exported["ForesightConsumers"][consumer], foresight.PAGE_TAKEN)
        finally:
            foresight.CONSUMERS.pop(consumer, None)

    def test_existing_pilot_keeps_choices_and_misstep_price(self):
        from storylines import wenduag_echo
        story = expansion.make_expansion()
        slot, = foresight.active_echoes()
        self.assertEqual((slot["sense"], slot["wrong"], slot["misstep"], slot["cost"]),
                         ("sight + sound", "white stair, water", "paid runner searches the wrong place", ("Finances", -50)))
        pilot = next(s for s in story["Scenes"] if s["Id"] == slot["host"])
        self.assertEqual(foresight._chapters(pilot), [4])
        self.assertEqual([n["Id"] for n in pilot["Nodes"]], [n["Id"] for n in wenduag_echo.SCENES[0]["Nodes"]])
        for before, after in zip(wenduag_echo.SCENES[0]["Nodes"], pilot["Nodes"]):
            self.assertEqual(len(before["Choices"]), len(after["Choices"]))
            for old, new in zip(before["Choices"], after["Choices"]):
                self.assertTrue({"trickster.now", foresight.PAGE_TAKEN}.issubset(new["Requires"]))
                self.assertEqual({k: v for k, v in old.items() if k != "Requires"},
                                 {k: v for k, v in new.items() if k != "Requires"})

    def test_one_fire_watch_on_both_chapter_lists(self):
        story = expansion.make_expansion()
        setters = [s for s in story["Scenes"] if any(foresight.GATE_WATCH in ch["Set"]
                   for nd in s["Nodes"] for ch in nd["Choices"])]
        self.assertEqual([s["Id"] for s in setters], [foresight.WATCH_SCENE])
        watch = setters[0]
        self.assertEqual(watch["AnswerLists"], ["1a17d8053a3be7f47a7908eb6706f2fe",
                                              "6dccfd39947ef4242a8afbe36b21a46c"])
        self.assertEqual(watch["Chapters"], [3, 5])
        self.assertEqual((watch["MinChapter"], watch["MaxChapter"]), (3, 5))
        self.assertTrue(watch["ReturnToList"])
        self.assertFalse(watch.get("Remote"))
        self.assertFalse(watch.get("InteractionHub"))
        self.assertIn(foresight.GATE_FIRE, watch["Requires"])
        self.assertIn(foresight.GATE_WATCH, watch["Forbids"])
        self.assertIn("fool_king.gone", watch["Forbids"])
        post, leave = watch["Nodes"][0]["Choices"]
        self.assertEqual(post["Crusade"], {"Resource": "Favors", "Amount": -50})
        self.assertTrue(leave["Abort"])
        self.assertEqual(leave["Set"], [])


    def test_watch_memories_follow_the_sold_memory_on_both_hubs(self):
        story = expansion.make_expansion()
        scenes = {s["Id"]: s for s in story["Scenes"]}
        for suffix in ("", "_awning"):
            for scene_id, via, index, target in (
                ("terendelev.trickster.watch.proof", "fear", 0, "try"),
                ("terendelev.trickster.after.first_night", "start", 1, "turnips"),
                ("terendelev.trickster.after.first_night", "sums", 0, "nothing"),
                ("terendelev.trickster.after.first_night", "sums", 1, "breakfast"),
                ("terendelev.trickster.watch.market", "child", 0, "ice"),
                ("terendelev.trickster.after.first_night", "sums", 0, "nothing"),
                ("terendelev.trickster.after.first_night", "sums", 1, "breakfast"),
                ("terendelev.trickster.watch.market", "child", 0, "ice"),
            ):
                host = scenes[scene_id + suffix]
                nodes = {nd["Id"]: nd for nd in host["Nodes"]}
                original = nodes[via]["Choices"][index]
                alternative = next(ch for ch in nodes[via]["Choices"] if ch["Next"] == "gap." + target)
                self.assertEqual(original["Next"], target)
                self.assertEqual(alternative["Next"], "gap." + target)
                for sold in (None, foresight.COST_PROMISE, foresight.COST_SQUARE, foresight.COST_CAVES):
                    flags = {"trickster.ever", foresight.ACCEPTED}
                    if sold in (foresight.COST_PROMISE, foresight.COST_SQUARE):
                        flags.add(foresight.GONE_SQUARE)
                    def shown(choice):
                        return set(choice["Requires"]).issubset(flags) and not set(choice["Forbids"]) & flags
                    choices = [ch for ch in (original, alternative) if shown(ch)]
                    self.assertEqual(len(choices), 1)
                    text = nodes[choices[0]["Next"]]["Text"]
                    if foresight.GONE_SQUARE in flags:
                        self.assertNotIn("the way it went on the square", text)
                        self.assertNotIn("laugh from the square", text)
                        self.assertNotIn("from the square", text)
                    else:
                        self.assertIn("square", text)
                self.assertEqual(nodes["gap." + target]["Choices"], nodes[target]["Choices"])


GAME = Path(os.environ.get("RRT_GAME_DIR") or
            r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure")


@unittest.skipUnless((GAME / "blueprints.zip").exists(), "blueprints.zip not installed")
class ForesightCanonTests(unittest.TestCase):
    def test_chadali_chance_cue_identity(self):
        localization = json.loads((GAME / "Wrath_Data/StreamingAssets/Localization/enGB.json")
                                  .read_text(encoding="utf-8-sig"))["strings"]
        with zipfile.ZipFile(GAME / "blueprints.zip") as blueprints:
            cue = json.loads(blueprints.read("World/Dialogs/c3/Mythic_Trickster/Council_Chadali/Cue_0012.jbp"))
        self.assertEqual(cue["AssetId"], "dc4fa93063e42c44981850d65914402e")
        self.assertTrue(cue["Data"]["$type"].endswith(", BlueprintCue"))
        self.assertIn("I am chance!", localization[cue["Data"]["Text"]["m_Key"]])

    def test_areelu_child_uses_commander_gender(self):
        localization = json.loads((GAME / "Wrath_Data/StreamingAssets/Localization/enGB.json")
                                  .read_text(encoding="utf-8-sig"))["strings"]
        with zipfile.ZipFile(GAME / "blueprints.zip") as blueprints:
            path = next(p for p in blueprints.namelist() if p.endswith("AreeluAllTruth/Cue_0028.jbp"))
            cue = json.loads(blueprints.read(path))
        self.assertEqual(cue["AssetId"], "6c39117f5ee77c34681c4cee77de75b8")
        self.assertEqual(cue["Data"]["Text"]["m_Key"], "bc4189f0-fda1-4cbe-9728-46ac3714dc87")
        native = localization[cue["Data"]["Text"]["m_Key"]]
        self.assertIn("my {mf|son|daughter}", native)
        reaction = "You made a joke over my {mf|son|daughter}'s jar. The jar kept it. So will I."
        for gender in ("son", "daughter"):
            self.assertIn("my " + gender, native.replace("{mf|son|daughter}", gender))
            self.assertIn("my " + gender + "'s jar", reaction.replace("{mf|son|daughter}", gender))
        story = expansion.make_expansion()
        text = "\n".join(n["Text"] for s in story["Scenes"] for n in s["Nodes"])
        self.assertNotIn("my daughter's jar", text)
        self.assertNotIn("Areelu's daughter", text)

    def test_commander_punchline_and_areelu_sacrifice_are_distinct(self):
        localization = json.loads((GAME / "Wrath_Data/StreamingAssets/Localization/enGB.json")
                                  .read_text(encoding="utf-8-sig"))["strings"]
        with zipfile.ZipFile(GAME / "blueprints.zip") as blueprints:
            def read(path):
                return json.loads(blueprints.read(path))

            base = "World/Dialogs/c6/SecondFloor/GrandFinal/"
            commander = read(base + "Answer_0011.jbp")
            areelu = read(base + "Answer_0055.jbp")
            self.assertEqual(commander["AssetId"], "10e6b2a8c754dae4b81e55ad6d0918b2")
            self.assertEqual(areelu["AssetId"], "91c5eca80c8779c4a8bd5754f5533cad")
            self.assertIn("I'm the punchline!", localization[commander["Data"]["Text"]["m_Key"]])
            self.assertIn("Use Areelu's life", localization[areelu["Data"]["Text"]["m_Key"]])
            endings = "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/"
            player_end = "!bp_" + read(endings + "Ending_PlayerSacrifice.jbp")["AssetId"]
            areelu_end = "!bp_" + read(endings + "Ending_AreeluSacrificeTrickster.jbp")["AssetId"]
            for answer, own, other in ((commander, player_end, areelu_end), (areelu, areelu_end, player_end)):
                with self.subTest(answer=answer["AssetId"]):
                    starts = [a["Etude"] for a in answer["Data"]["OnSelect"]["Actions"]
                              if a["$type"].endswith(", StartEtude")]
                    self.assertIn(own, starts)
                    self.assertNotIn(other, starts)


if __name__ == "__main__":
    unittest.main()

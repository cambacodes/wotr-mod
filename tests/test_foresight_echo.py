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
from storylines import foresight  # noqa: E402
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
        self.assertEqual(hosts, PROPOSED)
        self.assertTrue(set(PROPOSED).isdisjoint(foresight.ALLOCATED))
        self.assertEqual(foresight.active_echoes(), [])
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
        self.assertIn("trickster.ever", entry["Requires"])
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


class ForesightSurfaceTests(unittest.TestCase):
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


GAME = Path(os.environ.get("RRT_GAME_DIR") or
            r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure")


@unittest.skipUnless((GAME / "blueprints.zip").exists(), "blueprints.zip not installed")
class ForesightCanonTests(unittest.TestCase):
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

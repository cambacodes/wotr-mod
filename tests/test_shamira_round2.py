"""Round-two history, refusal and cost regressions, using route assembly."""
import copy
import unittest

from storylines import shamira_dream as dream, shamira_mind as mind
from storylines import shamira_trickster as route, shamira_round2 as polish
from tests.test_shamira_partner_stance import walk, visible


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class ShamiraRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = copy.deepcopy(route.SCENES + mind.SCENES + dream.SCENES)
        cls.payload = {"Scenes": copy.deepcopy(cls.base),
                       "Relationships": {"shamira": copy.deepcopy(route.RELATIONSHIP)}}
        dream.integrate(cls.payload)
        cls.by = {s["Id"]: s for s in cls.payload["Scenes"]}

    def nodes(self, suffix):
        return {n["Id"]: n for n in self.by[route.P + suffix]["Nodes"]}

    def test_saved_nodes_and_answers_remain_in_order(self):
        for before in self.base:
            after = self.by[before["Id"]]
            self.assertEqual([n["Id"] for n in before["Nodes"]],
                             [n["Id"] for _, n in zip(before["Nodes"], after["Nodes"])])
            for old, new in zip(before["Nodes"], after["Nodes"]):
                self.assertEqual([a.get("Id") for a in old["Choices"]],
                                 [a.get("Id") if a.get("Id") != "continue" else None
                                  for _, a in zip(old["Choices"], new["Choices"])])
                for a, b in zip(old["Choices"], new["Choices"]):
                    expected = "continue" if (before["Id"] == route.P + "epilogue.late"
                                               and old["Id"] == "page") else a.get("Id")
                    self.assertEqual(expected, b.get("Id"))
        late = next(a for a in self.nodes("epilogue.late")["page"]["Choices"] if a.get("Id") == "continue")
        self.assertEqual(late["Id"], "continue")
        self.assertIsNone(late["Next"])
        self.assertFalse(late["Set"])

    def test_extraction_dispatch_is_native_not_death(self):
        self.assertEqual(self.payload["QuestObjectives"][polish.EXTRACTED],
                         ["62920c1a061578143b4106fc456e6075", "Completed"])
        for suffix in ("killed.voice", "killed.voice_letter"):
            nodes = self.nodes(suffix)
            for flags, expected in ((set(), "cold"), ({polish.EXTRACTED}, "cold_extracted")):
                answers = [a for a in nodes["voice"]["Choices"] if visible(a, flags)]
                self.assertEqual([a["Next"] for a in answers], [expected])

    def test_never_audienced_is_not_witnessed_silence(self):
        for suffix, prefix in (("mind.first_night", "l_"),
                               ("killed.voice_letter", "n_l_"),
                               ("killed.drowning", "n_l_")):
            ask = self.nodes(suffix)[prefix + "ask"]
            answers = [a for a in ask["Choices"] if visible(a, set())]
            self.assertEqual([a["Next"] for a in answers], [prefix + "ask_never_went"])
            answers = [a for a in ask["Choices"] if visible(a, {polish.AUDIENCE})]
            self.assertEqual([a["Next"] for a in answers], [prefix + "silent"])

    def test_visit_has_local_cameos_and_unanswered_invitation(self):
        for suffix in ("", "_awning"):
            s = self.by[route.P + "after.visit" + suffix]
            self.assertNotIn("crossroute.arueshalae.unavailable", s["Forbids"])
            nodes = {n["Id"]: n for n in s["Nodes"]}
            for a in nodes["arueshalae"]["Choices"]:
                if a["Next"] in ("aru_evil", "aru_redeemed"):
                    self.assertIn(polish.ARU_EARNED, a["Requires"])
                    self.assertIn(polish.ARU_PRESENT, a["Requires"])
            self.assertTrue(any(visible(a, set()) and a["Next"] == "aru_absent"
                                for a in nodes["arueshalae"]["Choices"]))
            self.assertNotIn(polish.ACCEPTED, only(nodes["kind"]["Choices"])["Set"])
            self.assertIn(polish.ACCEPTED, only(nodes["come"]["Choices"])["Set"])
            defended = nodes["did_defended"]
            self.assertTrue(any(a["Next"] == "memory_offer" for a in defended["Choices"]))
            edge = nodes["memory_answer_edge"]
            answers = [a for a in edge["Choices"] if visible(a, {polish.EDGE})]
            self.assertEqual([a["Next"] for a in answers], ["body_edge"])

    def test_first_night_requires_her_answer_and_retains_refusals(self):
        for suffix in ("", "_awning"):
            s = self.by[route.P + "harem" + suffix]
            results = walk(s, ("trickster.now",))
            self.assertTrue(any(route.ALLY in flags for flags, _ in results))
            self.assertTrue(any(route.CLOSED in flags for flags, _ in results))
            for flags, trace in results:
                if "explicit.1" in trace:
                    self.assertIn("partner_start", trace)
                    self.assertIn(route.COMMITTED, flags)
                    if route.CLOSED in flags:
                        self.assertGreater(trace.index("partner_broken"), trace.index("explicit.1"))
                if route.ALLY in flags:
                    self.assertNotIn("explicit.1", trace)
            slot = next(n for n in s["Nodes"] if n["Id"] == "explicit.1")
            self.assertEqual(only(slot["Choices"])["Next"], "morning")

    def test_inquiry_survives_both_refusals_and_settles_once(self):
        inquiry = self.by[route.P + "mind.barracks_inquiry"]
        self.assertEqual(inquiry["Relationship"], "shamira_barracks")
        self.assertNotIn("ContactUnit", inquiry)
        for refusal in (route.ALLY, route.CLOSED):
            flags = {"trickster.ever", route.BARRACKS, refusal}
            self.assertTrue(set(inquiry["Requires"]) <= flags)
            self.assertFalse(set(inquiry["Forbids"]) & flags)
            for settled, _ in walk(inquiry, flags):
                self.assertIn(set(settled) & set(polish.SETTLED), [{f} for f in polish.SETTLED])
                self.assertTrue(set(inquiry["Forbids"]) & settled)
        cover = next(a for n in inquiry["Nodes"] if n["Id"] == "chaplain" for a in n["Choices"] if a.get("Crusade", {}).get("Amount") == -150)
        self.assertEqual(cover["Crusade"], {"Resource": "Favors", "Amount": -150})

    def test_dangerous_inspiration_has_actual_order_costs(self):
        nodes = self.nodes("mind.dream")
        patrol = nodes["patrol"]["Choices"]
        self.assertEqual([a.get("Crusade", {}).get("Amount", 0) for a in patrol], [150, 50, 0])
        self.assertEqual(only(nodes["burn"]["Choices"])["Next"], "patrol")


if __name__ == "__main__":
    unittest.main()

"""Situational histories, slot continuity and append-only route changes."""
import copy
import json
from pathlib import Path
import unittest

from storylines import kiana, kiana_native, kiana_round2, kiana_trickster as kt, pacing_pp4
from story_format import c, scene
from tests import test_kiana_partner as partner_tests
from tests.test_kiana_partner import holds, walk


class KianaRound2Tests(unittest.TestCase):
    def ward(self):
        ward = copy.deepcopy(next(s for s in kt.SCENES if s["Id"] == "kiana.trickster.ward_rounds"))
        ward["Nodes"][0]["Choices"].extend(copy.deepcopy(pacing_pp4.ROUNDS_CHOICES))
        ward["Nodes"].extend(copy.deepcopy(pacing_pp4.ROUNDS_NODES))
        payload = dict(Scenes=[ward])
        kt.integrate_ward(payload)
        kiana_round2.integrate(payload)
        return ward

    def test_each_cast_has_postponed_recall_without_a_wedding_disaster(self):
        ward = self.ward()
        pages = {n["Id"]: n for n in ward["Nodes"]}
        for role in ("captive", "hunter", "guest"):
            for recovery in (set(), {kt.WARD_GUESTS_HOME}):
                flags = {kt.H_BETROTHED, "kiana.wedding.cast." + role} | recovery
                recalls = [a for a in pages["start"]["Choices"] if a["Next"].startswith("court_") and holds(a, flags)]
                self.assertEqual([a["Next"] for a in recalls], ["court_" + role + "_postponed"])
                node = pages[recalls[0]["Next"]]
                self.assertNotIn("cup came", node["Text"])
                self.assertEqual(node["Choices"][0]["Next"], "rounds_no_wedding")
                outcomes = walk(ward["Nodes"], node["Id"], flags)
                self.assertTrue(outcomes)
                self.assertTrue(all("kiana.trickster.rounds_kept" in x for x in outcomes))
                self.assertTrue(all("kiana.kissed" not in x and "kiana.committed" not in x for x in outcomes))

    def test_captive_and_recovered_rounds_stay_distinct_for_every_cast(self):
        ward = self.ward()
        pages = {n["Id"]: n for n in ward["Nodes"]}
        for caller in ("start", "wrist_early", "court_captive", "court_hunter", "court_guest"):
            for flags, target in ((set(), "rounds_captive"), ({kt.WARD_GUESTS_HOME}, "rounds")):
                answers = [a for a in pages[caller]["Choices"] if a["Next"].startswith("rounds") and holds(a, flags)]
                self.assertEqual([a["Next"] for a in answers], [target], caller)
                self.assertTrue(walk(ward["Nodes"], target, flags))

    def test_honest_wait_has_an_independent_reply_before_the_invitation(self):
        payload = partner_tests.KianaPartnerTests().payload()
        host = next(s for s in payload["Scenes"] if s["Id"] == "kiana.answer")
        flags = {"trickster.now", "kiana.waited"}
        start = host["Nodes"][0]
        self.assertFalse(any(a["Next"] == "partner_wait" and holds(a, flags) for a in start["Choices"]))
        answer = next(a for a in start["Choices"] if a["Next"] == "reply_waited")
        self.assertTrue(holds(answer, flags))
        pages = {n["Id"]: n for n in host["Nodes"]}
        self.assertEqual(pages["reply_waited"]["Choices"][0]["Next"], "reply_elan")
        self.assertEqual(pages["reply_elan"]["Speaker"], "Elan")
        self.assertEqual(pages["reply_elan"]["Choices"][0]["Next"], "reply_kiana")
        outcomes = walk(host["Nodes"], "reply_waited", flags)
        accepted = [x for x in outcomes if "kiana.available" in x]
        self.assertTrue(accepted)
        self.assertTrue(all("kiana.separated" not in x and "kiana.committed" not in x for x in accepted))

    def test_slot_default_joins_earned_morning_and_keeps_legacy_exit(self):
        date = copy.deepcopy(next(s for s in kiana.SCENES if s["Id"] == "kiana.date"))
        date["Nodes"].extend(copy.deepcopy(kt.DATE_NODES))
        before = copy.deepcopy(date)
        kiana_round2.integrate(dict(Scenes=[date]))
        self.assertEqual([n["Id"] for n in date["Nodes"][:len(before["Nodes"])]],
                         [n["Id"] for n in before["Nodes"]])
        for old_node, new_node in zip(before["Nodes"], date["Nodes"]):
            for old, new in zip(old_node["Choices"], new_node["Choices"]):
                self.assertEqual((old["Next"], old["Set"]), (new["Next"], new["Set"]))
        pages = {n["Id"]: n for n in date["Nodes"]}
        slot = pages["kiana.date.explicit.1"]
        brief = json.loads((Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/kiana/kiana.date.explicit.1.json").read_text(encoding="utf-8"))
        self.assertIn(brief["last_line"].removeprefix("N: "), slot["Text"])
        for flags in ({"trickster.now"}, {"trickster.now", "kiana.partner_unsettled"},
                      {"trickster.now", "kiana.partner_unsettled", "kiana.elan.death_known"}):
            for result in walk(date["Nodes"], slot["Id"], flags):
                self.assertTrue({"kiana.lovers", "kiana.kissed"} <= result)
                self.assertNotIn("kiana.committed", result)
                self.assertNotIn(kt.WARD_GUESTS_HOME, result)
        for nid in ("read", "distance"):
            self.assertTrue(all("kiana.kissed" not in x for x in walk(date["Nodes"], nid, set())))

    def test_native_recovery_never_makes_elan_a_sleeper(self):
        books = copy.deepcopy(kiana_native.SCENES)
        # Only native hosts; no new actor, gate or native override.
        kiana_round2.integrate(dict(Scenes=books))
        for book in books:
            if book["Id"] in ("kiana.native.aftermath_home", "kiana.native.aftermath_6_home"):
                text = book["Nodes"][0]["Text"]
                self.assertNotIn("They have been awake", text)
                self.assertNotIn("discharged", text)
                self.assertIn("trickster.now", book["Requires"])

    def test_discovery_keeps_the_native_public_host_and_closure(self):
        host = next(s for s in partner_tests.KianaPartnerTests().payload()["Scenes"] if s["Id"] == "kiana.partner_discovery")
        self.assertEqual(host["AnswerLists"], ["a237e3aaab7c937468829bba3578770d"])
        self.assertNotIn("stairs", host["Nodes"][0]["Text"])
        for flags in ({"trickster.now", "kiana.partner_stance.secret"},):
            for outcome in walk(host["Nodes"], "start", flags):
                self.assertTrue({"kiana.partner_secret_exposed", "kiana.closed", "kiana.stayed_married"} <= outcome)


if __name__ == "__main__":
    unittest.main()

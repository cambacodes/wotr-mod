"""Exercise divergent settlements, receipt delivery and epilogue claims."""
import unittest

from tests.story_fixture import fresh_story
from tools import rrt_verify as verify

K = "konomi.trickster."


class KonomiRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.by = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.model = verify.Model(cls.story)

    def node(self, sid, nid):
        return next(n for n in self.by["konomi." + sid]["Nodes"] if n["Id"] == nid)

    @staticmethod
    def selectable(choice, flags):
        return set(choice.get("Requires", [])) <= flags and not set(choice.get("Forbids", [])) & flags

    def test_each_political_settlement_reaches_its_own_breakfast(self):
        cut = self.node("trickster.dismissed.private", "konomi.trickster.dismissed.private.explicit.1")
        for bargain, expected in (("paid", "morning"), ("paid_envoy", "morning"), ("favour", "morning_favour")):
            flags = set(self.node("trickster.dismissed.terms", bargain)["Choices"][0]["Set"])
            choices = [ch for ch in cut["Choices"] if self.selectable(ch, flags)]
            self.assertEqual([expected], [ch["Next"] for ch in choices])
            breakfast = self.node("trickster.dismissed.private", expected)
            self.assertTrue(breakfast["Choices"])
            if bargain == "favour":
                self.assertNotIn("Drezen's reserve and your endorsement", breakfast["Text"])
                self.assertIn("still mine to name", breakfast["Text"])
            else:
                self.assertIn("Drezen's reserve and your endorsement", breakfast["Text"])

    def test_whole_return_histories_leave_one_letter_or_two_with_fallback(self):
        prefix = "konomi.trickster."
        chains = (
            (5, ["dead.recalled", "dismissed.late", "dismissed.arrival"], 1),
            (5, ["never_arrived.accredited", "never_arrived.arrival", "never_arrived.audience_letter"], 1),
            (3, ["never_arrived.accredited", "never_arrived.arrival", "dead.recalled"], 1),
            (3, ["never_arrived.accredited", "never_arrived.arrival", "never_arrived.audience_letter", "dead.recalled"], 2),
        )
        for chapter, chain, letters in chains:
            hosts = [self.by[prefix + sid] for sid in chain]
            self.assertTrue(all(chapter in s["Chapters"] for s in hosts))
            self.assertEqual(letters, sum(bool(s.get("Remote")) for s in hosts))
            for s in hosts:
                if not s.get("Remote"):
                    self.assertEqual("b5e867e13503c6f41bb1316705efb4a2", s["ContactUnit"])
                    self.assertEqual(["33960c7f7af40cd43b7f801a76c87a0b"], s["AnswerLists"])
                    # No circular requirement for the actor the receipt unhides.
                    self.assertNotIn("konomi.present_now", s["Requires"])

    def test_paid_and_favour_histories_cannot_invent_an_envoy_appointment(self):
        pages = 0
        for s in self.story["Scenes"]:
            if s.get("Relationship") != "konomi" or s.get("Owner") != "Epilogue":
                continue
            for n in s["Nodes"]:
                paras = n.get("Paragraphs", [])
                for para in paras:
                    if "new envoy to Drezen had been appointed" not in para["Text"]:
                        continue
                    pages += 1
                    for settlement in ("paid_envoy", "favour"):
                        flags = {K + "recessed", K + "cost.outfoxed"}
                        flags.update(self.node("trickster.dismissed.terms", settlement)["Choices"][0]["Set"])
                        self.assertFalse(self.selectable(para, flags))
                        gossip = [p for p in paras if "supplied the driver's account" in p["Text"]]
                        self.assertEqual(1, len(gossip))
                        self.assertTrue(self.selectable(gossip[0], flags))
                        flags.update(self.node("trickster.dismissed.private", "envoy")["Choices"][0]["Set"])
                        self.assertTrue(self.selectable(para, flags))
                        self.assertFalse(self.selectable(gossip[0], flags))
        self.assertGreaterEqual(pages, 18)

    def test_all_register_copies_keep_the_signed_correction(self):
        copies = [p for s in self.story["Scenes"] if s.get("Relationship") == "konomi"
                  for n in s["Nodes"] for p in n.get("Paragraphs", [])
                  if "Royal Council's register" in p["Text"]]
        self.assertGreaterEqual(len(copies), 18)
        for para in copies:
            self.assertIn("signed correction", para["Text"])
            self.assertIn("dovecote", para["Text"])
            self.assertIn("two dates", para["Text"])
            self.assertIn("witnessed arrival", para["Text"])
            self.assertIn("konomi.trickster.returned", para["Requires"])
            self.assertIn("konomi.trickster.cost.accredited", para["Requires"])

    def test_new_lastcall_obligation_requires_an_actual_acceptance(self):
        page = self.by["konomi.lastcall.page"]
        accepted = next(p for p in page["Nodes"][0]["Paragraphs"] if "acceptance of her political terms" in p["Text"])
        call = self.by["konomi.lastcall.call"]
        terms = next(n for n in call["Nodes"] if n["Id"] == "terms")
        self.assertEqual(3, len(terms["Choices"]))
        flags = {"konomi.lastcall.called"}
        self.assertFalse(self.selectable(accepted, flags))
        for choice in terms["Choices"][1:]:
            self.assertFalse(self.selectable(accepted, flags | set(choice["Set"])))
        acceptance = next(n for n in call["Nodes"] if n["Id"] == terms["Choices"][0]["Next"])
        self.assertTrue(self.selectable(accepted, flags | set(acceptance["Choices"][0]["Set"])))
        collections = [p for s in self.story["Scenes"] if s.get("Relationship") == "konomi"
                       for n in s["Nodes"] for p in n.get("Paragraphs", [])
                       if "political terms of its collection" in p["Text"]]
        self.assertTrue(collections)
        for para in collections:
            outstanding = flags | {K + "favour_owed"}
            self.assertFalse(self.selectable(para, outstanding))
            self.assertTrue(self.selectable(para, outstanding | {"konomi.lastcall.terms_accepted"}))

    def test_actual_settlement_receipts_control_the_lastcall_account(self):
        for sid, nid, history, due in (
            ("trickster.dismissed.terms", "paid", K + "cost.debt_owed", False),
            ("trickster.dismissed.terms", "paid_envoy", K + "cost.debt_owed", False),
            ("trickster.dismissed.terms", "favour", K + "cost.debt_owed", True),
            ("trickster.dead.consultation", "paid", K + "cost.consult_fee", False),
        ):
            state = verify.SimState(5, 100)
            state.flags.update({"trickster", "trickster.ever", "trickster.lastcall.open", history})
            state.flags.update(self.node(sid, nid)["Choices"][0]["Set"])
            verify.sim_complete(self.model, state)
            self.assertEqual(due, "konomi.lastcall.favour_due" in state.flags, nid)
            self.assertEqual(due, "konomi.lastcall.account_due" in state.flags, nid)


if __name__ == "__main__":
    unittest.main()

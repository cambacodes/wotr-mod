"""Played-history regressions for D29/D30's dispatch and delivery boundaries."""
import unittest

from storylines import kiana_partner as kp, kiana_round4 as r4
import test_kiana_partner as partner_tests

holds = partner_tests.holds
walk = partner_tests.walk


class KianaRound4Tests(unittest.TestCase):
    def setUp(self):
        self.books = {s["Id"]: s for s in partner_tests.KianaPartnerTests().payload()["Scenes"]}
        self.flags = {"trickster.now", "trickster.ever", kp.OPEN,
                      "kiana.company", "kiana.rehearsed", "kiana.lovers", "kiana.trickster.met"}

    def assert_uncommitted(self, flags):
        self.assertFalse(flags & {kp.SHARE, kp.EXCLUSIVE, "kiana.separated",
                                  "kiana.committed", "kiana.trickster.late_yes"})

    def play(self, sid, entry, flags):
        return walk(self.books[sid]["Nodes"], entry, flags)

    def test_shared_dispatch_waits_for_a_later_answer_in_both_hosts(self):
        for sid in r4.HOSTS:
            host = self.books[sid]
            sent, = self.play(sid, "partner_share", self.flags)
            self.assertIn(r4.SHARE_SENT, sent)
            self.assert_uncommitted(sent)
            self.assertTrue(set(r4.PENDING) <= set(host["Forbids"]))
            reply = self.books[sid + ".elan_reply"]
            self.assertIn(r4.SHARE_SENT, reply["Requires"])
            self.assertEqual(reply["DelayHours"], 48)
            results = self.play(reply["Id"], "partner_elan_terms", sent)
            accepted = [state for state in results if kp.SHARE in state]
            self.assertTrue(accepted)
            self.assertTrue(all({"kiana.committed", "kiana.trickster.late_yes",
                                 "kiana.partner_elan_terms_kept"} <= state for state in accepted))
            refused = [state for state in results if "kiana.closed" in state]
            self.assertTrue(refused)
            for state in refused:
                self.assert_uncommitted(state)

    def test_exclusive_reply_and_delivery_are_separate_played_interactions(self):
        for sid in r4.HOSTS:
            sent, = self.play(sid, "partner_breakup", self.flags)
            self.assertIn(r4.BREAKUP_SENT, sent)
            self.assert_uncommitted(sent)
            reply = self.books[sid + ".elan_parting"]
            self.assertTrue(reply["Remote"])
            self.assertNotIn("ContactUnit", reply)
            self.assertIn(r4.BREAKUP_SENT, reply["Requires"])
            self.assertEqual(reply["DelayHours"], 48)
            waiting, = self.play(reply["Id"], "partner_breakup", sent)
            self.assertIn(r4.DELIVERY_WAIT, waiting)
            self.assert_uncommitted(waiting)
            after = self.books[sid + ".after_delivery"]
            self.assertIn(r4.DELIVERY_WAIT, after["Requires"])
            self.assertEqual(after["DelayHours"], 24)
            settled, = self.play(after["Id"], "partner_exclusive_yes", waiting)
            self.assertTrue({kp.EXCLUSIVE, "kiana.separated", "kiana.committed",
                             "kiana.partner_breakup_spoken", "kiana.trickster.late_yes"} <= settled)
            self.assertNotIn(kp.SHARE, settled)

    def test_live_and_postal_followups_keep_presence_and_choice_identity(self):
        for sid in r4.HOSTS:
            original = self.books[sid]
            for suffix in (".elan_reply", ".elan_parting", ".after_delivery"):
                followup = self.books[sid + suffix]
                self.assertEqual(followup["Relationship"], "kiana")
                for flag in original["Forbids"]:
                    if flag not in r4.PENDING:
                        self.assertIn(flag, followup["Forbids"])
                self.assertTrue(set(original["Requires"]) <= set(followup["Requires"]))
                self.assertTrue(all(not node.get("Paragraphs") for node in followup["Nodes"]))
            nodes = {n["Id"]: n for n in original["Nodes"]}
            for name in ("partner_share", "partner_breakup"):
                self.assertEqual(nodes[name]["Choices"][0]["Next"],
                                 "partner_elan_terms" if name == "partner_share" else "partner_elan_breakup")
                self.assertFalse(holds(nodes[name]["Choices"][0], self.flags))
            for name in ("partner_elan_terms", "partner_elan_breakup", "partner_share_yes",
                         "partner_exclusive_yes", "promise_accepted"):
                self.assertIn(name, nodes)

    def test_physical_request_can_finish_by_post_if_placement_later_fails(self):
        sent, = self.play(r4.HOSTS[0], "partner_share", self.flags)
        postal = self.books[r4.HOSTS[1] + ".elan_reply"]
        self.assertNotIn(kt_placed_failed := "kiana.presence.failed", sent)
        self.assertIn(kt_placed_failed, postal["Requires"])
        accepted = [state for state in self.play(postal["Id"], "partner_elan_terms",
                    sent | {kt_placed_failed}) if kp.SHARE in state]
        self.assertTrue(accepted)


if __name__ == "__main__":
    unittest.main()

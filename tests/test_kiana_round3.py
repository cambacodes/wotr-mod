"""Continuity counterexamples from the round-2 audit, using route graphs."""
import copy
import unittest

from storylines import kiana, kiana_further, kiana_followthrough, kiana_round2
from storylines import kiana_round3 as r3, kiana_partner as kp, kiana_trickster as kt
from story_format import c, n, scene
import test_kiana_partner as partner_tests

holds = partner_tests.holds
walk = partner_tests.walk


class KianaRound3Tests(unittest.TestCase):
    def payload(self):
        return partner_tests.KianaPartnerTests().payload()

    def test_waited_reply_records_knowledge_without_a_lifetime_stance(self):
        host = next(s for s in self.payload()["Scenes"] if s["Id"] == "kiana.answer")
        accepted = [f for f in walk(host["Nodes"], "reply_waited", {"trickster.now", "kiana.waited"})
                    if "kiana.available" in f]
        self.assertTrue(accepted)
        for flags in accepted:
            self.assertIn(r3.INFORMED, flags)
            self.assertFalse(flags & {kp.SHARE, kp.EXCLUSIVE, kp.SECRET, "kiana.committed"})

    def test_unsettled_late_yes_never_enters_the_celebration_first(self):
        for host in self.payload()["Scenes"]:
            if host["Id"] not in ("kiana.trickster.late_question", "kiana.trickster.late_question_letter"):
                continue
            start = host["Nodes"][0]
            for informed in (set(), {r3.INFORMED}):
                flags = {"trickster.now", "trickster.ever", kp.OPEN} | informed
                targets = {a["Next"] for a in start["Choices"] if holds(a, flags)}
                self.assertNotIn("yes", targets)
                self.assertIn("partner_terms_informed" if informed else "partner_terms", targets)
                for result in walk(host["Nodes"], "partner_terms_informed" if informed else "partner_terms", flags):
                    if "kiana.closed" in result:
                        self.assertNotIn("kiana.committed", result)

    def test_postal_negotiation_has_no_unearned_meeting(self):
        host = next(s for s in self.payload()["Scenes"] if s["Id"] == "kiana.trickster.late_question_letter")
        for node in host["Nodes"]:
            if not node["Id"].startswith("partner_"):
                continue
            for phrase in ("writes beside you", "across the table", "at her throat", "takes the page back", "looks at the script"):
                self.assertNotIn(phrase, node["Text"], node["Id"])

    def test_epilogue_summaries_follow_the_selected_outcome_once(self):
        host = next(s for s in self.payload()["Scenes"] if s["Id"] == "kiana.trickster.epilogue.commit")
        ns = {n["Id"]: n for n in host["Nodes"]}
        for node in host["Nodes"]:
            if node["Id"] not in ("margin", "stage", "blank") and not node["Id"].startswith("partner_resolved_"):
                self.assertTrue(all("trickster.ever" in p["Forbids"] for p in node.get("Paragraphs", [])))
        flags = {kp.OPEN, "trickster.now", "trickster.ever"}
        a = next(a for a in ns["partner_share_yes"]["Choices"] if holds(a, flags))
        self.assertEqual(a["Next"], "partner_resolved_share_yes")
        self.assertIn(kp.SHARE, a["Set"])
        self.assertTrue(ns["partner_resolved_share_yes"]["Paragraphs"])

    def test_both_ordinary_intimacy_extensions_have_one_complete_path(self):
        scenes = copy.deepcopy(kiana_followthrough.SCENES + kiana_further.SCENES)
        kiana_round2.integrate({"Scenes": scenes})
        for sid in ("kiana.ink_after", "kiana.unborrowed_evening"):
            host = next(s for s in scenes if s["Id"] == sid)
            kiss = next(n for n in host["Nodes"] if n["Id"] == "kiss")
            active = [a for a in kiss["Choices"] if holds(a, set())]
            intimate = [a for a in active if a["Next"] == sid + ".explicit.1"]
            self.assertEqual(len(intimate), 1)
            self.assertFalse(any(a["Next"] is None and not a["Abort"] for a in active))
            self.assertTrue(walk(host["Nodes"], intimate[0]["Next"], set()))

    def test_morning_separates_the_dispatched_answer_from_guest_recovery(self):
        date = copy.deepcopy(next(s for s in kiana.SCENES if s["Id"] == "kiana.date"))
        date["Nodes"].extend(copy.deepcopy(kt.DATE_NODES))
        kiana_round2.integrate({"Scenes": [date]})
        ns = {n["Id"]: n for n in date["Nodes"]}
        for informed in (set(), {r3.INFORMED}):
            flags = {kp.OPEN} | informed
            active = [a for a in ns["morning_after"]["Choices"] if holds(a, flags)]
            target = "morning_account_informed" if informed else "morning_account"
            self.assertEqual([a["Next"] for a in active], [target])
            for state, expected in ((set(), "morning_guests_captive"),
                                    ({kt.WARD_GUESTS_HOME}, "morning_guests_home"),
                                    ({kt.H_BETROTHED}, "morning_guests_uncaptured"),
                                    ({kt.H_BETROTHED, kt.WARD_GUESTS_HOME}, "morning_guests_uncaptured")):
                answers = [a for a in ns[target]["Choices"] if holds(a, flags | state)]
                self.assertEqual([a["Next"] for a in answers], [expected])
                self.assertTrue(all("kiana.lovers" in r for r in walk(date["Nodes"], target, flags | state)))

    def endings(self):
        scenes = [scene(sid, "", "Epilogue", 5, "", [
            n("start", "Narrator", "", c(), paragraphs=copy.deepcopy(kp.partner_paragraphs()))],
            Relationship="kiana") for sid in ("kiana.ending_apart", "kiana.ending_sacrifice", "kiana.lastcall.page")]
        r3.integrate({"Scenes": scenes})
        return scenes

    def test_ending_secrecy_hides_only_the_new_promise_when_visits_were_agreed(self):
        for host in self.endings():
            for dead in (set(), {kp.DEAD}):
                flags = {kp.SECRET, kp.LIVE, r3.INFORMED} | dead
                rendered = "\n".join(p["Text"] for p in host["Nodes"][0]["Paragraphs"] if holds(p, flags))
                self.assertNotIn("believing Kiana's private invitations concerned her play", rendered)
                self.assertNotIn("before the hidden affair could be confessed", rendered)
                self.assertIn("promise", rendered)

    def test_closed_and_unreturned_histories_have_no_continuing_shared_evenings(self):
        for host in self.endings():
            flags = {kp.SHARE, kp.LIVE, "engine.l12.commander_unreturned"}
            rendered = "\n".join(p["Text"] for p in host["Nodes"][0]["Paragraphs"] if holds(p, flags))
            self.assertNotIn("kept evenings for Elan as well as the Commander", rendered)
            if host["Id"] == "kiana.lastcall.page":
                flags.remove("engine.l12.commander_unreturned")
                rendered = "\n".join(p["Text"] for p in host["Nodes"][0]["Paragraphs"] if holds(p, flags))
                self.assertIn("agreed to the Commander's visits", rendered)

    def test_discovery_preserves_early_knowledge_and_the_same_fallout(self):
        books = {s["Id"]: s for s in self.payload()["Scenes"]}
        for sid, entry, target in (("kiana.partner_discovery", "start", "kiana_informed"),
                                   ("kiana.seelah", "partner_discovery", "partner_elan_letter_informed")):
            host = books[sid]
            ns = {n["Id"]: n for n in host["Nodes"]}
            flags = {kp.SECRET, r3.INFORMED}
            self.assertEqual([a["Next"] for a in ns[entry]["Choices"] if holds(a, flags)], [target])
            for outcome in walk(host["Nodes"], entry, flags):
                self.assertTrue({kp.EXPOSED, "kiana.closed", "kiana.stayed_married"} <= outcome)
                self.assertNotIn("kiana.separated", outcome)


if __name__ == "__main__":
    unittest.main()

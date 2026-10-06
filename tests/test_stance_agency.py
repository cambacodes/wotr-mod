"""Earned answers and event-driven discovery on the seven live stances."""
import unittest

from story_fixture import fresh_story
from tools.rrt_verify import Model, SimState, sim_complete
from storylines import (anevia_partner_stance as a, jerribeth_partner as j,
                        kiana_partner as k, nocticula_partners as no,
                        shamira_partner as sh, soana_partner as so,
                        wenduag_partner_stance as w)


def visible(answer, flags):
    return (set(answer.get("Requires", ())) <= flags
            and not set(answer.get("Forbids", ())) & flags
            and all(set(group) & flags for group in answer.get("AnyGroups", ())))


class StanceAgencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = Model(cls.story)
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def normalized(self, flags):
        state = SimState(5, 0)
        state.flags = set(flags)
        sim_complete(self.model, state)
        return state.flags

    def walk(self, sid, start, flags, stops=()):
        nodes = {node["Id"]: node for node in self.scenes[sid]["Nodes"]}
        pending = [(start, set(flags), ())]
        ends = []
        while pending:
            key, held, trace = pending.pop()
            held = self.normalized(held)
            if key in stops:
                ends.append((held, (*trace, key)))
                continue
            self.assertNotIn(key, trace, (sid, key))
            answers = [c for c in nodes[key]["Choices"] if visible(c, held)]
            self.assertTrue(answers, (sid, key, sorted(held)))
            for answer in answers:
                after = held | set(answer["Set"])
                if answer.get("Next"):
                    pending.append((answer["Next"], after, (*trace, key)))
                elif not answer.get("Abort"):
                    ends.append((self.normalized(after), (*trace, key)))
        return ends

    def test_page_and_current_path_alone_never_earn_exclusivity(self):
        flags = self.normalized({"trickster", "trickster.foresight.accepted", "foresight.page_taken"})
        for receipt in (j.EARNED, no.EARNED, sh.EARNED, w.EARNED):
            self.assertNotIn(receipt, flags)
        proofs = {
            j.EARNED: {"jerribeth.shared_work"},
            no.EARNED: {"noct.acq.concession_delivered"},
            sh.EARNED: {sh.P + "told_honest", sh.P + "ramisa_fooled"},
            w.EARNED: {w.W + "cairn.water"},
        }
        for receipt, evidence in proofs.items():
            self.assertIn(receipt, self.normalized({"trickster", *evidence}))
            self.assertNotIn(receipt, self.normalized(evidence))
        # Naming a forfeit or promising a kill is not completed work or care.
        self.assertNotIn(j.EARNED, self.normalized({"trickster", "jerribeth.trickster.forfeit_named"}))
        self.assertNotIn(w.EARNED, self.normalized({"trickster", w.W + "death_promised"}))

    def test_jerribeth_answers_work_and_current_custody(self):
        sid = "jerribeth.future"
        for proof, expected in ((set(), False), ({"jerribeth.shared_work"}, True)):
            results = self.walk(sid, "partner_answer_plant", {"trickster", j.PLANT, *proof}, ("partner_resume",))
            self.assertEqual(any(j.CHOSEN in flags for flags, _ in results), expected)
            self.assertTrue(any(j.SHARE in flags for flags, _ in results))
            if not expected:
                self.assertTrue(any(j.REFUSED in flags and "jerribeth.closed" in flags for flags, _ in results))
            for flags, _ in results:
                if j.CHOSEN in flags:
                    self.assertIn("jerribeth.trickster.cost.forfeit", flags)
                    self.assertNotIn(j.DEAD, flags)
        # Paid work cannot summon a living possession through a bodiless tenant.
        results = self.walk(sid, "partner_answer_distant", {"trickster", j.PLANT, j.RETURNED, "jerribeth.shared_work"}, ("partner_resume",))
        self.assertFalse(any(j.CHOSEN in flags for flags, _ in results))

    def test_kiana_chooses_after_company_and_rehearsal(self):
        for proof, expected in ((set(), False), ({"kiana.company", "kiana.rehearsed"}, True),
                                ({"kiana.trickster.met", "kiana.rehearsed"}, True), ({"kiana.trickster.met"}, False)):
            results = self.walk("kiana.morning", "partner_answer", {"trickster", k.OPEN, *proof})
            self.assertEqual(any(k.EXCLUSIVE in flags and "kiana.separated" in flags for flags, _ in results), expected)
            if not expected:
                self.assertTrue(any(k.SHARE in flags and "kiana.committed" in flags for flags, _ in results))
                self.assertTrue(any(k.EXCLUSIVE in flags and "kiana.closed" in flags for flags, _ in results))
        coerced = self.walk("kiana.morning", "partner_refuse", {"trickster", k.OPEN})
        self.assertTrue(any(k.SHARE in flags and "kiana.committed" in flags for flags, _ in coerced))
        self.assertTrue(any(k.EXCLUSIVE in flags and "kiana.closed" in flags for flags, _ in coerced))

    def test_nocticula_and_shamira_have_earned_yes_and_refusal(self):
        sid = "nocticula.trickster.partner_terms.threshold"
        for proof, expected in ((set(), False), ({"noct.acq.concession_delivered"}, True)):
            results = self.walk(sid, "terms.alive.answer", {"trickster", *proof})
            self.assertEqual(any(no.CHOSEN in flags for flags, _ in results), expected)
            self.assertTrue(any(no.P + "share" in flags for flags, _ in results))
            if not expected:
                self.assertTrue(any(no.REFUSED in flags and "noct.closed" in flags for flags, _ in results))
        for proof, expected in ((set(), False), ({sh.P + "told_honest", sh.P + "ramisa_fooled"}, True)):
            for suffix in ("", "_awning"):
                results = self.walk(sh.P + "harem" + suffix, "partner_answer", {"trickster", *proof}, ("rise",))
                self.assertEqual(any(sh.CHOSEN in flags for flags, _ in results), expected)
                if not expected:
                    self.assertTrue(any(sh.SHARE in flags for flags, _ in results))
                    self.assertTrue(any(sh.EXCLUSIVE in flags and sh.CLOSED in flags for flags, _ in results))
                self.assertFalse(any("noct.closed" in flags for flags, _ in results))

    def test_soana_and_wenduag_answer_the_existing_run(self):
        for proof, expected in ((set(), False), ({"soana.late_thorn_tested"}, True)):
            results = self.walk("soana.the_days_she_counted", "partner_exclusive_commit_answer", {"trickster", *proof})
            self.assertEqual(any(so.CHOSEN in flags for flags, _ in results), expected)
            if not expected:
                self.assertTrue(any(so.SHARE in flags and "soana.committed" in flags for flags, _ in results))
                self.assertTrue(any(so.EXCLUSIVE in flags and "soana.late_romance_ended" in flags for flags, _ in results))
        for proof, expected in ((set(), False), ({w.W + "cairn.water"}, True)):
            results = self.walk(w.W + "court.claim", "partner_exclusive_answer", {"trickster", *proof}, ("want",))
            self.assertEqual(any(w.EXCLUSIVE in flags and w.CLOSED not in flags for flags, _ in results), expected)
            if not expected:
                self.assertTrue(any(w.SHARE in flags for flags, _ in results))
                self.assertTrue(any(w.REFUSED in flags and w.CLOSED in flags for flags, _ in results))

    def test_secret_discovery_reads_evidence_and_keeps_consequences(self):
        elan = self.scenes["kiana.partner_discovery"]
        self.assertTrue(visible(elan, self.normalized({"trickster", k.SECRET})))
        self.assertFalse(visible(elan, self.normalized({"trickster", k.SECRET, k.CAREFUL})))
        self.assertTrue(visible(elan, self.normalized({"trickster", k.SECRET, k.CAREFUL, k.TRAIL})))
        for careful in (False, True):
            flags = {"trickster", so.SECRET, so.PURSUED, "soana.committed"}
            if careful:
                flags.add(so.CAREFUL)
            results = self.walk(so.K + "homecoming", "start", flags)
            self.assertTrue(results)
            for after, trace in results:
                hidden = "hidden" in trace
                self.assertEqual(so.EXPOSED in after, not hidden)
                self.assertEqual(so.BROKEN in after, not hidden)
                self.assertIn(so.CONFIRMED, after)
            self.assertEqual(any("hidden" in trace for _, trace in results), careful)
        morning = self.scenes[w.W + "react.lann_secret"]
        self.assertIn(w.CAREFUL, morning["Forbids"])
        quiet = self.scenes[w.W + "react.lann_secret_quiet"]
        self.assertIn(w.CAREFUL, quiet["Requires"])
        self.assertFalse(quiet["Reaction"])
        self.assertNotIn(w.DISCOVERED, quiet["Nodes"][0]["Choices"][0]["Set"])

    def test_queen_absence_is_not_an_irabeth_survival_or_return_receipt(self):
        page = self.scenes["anevia.a_key_that_is_hers"]["Nodes"][0]
        quiet = next(c for c in page["Choices"] if c.get("Next") == "partner_absent_night")
        self.assertTrue(visible(quiet, {"irabeth_away"}))
        for changed in ("irabeth_dead", "irabeth_gone", *a.SURVIVAL):
            self.assertFalse(visible(quiet, {"irabeth_away", changed}), changed)
        for scene in self.story["Scenes"]:
            if scene.get("Relationship") != "anevia":
                continue
            for node in scene["Nodes"]:
                for answer in node["Choices"]:
                    if (answer.get("Next") or "").endswith("absent_night"):
                        self.assertTrue(set(("irabeth_dead", "irabeth_gone", *a.SURVIVAL)) <= set(answer["Forbids"]))

    def test_soanas_paid_search_carries_the_exclusive_answer(self):
        flags = {"trickster", so.EXCLUSIVE, so.CHOSEN, so.PURSUED, "soana.committed"}
        results = self.walk(so.K + "homecoming", "start", flags)
        self.assertTrue(results)
        for after, trace in results:
            self.assertIn("exclusive", trace)
            self.assertIn(so.CONFIRMED, after)
            self.assertIn(so.SEPARATED, after)
            self.assertNotIn(so.EXPOSED, after)
            self.assertNotIn(so.BROKEN, after)
        # Withholding his letter still costs the romance on the new stance.
        results = self.walk(so.K + "returned_letter", "start", flags | {so.BURIED})
        self.assertTrue(all(so.BROKEN in after and so.SEPARATED in after for after, _ in results))

    def test_careful_secrets_can_hold_but_deliberate_lingering_exposes(self):
        # The quiet late evening still pays the original memory collection.
        late = self.scenes["jerribeth.trickster.epilogue.commit"]
        for node in late["Nodes"]:
            if node["Id"].startswith("partner_private_"):
                self.assertEqual(node["Choices"][0]["Next"], "collected")
        results = self.walk(sh.P + "harem", "go", {"trickster", sh.SECRET, sh.CAREFUL})
        self.assertTrue(any(sh.EXPOSED not in flags and "partner_private_exit" in trace for flags, trace in results))
        self.assertTrue(any(sh.EXPOSED in flags for flags, _ in results))
        results = self.walk("anevia.the_last_ordinary_thing", "start", {"trickster", "chapter_later", a.SECRET, a.CAREFUL})
        self.assertTrue(any(a.EXPOSED not in flags for flags, _ in results))
        self.assertTrue(any(a.EXPOSED in flags and "anevia.closed" in flags for flags, _ in results))
        dead = self.walk("anevia.the_last_ordinary_thing", "start", {"trickster", "chapter_later", a.SECRET, a.CAREFUL, "irabeth_dead"})
        self.assertTrue(dead)
        self.assertTrue(all(a.EXPOSED not in flags for flags, _ in dead))
        results = self.walk("noct.second_door", "end", {"trickster", no.P + "secret", no.CAREFUL, no.TERMS})
        self.assertTrue(results)
        self.assertTrue(any(no.EXPOSED not in flags for flags, _ in results))
        self.assertTrue(any(no.EXPOSED in flags for flags, _ in results))

    def test_no_live_bond_in_the_three_uncertain_routes(self):
        for route in ("aranka", "nidalynn", "yaniel"):
            self.assertFalse(any(flag.startswith(route + ".partner_stance.")
                                 for scene in self.story["Scenes"] for node in scene["Nodes"]
                                 for choice in node["Choices"] for flag in choice["Set"]))

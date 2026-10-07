"""Situation histories and earned receipts for Dorgelinda's second polish round."""
import copy
import json
from pathlib import Path
import unittest

from storylines import dorgelinda_ledger as l, dorgelinda_trickster as t
from tests.test_dorgelinda_polish import visible


class RoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = {"Scenes": copy.deepcopy(t.SCENES + l.SCENES)}
        t.integrate(cls.payload)
        l.integrate(cls.payload)
        cls.scenes = {s["Id"]: s for s in cls.payload["Scenes"]}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]["Nodes"] if n["Id"] == node)

    def answers(self, scene, node, flags):
        return [c for c in self.node(scene, node)["Choices"] if visible(c, flags)]

    def test_professional_progress_cannot_be_late_acceptance(self):
        self.assertEqual(t.DERIVED[t.P + "late_committed"],
                         [["trickster.ever", t.COMMITTED, "dorgelinda.outcome.accepted"]])
        self.assertEqual(t.DERIVED["dorgelinda.outcome.accepted"], [[t.COMMITTED]])
        for nid in ("clean", "dirty"):
            self.assertNotIn(t.COMMITTED, self.node(t.P + "after.fellows_methods", nid)["Choices"][0]["Set"])

    def test_disclosure_pays_before_renewed_request_and_she_answers(self):
        sid = t.P + "after.second_ask"
        payment = self.node(sid, "price")["Choices"][0]
        self.assertEqual(payment["Crusade"]["Amount"], -100)
        self.assertEqual(payment["Set"], [t.TOLD_ALL])
        request = self.node(sid, "told")["Choices"][0]
        self.assertFalse(request["Set"])
        self.assertEqual(request["Next"], "accepted")
        answer = self.node(sid, "accepted")
        self.assertIn("puts it in your hand", answer["Text"])
        self.assertEqual(answer["Choices"][0]["Set"], [t.COMMITTED, t.TOLD_ALL])

    def test_recovery_precedes_actual_requisition_and_crisis(self):
        sid = t.P + "after.fellows_methods"
        flags = {l.REQUISITIONS, t.CONSCIENCE}
        answers = self.answers(sid, "door", flags)
        self.assertEqual([a["Next"] for a in answers], ["conscience"])
        self.assertEqual(self.payload["SeenCues"][l.REQUISITIONS],
                         ["1576c91c20be9064083a3181abb354a9"])
        self.assertNotIn("sack of oats", self.node(sid, "start")["Text"])
        self.assertIn("in her own hand", self.node(sid, "start_surplus")["Text"])
        for flags in ({t.CONSCIENCE}, {t.CONSCIENCE, l.RATIONS_EQUAL, l.RATIONS_LIE}):
            self.assertEqual([a["Next"] for a in self.answers(l.RATIONS, "start", flags)],
                             ["provisioned"])
        self.assertIn("donations are in", self.node(l.RATIONS, "provisioned")["Text"])

    def test_delivery_awards_stock_once_and_sealing_awards_none(self):
        self.assertNotIn("Crusade", self.node(l.DEBTS, "forge")["Choices"][0])
        for nid, amount in (("twice", 100), ("honest", 75), ("fence", 100)):
            fresh = self.answers(l.HELMETS, nid, set())
            received = self.answers(l.HELMETS, nid, {l.L + "helmets_received"})
            self.assertEqual(len(fresh), 1)
            self.assertEqual(fresh[0]["Crusade"]["Amount"], amount)
            self.assertEqual(len(received), 1)
            self.assertNotIn("Crusade", received[0])

    def test_all_quarrel_exits_inherit_loss_and_repairs_cannot_mint_stock(self):
        loss = self.answers(l.QUARREL_SCENE, "start", set())
        self.assertEqual(len(loss), 1)
        self.assertEqual(loss[0]["Crusade"]["Amount"], -150)
        self.assertIn(l.ALLOTMENT_LOST, loss[0]["Set"])
        self.assertNotIn("Crusade", self.answers(l.QUARREL_SCENE, "start", {l.ALLOTMENT_LOST})[0])
        self.assertEqual(self.node(l.QUARREL_SCENE, "grain_receipt")["Choices"][0]["Crusade"]["Amount"], -50)
        for sid, nid in ((l.QUARREL_SCENE, "written"), (l.COLD_COUNTS, "letter")):
            for flags, expected in ((set(), 0), ({l.ALLOTMENT_LOST}, 50),
                                    ({l.ALLOTMENT_LOST, l.POWDER_RESTORED}, 0)):
                answers = self.answers(sid, nid, flags)
                self.assertEqual(len(answers), 1)
                self.assertEqual(answers[0].get("Crusade", {}).get("Amount", 0), expected)

    def test_bill_checks_keep_a_real_debt_and_payment_is_separate(self):
        for nid, flag, amount in (("jest_won", l.WINE_OWED, 50), ("jest_lost", l.BILL_OWED, 200)):
            answers = self.node(l.REVELS, nid)["Choices"]
            self.assertIn(flag, answers[0]["Set"])
            self.assertNotIn("Crusade", answers[0])
            self.assertEqual(answers[1]["Crusade"]["Amount"], -amount)
            self.assertIn(l.CELLAR_PAID, answers[1]["Set"])
            self.assertNotIn(t.COMMITTED, answers[1]["Set"])
        self.assertTrue(self.node(l.L + "cellar_settlement", "bill")["Choices"][-1]["Abort"])

    def test_solo_denials_and_poly_denial_follow_real_state(self):
        sid = l.OTHERS
        solo = [a for a in self.answers(sid, "says", {"trickster.ever"}) if a["Next"] in ("lie", "nobody")]
        poly = [a for a in self.answers(sid, "says", {"trickster.ever", l.OTHER_LOVER}) if a["Next"] in ("lie", "nobody")]
        self.assertEqual(len(solo), 1)
        self.assertEqual(len(poly), 1)
        self.assertTrue(poly[0]["Text"].startswith("[Lie]"))
        self.assertEqual({a["Next"] for a in solo}, {"nobody"})
        self.assertEqual({a["Next"] for a in poly}, {"lie"})
        self.assertIn("Admit the lie", self.node(sid, "lie")["Choices"][0]["Text"])
        self.assertNotIn("three entries", self.node(sid, "lie")["Text"])
        self.assertNotIn(["ember.harem.eligible"], self.payload["Derived"][l.OTHER_LOVER])
        self.assertNotIn(["aivu.harem.eligible"], self.payload["Derived"][l.OTHER_LOVER])

    def test_names_are_disclosed_before_terms_and_new_relationship_has_followup(self):
        sid = l.OTHERS
        answers = self.answers(sid, "names.0", {l.L + "undisclosed.nocticula"})
        self.assertEqual([a["Next"] for a in answers], ["named.nocticula"])
        answer = self.node(sid, "named.nocticula")["Choices"][0]
        self.assertFalse(answer["Set"])
        self.assertEqual(self.payload["DerivedOpenRoutes"][l.L + "current_other.nocticula"], ["nocticula"])
        self.assertEqual(self.answers(sid, "names.0", set())[-1]["Next"], "names_done")
        follow = self.scenes[l.L + "changed_columns"]
        self.assertEqual(follow["RequiresAnyGroups"], [[l.L + "sole_line", l.L + "terms_kept"]])
        self.assertIn(l.L + "new_columns", follow["Requires"])
        self.assertIn(t.CLOSED, follow["Forbids"])
        nodes = {n["Id"]: n for n in follow["Nodes"]}
        reached, pending = set(), [follow["Nodes"][0]["Id"]]
        while pending:
            nid = pending.pop()
            if nid in reached:
                continue
            reached.add(nid)
            pending.extend(a["Next"] for a in nodes[nid]["Choices"] if a.get("Next"))
        self.assertEqual(reached, set(nodes))

    def test_disclosure_is_acyclic_and_names_only_each_actual_relationship(self):
        from storylines.household import PARTNERS
        partners = [r for r in PARTNERS if r != "dorgelinda"]
        for actual in ([], ["nocticula"], ["anevia", "galfrey"], partners):
            flags = {l.L + "undisclosed." + r for r in actual if not (r in ("anevia", "irabeth") and "tirabade" in actual)}
            current, visited, named = "names.0", set(), []
            while current != "names_done":
                self.assertNotIn(current, visited)
                visited.add(current)
                if current.startswith("named."):
                    named.append(current[6:])
                choices = self.answers(l.OTHERS, current, flags)
                self.assertEqual(len(choices), 1, (current, actual))
                flags.update(choices[0]["Set"])
                current = choices[0]["Next"]
            self.assertEqual(named, [r for r in partners if r in actual and not (r in ("anevia", "irabeth") and "tirabade" in actual)])
        for rel, native in (("arueshalae", l.L + "native_arueshalae_open"),
                            ("camellia", "camellia.romance"),
                            ("galfrey", "galfrey.romance_active"),
                            ("wenduag", "wenduag.romance_active")):
            key = l.L + "current_other." + rel
            self.assertIn([native], self.payload["Derived"][key])
            self.assertEqual(self.payload["DerivedOpenRoutes"][key], [rel])
        self.assertEqual(self.payload["Etudes"][l.L + "native_arueshalae"],
                         "d6a90c0f6536331498cafa1f3195d886")
        self.assertEqual(self.payload["Derived"][l.L + "native_arueshalae_open"],
                         [[l.L + "native_arueshalae"]])
        self.assertNotIn(l.L + "native_arueshalae_failed", self.payload["Etudes"])

    def test_first_night_slot_and_brief_have_matching_cut(self):
        slot = "dorgelinda.ledger.after_hours.explicit.1"
        old = self.node(l.NIGHT, "threshold")["Choices"][0]
        self.assertEqual(old["Next"], slot)
        self.assertFalse(old["Set"])
        self.assertEqual(self.node(l.NIGHT, slot)["Choices"][0]["Set"], [l.NIGHT_KEPT])
        brief = json.loads((Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/dorgelinda-stranglehold" / (slot + ".json")).read_text(encoding="utf-8"))
        self.assertTrue(self.node(l.NIGHT, slot)["Text"].endswith(brief["last_line"][3:] + "{/n}"))


if __name__ == "__main__":
    unittest.main()

"""S36 deed contracts, current attendance, paid remedies and reader histories."""
import copy
import unittest

from storylines import household_pair_melazmera_hepzamirah as row
from storylines import melazmera_trickster, hepzamirah_trickster
from tools import rrt_verify as rules


def fixture():
    payload = dict(Scenes=[dict(Id=w + ".lastcall.page", Nodes=[dict(Id="page", Paragraphs=[])])
                           for w in row.WOMEN],
        Relationships=dict(melazmera=copy.deepcopy(melazmera_trickster.RELATIONSHIP),
                           hepzamirah=copy.deepcopy(hepzamirah_trickster.RELATIONSHIP),
                           household=dict(StartedFlag="household.started", ClosedFlag="household.closed", CommittedFlag="household.committed")),
        Books={"trickster.ledger": dict(Entries=[])}, RestAllowances={"household.protected": 2})
    row.integrate(payload)
    # The runtime model needs scenes with actual nodes, not the destination stubs.
    modeled = dict(payload, Scenes=[s for s in payload["Scenes"] if s["Id"].startswith(row.P)])
    return payload, rules.Model(modeled)


def state():
    s = rules.SimState(5, 100)
    s.flags.update(row.COMMON)
    s.crusade_resources = {"Finances": 1000}
    return s


def paragraphs_visible(paragraphs, flags):
    return [p for p in paragraphs if set(p["Requires"]) <= flags
            and not set(p["Forbids"]) & flags
            and all(set(group) & flags for group in p["AnyGroups"])]


class S36Tests(unittest.TestCase):
    def setUp(self):
        self.payload, self.model = fixture()
        self.scenes = {s["Id"][len(row.P):]: s for s in self.model.scenes}

    def answer(self, step, node, index=0):
        return next(n for n in self.scenes[step]["Nodes"] if n["Id"] == node)["Choices"][index]

    def take(self, s, step, node, index=0):
        answer = self.answer(step, node, index)
        self.assertTrue(rules.sim_choice_available(answer, s))
        def publish():
            s.flags.update(answer["Set"])
            s.times.update({flag: s.hour for flag in answer["Set"]})
            if answer["Next"] is None and not answer["Abort"]:
                s.flags.add(self.scenes[step]["Id"])
                s.rest_spent["household.protected"] = s.rest_spent.get("household.protected", 0) + 1
        if answer.get("Crusade"):
            self.assertTrue(rules.sim_paid_choice(self.model, self.scenes[step], answer, s, publish))
        elif not answer["Abort"]:
            publish()
        return answer

    def prepare(self, s):
        self.take(s, "open", "start", 0)
        known = row.TRUCE in s.flags
        self.take(s, "open", "prepared", 0 if known else 1)
        self.take(s, "open", "terms.known" if known else "terms.unknown")
        s.hour += 48
        s.rest_spent.clear()

    def test_frozen_contract_and_gate_mutations(self):
        self.assertTrue(row.validate())
        for mutate in (
            lambda s: s[0]["Requires"].remove("foresight.page_taken"),
            lambda s: s[1].__setitem__("DelayHours", 47),
            lambda s: s[2]["Forbids"].append(next(iter(row.ENMITIES))),
            lambda s: s[0]["Nodes"][0]["Choices"][-1]["Set"].append(row.P + "free"),
            lambda s: s[1]["Nodes"][1]["Choices"][0]["Set"].append("hepzamirah.harem.stance.joined"),
            lambda s: s[0].__setitem__("Participants", ["melazmera"]),
        ):
            scenes = copy.deepcopy(row.SCENES)
            mutate(scenes)
            with self.assertRaises(ValueError):
                row.validate(scenes)

    def test_paid_page_live_path_and_body_are_independent_gates(self):
        for missing in row.COMMON:
            s = state()
            s.flags.remove(missing)
            s.flags.update(["trickster.ever", "trickster.foresight.met"])
            self.assertFalse(rules.sim_available(self.model, self.scenes["open"], s), missing)
        for chapter in (3, 4, 6):
            s = state(); s.chapter = chapter
            self.assertFalse(rules.sim_available(self.model, self.scenes["open"], s))
        s = state()
        for w in row.WOMEN:
            s.flags.add(w + ".harem.stance.own_house")
        self.assertTrue(rules.sim_available(self.model, self.scenes["open"], s))

    def test_current_closure_and_absence_at_every_step(self):
        for step in self.scenes:
            s = state(); s.flags.update([row.P + "open.ready", row.P + "diversion.failed"])
            self.assertTrue(rules.sim_available(self.model, self.scenes[step], s))
            for w in row.WOMEN:
                rel = self.payload["Relationships"][w]
                for absent in [rel["ClosedFlag"], *rel["UnavailableFlags"]]:
                    gone = copy.deepcopy(s); gone.flags.add(absent)
                    self.assertFalse(rules.sim_available(self.model, self.scenes[step], gone), (step, absent))
            if step != "open":
                gone = copy.deepcopy(s); gone.flags.remove(row.CONTACT[1])
                self.assertFalse(rules.sim_available(self.model, self.scenes[step], gone))

    def test_success_and_escort_write_acts_not_roll_or_desire(self):
        for terminal, paid in (("held", 0), ("escorted", 300)):
            s = state(); self.prepare(s)
            self.assertTrue(rules.sim_available(self.model, self.scenes["diversion"], s))
            self.take(s, "diversion", "start", 0 if terminal == "held" else 1)
            self.assertNotIn(row.P + "diversion.held", s.flags)
            self.take(s, "diversion", terminal)
            self.assertTrue(set(row.HELD) <= s.flags)
            self.assertEqual(s.crusade_resources["Finances"], 1000 - paid)
            self.assertNotIn(row.P + "replacement.held", s.flags)
            self.assertFalse(rules.sim_available(self.model, self.scenes["replacement"], s))
            self.assertFalse(any(".attitude." in f or ".enmity." in f for f in s.flags))

    def test_failed_trail_single_separate_remedy_saved_clock_and_full_debit(self):
        s = state(); self.prepare(s)
        self.take(s, "diversion", "start")
        self.take(s, "diversion", "lost")
        self.assertNotIn(row.P + "resolved", s.flags)
        saved = copy.deepcopy(s)
        s.hour += 47; s.rest_spent.clear()
        self.assertFalse(rules.sim_available(self.model, self.scenes["replacement"], s))
        s.hour += 1
        for f in row.ENMITIES:
            s.flags.add(f)
        other = "hepzamirah.harem.enmity.delamere"
        s.flags.add(other)
        self.assertTrue(rules.sim_available(self.model, self.scenes["replacement"], s))
        self.take(s, "replacement", "start")
        self.take(s, "replacement", "carried")
        self.assertEqual(s.crusade_resources["Finances"], 600)
        self.assertTrue({row.P + "resolved", row.P + "diversion.failed", row.P + "unsettled", other} <= s.flags)
        self.assertFalse(rules.sim_available(self.model, self.scenes["replacement"], copy.deepcopy(s)))
        self.assertNotIn(row.P + "resolved", saved.flags)
        self.assertEqual(saved.times[row.P + "diversion.failed"], 148)

    def test_payment_cannot_publish_partial_cost_or_witnesses(self):
        for step, terminal, price in (("diversion", "escorted", 300), ("replacement", "carried", 400)):
            for funds in (None, 0, price - 1, price, price + 1):
                s = state(); s.flags.update([row.P + "open.ready", row.P + "diversion.failed"])
                s.crusade_resources = None if funds is None else {"Finances": funds}
                before = copy.deepcopy(s.__dict__)
                answer = self.answer(step, terminal)
                def publish():
                    s.flags.update(answer["Set"])
                    s.flags.add(self.scenes[step]["Id"])
                    s.rest_spent["household.protected"] = 1
                affordable = funds is not None and funds >= price
                self.assertEqual(rules.sim_paid_choice(self.model, self.scenes[step], answer, s, publish), affordable)
                if not affordable:
                    self.assertEqual(s.__dict__, before)
                else:
                    self.assertEqual(s.crusade_resources["Finances"], funds - price)

    def test_refusals_and_aborts_never_close_romances_or_grant_resolution(self):
        for step, index in (("open", 1), ("diversion", 2), ("replacement", 1)):
            s = state(); self.take(s, step, "start", index)
            self.take(s, step, "refused")
            self.assertIn(row.P + "permanent_refusal", s.flags)
            self.assertNotIn(row.P + "resolved", s.flags)
            self.assertFalse(any(w + ".closed" in s.flags for w in row.WOMEN))
        for step in self.scenes:
            s = state(); before = copy.deepcopy(s.__dict__)
            self.take(s, step, "start", len(self.scenes[step]["Nodes"][0]["Choices"]) - 1)
            self.assertEqual(s.__dict__, before)

    def test_optional_native_memory_never_earns_an_outcome(self):
        for known in (False, True):
            s = state()
            if known: s.flags.add(row.TRUCE)
            answer = self.answer("open", "prepared", 0 if known else 1)
            other = self.answer("open", "prepared", 1 if known else 0)
            self.assertTrue(rules.sim_choice_available(answer, s))
            self.assertFalse(rules.sim_choice_available(other, s))
            self.assertEqual(answer["Set"], list(row.TERMINALS["open", "prepared", 0]))
        self.assertEqual(row.SEEN_CUES[row.TRUCE], ["326fe8ba065fb9248992d419dd0d133d"])
        self.assertNotIn("Colyphyr", row.UNKNOWN)

    def test_living_reader_survival_closure_and_all_costs(self):
        for woman in row.WOMEN:
            page = next(s for s in self.payload["Scenes"] if s["Id"] == woman + ".lastcall.page")
            paragraphs = page["Nodes"][0]["Paragraphs"]
            held = {row.P + "resolved", row.P + "cost.commander_watch_kept", woman + ".harem.eligible", woman + ".trickster.returned"}
            for sacrifice, returned, expected in ((False, False, 2), (True, False, 0), (True, True, 2)):
                s = state(); s.flags.update(held)
                if sacrifice: s.flags.add("sacrifice")
                if returned: s.flags.add("trickster.commander_back")
                rules.sim_complete(self.model, s)
                self.assertEqual(len(paragraphs_visible(paragraphs, s.flags)), expected)
                s.flags.add(woman + ".closed"); rules.sim_complete(self.model, s)
                self.assertEqual(paragraphs_visible(paragraphs, s.flags), [])
            for cost in row.COSTS:
                self.assertTrue(any(row.P + "cost." + cost in p["Requires"] for p in paragraphs))
        for entry in row.ledger_entries():
            self.assertFalse(any("reader." in flag or flag == "sacrifice" for flag in entry["Requires"]))
            for cost in row.COSTS:
                self.assertTrue(any(row.P + "cost." + cost in p["Requires"] for p in entry["Lines"]))

    def test_direct_exchange_enmity_but_remedy_does_not_change_existing_target(self):
        s = state(); s.flags.add(next(iter(row.ENMITIES)))
        self.assertFalse(rules.sim_available(self.model, self.scenes["open"], s))
        s.flags.update(row.ENMITIES.values())
        self.assertTrue(rules.sim_available(self.model, self.scenes["open"], s))
        self.assertEqual(row.POLICY_INPUTS["failure"], row.P + "diversion.failed")
        self.assertEqual(row.POLICY_INPUTS["reconciliation"], row.P + "replacement.held")
        self.assertEqual(row.RESPECT_GROUPS, [[row.P + "diversion.held"], [row.P + "replacement.held"]])


if __name__ == "__main__":
    unittest.main()

"""S24's indexed outcomes, current attendance and delayed retry contract."""
import copy
import json
from pathlib import Path
import unittest

from storylines import household
from storylines.harem_rows import s24
from tools import rrt_verify, savecompat


class S24Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads((Path(__file__).resolve().parents[1] / "development/Story.json").read_text(encoding="utf-8-sig"))
        s24.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.model = rrt_verify.Model(cls.payload)
        cls.rows = {s["Id"]: s for s in cls.payload["Scenes"] if s["Id"].startswith(s24.PREFIX)}

    def state(self, branch="good"):
        state = rrt_verify.SimState(5, 1000)
        scene = self.rows[s24.P("settle." + branch)]
        state.flags.update(scene["Requires"])
        # These native/earned inputs justify rather than merely assert adapters.
        state.flags.update(["trickster", "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                            "arueshalae.committed", "vellexia.committed", "vellexia.trickster.unmirrored"])
        state.flags.add("arueshalae.fallen" if branch == "fallen" else "arueshalae.changed")
        state.flags.update(["arueshalae.recruited_drezen"])
        return state

    def available(self, suffix, state):
        return rrt_verify.sim_available(self.model, self.model.by_id[s24.P(suffix)], state)

    def test_personality_precedence_unknown_and_present_path(self):
        state = self.state()
        self.assertTrue(self.available("settle.good", state))
        state.flags.add("arueshalae.corrupted")
        self.assertFalse(self.available("settle.good", state))
        self.assertTrue(self.available("settle.fallen", state))
        state.flags.difference_update(["arueshalae.redeemed", "arueshalae.corrupted"])
        self.assertFalse(self.available("settle.good", state))
        self.assertFalse(self.available("settle.fallen", state))
        for flag in ("trickster", household.PAGE_TAKEN, household.KEPT, household.STANCE_ELIGIBLE,
                     *s24.BODY_REQUIRES):
            state = self.state()
            state.flags.remove(flag)
            self.assertFalse(self.available("settle.good", state), flag)
        for chapter in (3, 4, 6):
            state = self.state()
            state.chapter = chapter
            self.assertFalse(self.available("settle.good", state))

    def test_current_losses_mirror_window_and_directional_enmity(self):
        for suffix in self.rows:
            scene = self.rows[suffix]
            for flag in s24.BODY_FORBIDS:
                self.assertIn(flag, scene["Forbids"])
            for woman in s24.PAIR:
                state = self.state()
                state.flags.add(self.payload["Relationships"][woman]["ClosedFlag"])
                self.assertFalse(self.available("settle.good", state))
            for flag in ("vellexia.trickster.kept_as_mirror", "vellexia.trickster.visited",
                         "engine.l12.commander_unreturned", "trickster.failed"):
                state = self.state()
                state.flags.add(flag)
                self.assertFalse(self.available("settle.good", state))
        for a, b in (s24.PAIR, s24.PAIR[::-1]):
            state = self.state()
            state.flags.add(household.enmity(a, b))
            self.assertFalse(self.available("settle.good", state))
            state.flags.add(a + ".harem.reconciled." + b)
            self.assertTrue(self.available("settle.good", state))
        for woman in s24.PAIR:
            state = self.state()
            state.flags.add(woman + ".trickster.returned")
            state.flags.update(self.payload["Relationships"][woman].get("EpochUnavailableFlags", []))
            self.assertFalse(self.available("settle.good", state), woman)

    def test_fixed_indices_terminal_witnesses_and_no_extra_mechanics(self):
        for sid, scene in self.rows.items():
            step = "retry" if ".retry." in sid else "settle"
            fallen = sid.endswith("fallen")
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            root = nodes["start"]["Choices"]
            self.assertEqual(len(root), 4)
            self.assertTrue(root[3]["Abort"])
            self.assertFalse(root[3]["Set"])
            for choice in root:
                self.assertFalse(choice["Set"])
            if step == "settle":
                self.assertEqual(root[0]["Check"], dict(Skill="SkillAthletics", DC=20,
                                                      Success="bounded", Failure="botched", CommanderOnly=True))
                self.assertEqual(nodes["bounded"]["Choices"][0]["Set"], list(s24._success(step, fallen)))
            self.assertEqual(nodes["refereed"]["Choices"][0]["Set"], list(s24._success(step, fallen)))
            failure = nodes["failed" if step == "retry" else "botched"]["Choices"][0]
            self.assertEqual(failure["Set"], [s24.P(step + ".seen"), s24.P(step + ".failed"), s24.P("bout.interrupted")])
            self.assertEqual(nodes["declined"]["Choices"][0]["Set"], [s24.P(step + ".seen"), s24.P(step + ".declined")])
            self.assertEqual(scene["RestAllowance"], "household.protected")
            self.assertNotIn("HouseholdArcStart", scene)
            self.assertNotIn("Remote", scene)
            for node in scene["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                self.assertTrue(node["Choices"])
                for choice in node["Choices"]:
                    for flag in choice["Set"]:
                        self.assertTrue(flag.startswith(s24.PREFIX))
                        self.assertNotIn(".harem.attitude.", flag)
                        self.assertNotIn(".enmity.", flag)
                        self.assertNotIn(".committed", flag)

    def test_retry_requires_timestamp_and_never_reopens_success_or_refusal(self):
        state = self.state()
        self.assertFalse(self.available("retry.good", state))
        state.flags.add(s24.P("settle.failed"))
        state.times[s24.P("settle.failed")] = state.hour
        self.assertFalse(self.available("retry.good", state))
        state.hour += 48
        self.assertTrue(self.available("retry.good", state))
        for suffix in ("settle.kept", "settle.declined", "retry.seen"):
            blocked = copy.deepcopy(state)
            blocked.flags.add(s24.P(suffix))
            self.assertFalse(self.available("retry.good", blocked))
        state.flags.remove("vellexia.present_now")
        self.assertFalse(self.available("retry.good", state))

    def test_registration_is_repeatable_save_safe_and_ledger_is_historical(self):
        before = copy.deepcopy(self.payload)
        entries = list(household.ENTRIES)
        consumers = dict(household.CONSUMERS)
        s24.register(self.payload, [], {})
        self.assertEqual(self.payload, before)
        self.assertEqual(household.ENTRIES, entries)
        self.assertEqual(household.CONSUMERS, consumers)
        self.assertEqual(savecompat.check(self.payload), [])
        ledger = next(e for e in self.payload["Books"]["trickster.ledger"]["Entries"]
                      if e["Id"] == "seating.arueshalae.vellexia")
        self.assertNotIn("vellexia.present_now", ledger["Requires"])
        pending = next(line for line in ledger["Lines"] if "interrupted" in line["Text"])
        self.assertEqual(pending["Forbids"], [s24.P("retry.seen")])

    def test_respect_requires_every_deed_and_has_no_higher_rung(self):
        for a, b in (s24.PAIR, s24.PAIR[::-1]):
            stage = a + ".harem.attitude." + b + "."
            self.assertEqual(self.payload["Derived"][stage + "respect"],
                             [[s24.P(w) for w in s24.RESPECT_WITNESSES]])
            self.assertEqual(self.payload["DerivedForbids"][stage + "rival"], [stage + "respect"])
            self.assertNotIn(stage + "friend", self.payload["Derived"])
            self.assertNotIn(stage + "lover", self.payload["Derived"])

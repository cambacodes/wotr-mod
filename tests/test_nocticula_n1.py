"""N1 save migration: append-only fallbacks and the real authored flag graph."""
from copy import deepcopy
import unittest

from storylines import nocticula_continuation as route, nocticula_acquired_harbor as clones
from storylines import nocticula_partners as partners, nocticula_trickster, nocticula_trickster_concession
from storylines.nocticula_n1 import RETIRED, REWIRES, NEW_FLAGS
from storylines.nocticula_trickster_acquisition import allowed
from tools import savecompat


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class NocticulaN1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = {"Scenes": deepcopy(route.SCENES + clones.SCENES + nocticula_trickster.SCENES
                                     + nocticula_trickster_concession.SCENES)}
        partners.integrate(payload)
        cls.scenes = {s["Id"]: s for s in payload["Scenes"]}

    def choices(self, sid, node):
        return next(n["Choices"] for n in self.scenes["noct." + sid]["Nodes"] if n["Id"] == node)

    def test_eight_retirements_and_frozen_clone_ids_choices_and_text(self):
        for key in RETIRED:
            scene = self.scenes["noct." + key]
            self.assertIn("noct.retired", scene["Requires"])
            self.assertFalse(allowed(scene, set(scene["Requires"]) - {"noct.retired"}))
            self.assertEqual(scene["Kind"], "memory")
        for old in clones.BASELINE["IntegratedScenes"]:
            new = self.scenes[old["Id"]]
            self.assertEqual([], savecompat.check({"Scenes": [new]}, savecompat.inventory({"Scenes": [old]})))
            self.assertEqual([[{k: v for k, v in c.items() if k != "Text"} for c in n["Choices"]]
                              for n in old["Nodes"]],
                             [[{k: v for k, v in c.items() if k != "Text"} for c in n["Choices"]]
                              for n in new["Nodes"]])
            if not new["Owner"].endswith("Epilogue"):
                self.assertIn("chapter_later", new["Forbids"])

    def test_seven_rewires_and_parked_save_fallbacks(self):
        for key, (old, new) in REWIRES.items():
            scene = self.scenes["noct." + key]
            self.assertIn("noct." + new, scene["Requires"])
            self.assertNotIn("noct." + old, scene["Requires"])
        for sid, node, index, state, target in (
            ("captains_reply", "start", 4, {"noct.witness_heard"}, "ledger"),
            ("demonstration", "start", 4, set(), "release"),
            ("return_count", "start", 4, set(), "carrier"),
            ("return_count", "strain", 3, set(), "reinforced"),
            ("uninvited_guest", "start", 4, set(), "guest"),
            ("bell_without_master", "start", 3, set(), "bounded"),
            ("no_applause", "debt_report", 2, set(), "debt_refused"),
        ):
            with self.subTest(scene=sid, node=node):
                a = only(c for c in self.choices(sid, node)
                         if c["Next"] == target and allowed(c, state)
                         and (bool(c["Set"]) or target == "carrier"))
                self.assertTrue(allowed(a, state))
                self.assertEqual(a["Next"], target)
                if target == "carrier":
                    self.assertTrue(all(c["Set"] for c in self.choices(sid, "carrier")))
                else:
                    self.assertTrue(a["Set"])
                    # A fallback cannot overwrite a played decision.
                    self.assertFalse(allowed(a, state | set(a["Set"])))

    def test_wager_all_four_predictions_and_resource_twins(self):
        wager, credit = self.choices("no_applause", "wager"), self.choices("no_applause", "credit")
        self.assertEqual([(a["Requires"], a["Set"], a["Next"]) for a in wager], [
            (["noct.lodge_debt_purchased"], ["noct.wager_won"], "run.caught"),
            (["noct.lodge_debt_denied"], ["noct.wager_lost"], "run.free"),
            (["noct.lodge_debt_denied"], ["noct.wager_won"], "run.free"),
            (["noct.lodge_debt_purchased"], ["noct.wager_lost"], "run.caught")])
        for debt, result in (("purchased", "won"), ("denied", "lost"),
                             ("denied", "won"), ("purchased", "lost")):
            state = {"noct.lodge_debt_" + debt}
            answer = only(a for a in wager if a["Set"] == ["noct.wager_" + result] and allowed(a, state))
            state.update(answer["Set"])
            offered = [a for a in credit if allowed(a, state)]
            self.assertEqual([a["Set"] for a in offered],
                             [["noct.lodge_desire_contested"], ["noct.lodge_danger_desired"]])
            self.assertEqual([a.get("Crusade") for a in offered],
                             [{"Resource": "Finances", "Amount": 200}] * 2 if result == "won" else [None, None])
        self.assertEqual([a.get("Crusade") for a in credit if allowed(a, set())], [None, None])

    def test_all_new_flags_have_producers_except_never_set_and_native(self):
        produced = {f for s in self.scenes.values() for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]}
        self.assertNotIn("noct.retired", produced)
        self.assertNotIn("noct.native_trials_seen", produced)
        self.assertTrue(set(NEW_FLAGS) - {"noct.retired", "noct.native_trials_seen"} <= produced)
        self.assertEqual(route.SEEN_CUES["noct.native_trials_seen"], ["a5472a3492d23c542b5f77cb6e591ca3"])
        bindings = {}
        route.integrate(bindings)
        self.assertIn("noct.retired", bindings["PendingHooks"])
        self.assertNotIn("noct.retired", bindings.get("Derived", {}))

    def test_mark_after_night_only_and_open_mark_forces_discovery(self):
        self.assertEqual(only(self.choices("her_own_face", "talk"))["Next"], "morning")
        self.assertEqual(only(self.choices("her_own_face", "noct.her_own_face.aftermath.1"))["Next"], "mark")
        end = self.choices("second_door", "end")
        state = {partners.P + "secret", partners.CAREFUL}
        quiet = only(a for a in end if a.get("Next") == "partner_discovery.end.0.hidden" and allowed(a, state))
        exposed = only(a for a in end if a.get("Next") == "partner_discovery.end.0" and "noct.mark_shown" in a["Requires"])
        self.assertFalse(allowed(exposed, state))
        state.add("noct.mark_shown")
        self.assertFalse(allowed(quiet, state))
        self.assertTrue(allowed(exposed, state))

    def test_receipts_require_their_own_deeds(self):
        receipts = partners.harbor_receipts()
        self.assertTrue(any(p["Forbids"] == ["noct.lodge_given_rhez"] for p in receipts))
        for receipt in (p for p in receipts if p["Requires"]):
            self.assertFalse(allowed(receipt, set()))
            self.assertTrue(allowed(receipt, set(receipt["Requires"])))

    def test_waking_priority_presence_and_no_conditional_live_paragraphs(self):
        for sid in ("captains_reply", "her_own_face", "hearing", "uninvited_guest", "second_door"):
            choices = self.choices(sid, "waking")
            all_party = {f for a in choices for f in a["Requires"]} | {"noct.mark_shown"}
            self.assertEqual([a["Next"] for a in choices if allowed(a, all_party)], ["waking." + {"captains_reply": "lann", "her_own_face": "daeran", "hearing": "regill", "uninvited_guest": "wenduag", "second_door": "arueshalae"}[sid], None])
            self.assertEqual([a["Next"] for a in choices if allowed(a, set())], [None])
        for s in self.scenes.values():
            if not s["Owner"].endswith("Epilogue"):
                self.assertFalse(any(n.get("Paragraphs") for n in s["Nodes"]), s["Id"])

    def test_fold_bypasses_retained_letter_but_keeps_parked_nodes(self):
        from tests.story_fixture import fresh_story
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        retired = scenes["noct.acq.the_retained_copy"]
        self.assertIn("noct.retired", retired["Requires"])
        paid = scenes["noct.acq.the_paid_address"]
        copies = [n for n in paid["Nodes"] if n["Id"].startswith("the_retained_copy.")]
        self.assertTrue(copies)
        self.assertTrue(all(n["Choices"] for n in copies))
        bridges = [a for n in paid["Nodes"] if not n["Id"].startswith("the_retained_copy.")
                   for a in n["Choices"] if a["Next"] == "an_answer_of_her_own.arrives"]
        self.assertTrue(bridges)
        self.assertTrue(all("noct.acq.the_retained_copy_done" in a["Set"] for a in bridges))
        archives = [a for n in paid["Nodes"] for a in n["Choices"] if a["Next"] == "the_retained_copy.arrives"]
        self.assertTrue(archives)
        self.assertTrue(all("noct.retired" in a["Requires"] for a in archives))


if __name__ == "__main__":
    unittest.main()

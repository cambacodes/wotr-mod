"""Quick route-only walks: custody, refusal receipts and interrupted payments."""
import copy
import importlib
from pathlib import Path
import unittest

from storylines import seelah, seelah_trickster, seelah_round2 as r
from tools.savecompat import choice_identities


def route_story():
    names = ("seelah", "seelah_later", "seelah_fate", "seelah_abyss", "seelah_aftermath",
             "seelah_late_campaign", "seelah_return", "seelah_progression", "seelah_trickster")
    story = {"Scenes": [], "Relationships": {"seelah": copy.deepcopy(seelah.RELATIONSHIP)}}
    for name in names:
        story["Scenes"].extend(copy.deepcopy(importlib.import_module("storylines." + name).SCENES))
    seelah_trickster.integrate(story)
    # These walks have an observed living actor. Production builds additionally
    # install the shared epoch contract; its registry is a coordinator escalation.
    story["Derived"]["seelah.present_now"] = [["availability.observed"]]
    return story


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class Walk:
    def __init__(self, story, flags=(), favors=0, finances=0):
        self.story = story
        self.flags = set(flags) | {"availability.observed"}
        self.resources = {"Favors": favors, "Finances": finances}

    def has(self, key, stack=()):
        if key in stack:
            return False
        groups = self.story.get("Derived", {}).get(key)
        yes = key in self.flags if groups is None else any(
            all(self.has(k, stack + (key,)) for k in group) for group in groups)
        return yes and not any(self.has(k, stack + (key,)) for k in
                              self.story.get("DerivedForbids", {}).get(key, []))

    def available(self, target):
        return all(self.has(k) for k in target.get("Requires", [])) and all(
            not self.has(k) or self.has(target.get("ForbidOverrides", {}).get(k, ""))
            for k in target.get("Forbids", []))

    def take(self, s, nid, index):
        node = r.node(s, nid)
        answer = next(a for a, ref in zip(node["Choices"], choice_identities(s, node))
                      if ref["GuidFor"] == f"answer.{s['Id']}.{nid}.{index}")
        if not self.available(answer):
            raise AssertionError((s["Id"], nid, index, "not selectable"))
        debit = answer.get("Crusade")
        if debit and self.resources.get(debit["Resource"], 0) + debit["Amount"] < 0:
            return False  # the production exporter supplies the no-payment exit
        if debit:
            self.resources[debit["Resource"]] += debit["Amount"]
        if answer.get("RemoveItem"):
            self.flags.discard("seelah.diamond_held")
        self.flags.update(answer["Set"])
        return answer.get("Next")


class SeelahRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = route_story()
        cls.by = {s["Id"]: s for s in cls.story["Scenes"]}

    def test_kept_list_blocks_both_ordinary_commitments_until_reclamation(self):
        w = Walk(self.story, (r.HOLDS, r.KEEPS))
        self.assertFalse(w.has(r.CUSTODY))
        for sid in ("seelah.door", "seelah.road", "seelah.late_afterglow", r.PREFIX + "epilogue.commit"):
            self.assertIn(r.CUSTODY, self.by[sid]["Requires"])
        reclaim = self.by[r.PREFIX + "dead.list_reclaimed"]
        self.assertIn(r.PREFIX + "woke", reclaim["Requires"])
        self.assertIn(r.KEEPS, reclaim["Requires"])
        self.assertEqual("offer_first", w.take(reclaim, "start", 3))
        self.assertTrue(w.has(r.CUSTODY))
        self.assertIn(r.ROBBED, w.flags)
        self.assertNotIn("seelah.committed", w.flags)
        w.take(reclaim, "offer_first", 1)
        self.assertNotIn(r.GAME, w.flags)
        # Ordinary and immediately-returned histories owe no new custody test.
        self.assertTrue(Walk(self.story).has(r.CUSTODY))
        self.assertTrue(Walk(self.story, (r.HOLDS, r.GIVEN)).has(r.CUSTODY))

    def test_list_return_leaves_refusal_and_neutral_exit_in_both_twins(self):
        for suffix in ("commit", "commit_visit"):
            s = self.by[r.PREFIX + "dismissed." + suffix]
            w = Walk(self.story, (r.HOLDS, "seelah.kissed"))
            self.assertEqual("list_back", w.take(s, "answer", 6))
            self.assertTrue(w.has(r.CUSTODY))
            self.assertTrue(w.available(next(a for a in r.node(s, "list_back")["Choices"] if a["Abort"])))
            self.assertEqual("no_stones", w.take(s, "list_back", 2))
            w.take(s, "no_stones", 0)
            self.assertIn(r.COIN_NO, w.flags)
            self.assertNotIn("seelah.committed", w.flags)

    def test_time_does_not_pay_first_coin(self):
        flags = ("trickster.ever", r.PREFIX + "returned", r.PREFIX + "declined",
                 r.COIN_NO, r.HOLDS, r.GIVEN, "seelah.kissed")
        w = Walk(self.story, flags)
        ask = self.by[r.PREFIX + "dismissed.second_ask"]
        self.assertFalse(w.available(ask))
        paid = self.by[r.PREFIX + "dismissed.second_ask_paid"]
        self.assertTrue(w.available(paid))
        w.take(paid, "start", 0)
        self.assertIn(r.COIN_PAID, w.flags)
        self.assertNotIn("seelah.committed", w.flags)
        self.assertTrue(w.available(ask))
        self.assertFalse(w.available(next(a for a in r.node(ask, "price")["Choices"] if a["Next"] == "robbed")))
        w.take(ask, "coin_answer", 0)
        self.assertTrue(w.available(next(a for a in r.node(ask, "price")["Choices"] if a["Next"] == "robbed")))

    def test_papers_refusal_gets_a_free_return_not_a_coin_receipt(self):
        w = Walk(self.story, (r.FREEDOM_NO,))
        ask = self.by[r.PREFIX + "dismissed.second_ask"]
        self.assertFalse(w.available(next(a for a in r.node(ask, "price")["Choices"] if a["Next"] == "robbed")))
        w.take(ask, "free_return", 0)
        self.assertTrue(w.available(next(a for a in r.node(ask, "price")["Choices"] if a["Next"] == "closed")))
        self.assertNotIn(r.COIN_PAID, w.flags)

    def test_abort_after_seller_arrest_resumes_without_second_charge(self):
        for suffix in ("pickpocket", "pickpocket_effects"):
            s = self.by[r.PREFIX + "dead." + suffix]
            w = Walk(self.story, favors=50)
            # Untaught failed lift: conceal/arrest/buy-off indices remain stable.
            w.take(s, "grabbed", 2 if suffix.endswith("effects") else 1)
            self.assertEqual(0, w.resources["Favors"])
            w.take(s, "taken", 1 if suffix.endswith("effects") else 0)
            terminal = "rider_word" if suffix.endswith("effects") else "pocketed"
            debit_index = 0 if suffix.endswith("effects") else 1
            self.assertFalse(w.take(s, terminal, debit_index))
            self.assertNotIn(r.PREFIX + "cost.chaplains_word", w.flags)
            w.flags.add("seelah.diamond_held")
            entry = "start" if suffix.endswith("effects") else "bier"
            choices = r.node(s, entry)["Choices"]
            selectable = [ref["GuidFor"].removeprefix(f"answer.{s['Id']}.{entry}.")
                          for a, ref in zip(choices, choice_identities(s, r.node(s, entry))) if w.available(a)]
            self.assertEqual([a["Next"] for a in choices if w.available(a)], ["payment_resume"])
            self.assertEqual("payment_resume", w.take(s, entry, only(selectable)))
            w.take(s, "payment_resume", 0)
            w.take(s, "rider" if suffix.endswith("effects") else "pocketed", 0)
            self.assertEqual(0, w.resources["Favors"])
            self.assertNotIn("seelah.diamond_held", w.flags)

    def test_presence_is_wanted_after_commitment_and_retained_body_is_excluded(self):
        presence = self.story["Presences"]["seelah.presence"]
        w = Walk(self.story, ("trickster.ever", r.PREFIX + "in_drezen", "seelah.committed"))
        self.assertTrue(w.available(presence))
        w.flags.add("seelah.revived")
        self.assertFalse(w.available(presence))
        # Contacts are obtained from wanted presence, never independently seeded.
        w.flags.discard("seelah.revived")
        contacts = {presence["Unit"]} if w.available(presence) else set()
        self.assertIn(self.by[r.PREFIX + "dead_no_unit.seller_word"]["ContactUnit"], contacts)

    def test_living_courier_can_deliver_before_seelah_arrives(self):
        for suffix in ("reply", "arrival"):
            s = self.by[r.PREFIX + "dead.effects_" + suffix]
            self.assertEqual([r.FYE_HUB], s["AnswerLists"])
            self.assertEqual(r.FYE, s["ContactUnit"])
            self.assertNotIn("InteractionHub", s)
            self.assertNotIn("seelah.present_now", s["Requires"])
            self.assertFalse(s.get("Remote", False))
        self.assertFalse(any("courier" in name for name in self.story["Presences"]))

    def test_slots_are_complete_and_quiet_choices_do_not_enter_them(self):
        root = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/seelah"
        for path in root.glob("*.json"):
            slot_id = path.stem
            s = self.by[slot_id.rsplit(".explicit.", 1)[0]]
            blocks = s["Nodes"] + [p for n in s["Nodes"] for p in n.get("Paragraphs", [])]
            slots = [b for b in blocks if b.get("Id") == slot_id]
            slot = only(slots)
            self.assertEqual(slot["Id"], slot_id)
            for answer in slot.get("Choices", []):
                self.assertEqual([], answer["Set"], slot_id)
                self.assertFalse(answer["Abort"], slot_id)
        door = self.by["seelah.door"]
        self.assertEqual([a["Next"] for a in r.node(door, "honest")["Choices"]],
                         ["kiss", "seelah.door.explicit.1.approach", "quiet", "different"])
        for s in self.by.values():
            ids = {n["Id"] for n in s["Nodes"]}
            for n in s["Nodes"]:
                for a in n["Choices"]:
                    if a.get("Next"):
                        self.assertIn(a["Next"], ids, (s["Id"], n["Id"]))


if __name__ == "__main__":
    unittest.main()

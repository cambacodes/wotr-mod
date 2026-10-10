"""Receipts and alternative histories for the Nocticula round-2 situations."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools.savecompat import choice_identities, EXIT_MECHANICS
from storylines import nocticula_partners as partners
from storylines.nocticula_trickster import PAID, REFUSED, SAID_YES, LATE, ALIVE_AFTER


def allowed(item, flags):
    blocked = {f for f in item.get("Forbids", ())
               if item.get("ForbidOverrides", {}).get(f) not in flags}
    return (set(item.get("Requires", ())) <= flags
            and not blocked & flags
            and all(set(g) & flags for g in item.get("AnyGroups", ()))
            and all(set(g) & flags for g in item.get("RequiresAnyGroups", ())))


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class NocticulaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def nodes(self, sid):
        return {n["Id"]: n for n in self.scenes[sid]["Nodes"]}

    def test_yes_is_the_only_shadow_commit_receipt_including_partner_resumes(self):
        sid = "nocticula.trickster.defeated.chair"
        nodes = self.nodes(sid)
        for n in nodes.values():
            for c in n["Choices"]:
                if {SAID_YES, "noct.complete"} & set(c["Set"]):
                    self.assertEqual(n["Id"], "yes")
                    self.assertEqual(c["Set"], ["noct.complete", SAID_YES])
        # Exercise true/joke, paid/refused, and all current partner conditions.
        for paid in (False, True):
            for state, req, bad in partners.STATES:
                for opening in ("verdict_true", "verdict_joke"):
                    with self.subTest(paid=paid, partner=state, opening=opening):
                        flags = set(req) | set(self.scenes[sid]["Requires"]) | {
                            "trickster.now", PAID if paid else REFUSED}
                        pending = [(opening, frozenset(flags))]
                        seen, yes, committed = set(), False, False
                        while pending:
                            key, current = pending.pop()
                            if (key, current) in seen:
                                continue
                            seen.add((key, current))
                            choices = [c for c in nodes[key]["Choices"] if allowed(c, current)]
                            self.assertTrue(choices, (key, current))
                            if key == "yes":
                                yes = True
                                self.assertNotIn(SAID_YES, current)
                            for c in choices:
                                after = current | set(c["Set"])
                                if SAID_YES in after:
                                    committed = True
                                    self.assertIn(partners.TERMS, after)
                                if c["Next"]:
                                    pending.append((c["Next"], frozenset(after)))
                        self.assertTrue(yes and committed)

    def test_chair_and_sacrifice_each_require_their_real_receipt(self):
        ending = self.nodes("nocticula.trickster.defeated.epilogue")["end"]
        seat = next(p for p in ending["Paragraphs"] if set(p["Requires"]) == {SAID_YES, PAID})
        self.assertFalse(allowed(seat, {SAID_YES, REFUSED}))
        self.assertTrue(allowed(seat, {SAID_YES, PAID}))
        loss = self.scenes["nocticula.trickster.defeated.epilogue.unanswered"]
        self.assertIn(ALIVE_AFTER, loss["Forbids"])
        n = loss["Nodes"][0]
        for p in n["Paragraphs"]:
            if PAID in p["Requires"]:
                self.assertEqual(p["Requires"], [PAID])
            if SAID_YES in p["Requires"]:
                self.assertEqual(p["Requires"], [SAID_YES])

    def test_paid_refusal_and_inn_collect_without_changing_legacy_exits(self):
        sid = "nocticula.trickster.epilogue.commit"
        for key in ("refused_page", "inn"):
            n = self.nodes(sid)[key]
            old = only(n["Choices"])
            self.assertFalse(any(old.get(k) for k in EXIT_MECHANICS))
            self.assertEqual(only(choice_identities(self.scenes[sid], n))["GuidFor"],
                             "answer." + sid + "." + key + ".continue")
            collections = [p for p in n["Paragraphs"] if p.get("Requires") == [PAID]]
            self.assertTrue(collections)
            for collection in collections:
                self.assertTrue(allowed(collection, {PAID}))
                self.assertFalse(allowed(collection, {REFUSED}))

    def test_daeran_is_not_invented_by_absence_of_loss_flags(self):
        choices = self.nodes("nocticula.trickster.defeated.morning")["start"]["Choices"]
        never_recruited = {PAID}
        self.assertEqual([c["Next"] for c in choices if allowed(c, never_recruited)], ["note_paid_alone"])
        self.assertEqual([c["Next"] for c in choices if allowed(c, {PAID, "nocticula.daeran_present"})], ["note_paid"])
        for loss in ("daeran.dead", "daeran.kicked_out"):
            self.assertFalse(any(c["Next"] == "note_paid" and allowed(c, {PAID, loss}) for c in choices))
        self.assertEqual(self.story["Etudes"]["nocticula.daeran_in_party"], "e49732bbb3126ec4280cf7f12946abad")

    def test_terms_precede_harbor_approaches_and_copies_stay_retired(self):
        for sid, key, target in (("noct.unlit_quay", "offer", "later"),
                                 ("noct.her_own_face", "start", "face"),
                                 ("noct.her_own_face", "start", "invention"),
                                 ("noct.another_place", "start", "dance"),
                                 ("noct.what_she_keeps", "ambition", "power")):
            n = self.nodes(sid)[key]
            self.assertIn(partners.TERMS, next(c for c in n["Choices"] if c["Next"] == target)["Requires"])
            self.assertTrue(any((c["Next"] or "").startswith("partner_terms.") and partners.TERMS in c["Forbids"]
                                for c in n["Choices"]))
        for s in self.story["Scenes"]:
            if s["Id"].startswith("noct.join.") or ".acquired." in s["Id"] and not s["Owner"].endswith("Epilogue"):
                self.assertIn("chapter_later", s["Forbids"])

    def test_acquisition_visit_is_optional_read_only_and_channel_limited(self):
        sid = "noct.acq.epilogue.correspondence"
        nodes = self.nodes(sid)
        page = nodes["page"]
        self.assertFalse(any(next(c for c in page["Choices"] if c.get("Id") == "continue").get(k) for k in EXIT_MECHANICS))
        self.assertEqual(next(ref for ref in choice_identities(self.scenes[sid], page) if ref["Id"] == "continue")["GuidFor"], "answer." + sid + ".page.continue")
        from tests.fix16b_structure import reachable_nodes
        reached = reachable_nodes(self.scenes[sid])
        self.assertTrue({"page", "invitation", "letters", "arrival", "admitted", "conversation"} <= reached)
        self.assertEqual([None, "invitation"], [c["Next"] for c in page["Choices"]])
        self.assertEqual(["admitted", "letters"], [c["Next"] for c in nodes["arrival"]["Choices"]])
        self.assertTrue(any(c["Next"] == "letters" for c in nodes["invitation"]["Choices"]))
        self.assertTrue(any(c["Next"] == "conversation" for c in nodes["admitted"]["Choices"]))
        for n in nodes.values():
            self.assertTrue(all(not c["Set"] for c in n["Choices"]))
        coda = self.scenes["nocticula.acquisition.lastcall.page"]
        self.assertIn("noct.acq.renewed_agreement", coda["Requires"])
        self.assertNotIn("noct.complete", coda["Requires"])
        for blocker in ("noct.closed", "noct.acq.closed", "noct.dead", "sacrifice"):
            self.assertIn(blocker, coda["Forbids"])
        self.assertEqual(coda["ForbidOverrides"], {"sacrifice": ALIVE_AFTER})
        earned = set(coda["Requires"])
        for group in coda.get("RequiresAnyGroups", ()):
            earned.add(group[0])
        self.assertNotIn("noct.complete", earned)
        self.assertTrue(allowed(coda, earned))
        self.assertFalse(allowed(coda, earned - {"noct.acq.renewed_agreement"}))
        for blocker in ("noct.complete", "noct.closed", "noct.acq.closed", "noct.dead", "sacrifice"):
            with self.subTest(blocker=blocker):
                self.assertFalse(allowed(coda, earned | {blocker}))
        self.assertTrue(allowed(coda, earned | {"sacrifice", ALIVE_AFTER}))

    def test_each_manifest_slot_is_a_dedicated_heated_cut(self):
        root = Path(__file__).resolve().parents[1]
        for brief in (root / "tools/route_packs/explicit_slots/nocticula").glob("*.json"):
            key = brief.stem
            sid = key.rsplit(".explicit.", 1)[0]
            if sid not in self.scenes:
                continue  # copy-host briefs are verified in the same pass when present
            data = json.loads(brief.read_text(encoding="utf-8"))
            fill = self.nodes(sid)[key]
            self.assertEqual(fill["Id"], key)
            self.assertFalse(any(c["Set"] for c in fill["Choices"]))
            self.assertTrue(any(c["Next"] == key for n in self.scenes[sid]["Nodes"] for c in n["Choices"]))


if __name__ == "__main__":
    unittest.main()

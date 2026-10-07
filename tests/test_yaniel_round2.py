"""Route-local histories for the round-two situations and their receipts."""
import copy
import json
import unittest
from pathlib import Path

from storylines import yaniel_walls as walls
from storylines import yaniel_trickster as yt


class YanielRoundTwoTests(unittest.TestCase):
    def setUp(self):
        self.scenes = {s["Id"]: copy.deepcopy(s) for s in walls.SCENES}

    def node(self, scene, node):
        return next(n for n in self.scenes[yt.Y + scene]["Nodes"] if n["Id"] == node)

    def selected(self, choices, flags):
        # The selectors tested here use only route-local OR aliases and party item reads.
        def has(key):
            if key in flags:
                return True
            return any(all(has(k) for k in group) for group in yt.DERIVED.get(key, []))
        return [c for c in choices if all(has(k) for k in c["Requires"])
                and not any(has(k) for k in c["Forbids"])
                and (not c.get("AnyGroups") or any(all(has(k) for k in group)
                                                  for group in c["AnyGroups"]))]

    def test_raid_uses_actual_party_sword_form(self):
        # Apply the existing party-only integration to the two legacy selectors.
        choices = self.node("beat.raid", "start")["Choices"]
        for choice in choices[2:4]:
            for field in ("Requires", "Forbids"):
                choice[field] = [yt.PARTY if k == yt.HELD else k for k in choice[field]]
        for form in ("masterwork", "plus1", "plus2", "ha4", "ha6"):
            with self.subTest(form=form):
                flags = {yt.PARTY, "yaniel.radiance_party." + form}
                got = self.selected(choices, flags)
                self.assertEqual(len(got), 1)
                self.assertEqual(got[0]["Next"], "judges" if form in ("ha4", "ha6") else "judges_plain")
        # A holy sword in the stash cannot illuminate a plain sword in the party.
        got = self.selected(choices, {yt.PARTY, "yaniel.radiance_party.plus1", yt.HA4})
        self.assertEqual([c["Next"] for c in got], ["judges_plain"])
        self.assertEqual([c["Next"] for c in self.selected(choices, {yt.HA4})], ["judges_empty"])

    def test_sparring_methods_have_real_results_and_do_not_earn_trust(self):
        choices = self.node("beat.bout", "fight")["Choices"]
        self.assertEqual([c["Next"] for c in choices[:3]], ["fair", "dirty", "yield"])
        for choice, skill in zip(choices[3:], ("SkillMobility", "CheckBluff")):
            self.assertEqual(choice["Check"]["Skill"], skill)
            self.assertEqual(choice["Check"]["DC"], 25)
            for result in ("Success", "Failure"):
                self.assertEqual(self.node("beat.bout", choice["Check"][result])["Choices"][0]["Next"], "end")
        self.assertEqual(self.node("beat.bout", "end")["Choices"][0]["Set"], [yt.B_BOUT])
        for node in self.scenes[yt.Y + "beat.bout"]["Nodes"]:
            for choice in node["Choices"]:
                self.assertNotIn(yt.TRUSTED, choice["Set"])

    def test_prior_raid_kiss_is_optional_and_recalled_only_when_earned(self):
        choices = self.node("commit.trade", "yes")["Choices"]
        self.assertEqual([c["Next"] for c in self.selected(choices, {yt.Y + "raid_kiss"})], ["yes_raid"])
        self.assertEqual([c["Next"] for c in self.selected(choices, {yt.DRAWN_WALLS})], ["yes2"])
        self.assertEqual(self.node("commit.trade", "ask")["Choices"][0]["Set"], [yt.COMMITTED, yt.SHACKLE])
        self.assertLess(self.node("commit.trade", "yes")["Text"].index("kiss"),
                        self.node("commit.trade", "yes")["Text"].index("what I wanted"))

    def test_trade_distinguishes_report_from_belief_and_pending_oath(self):
        choices = self.node("commit.trade", "room")["Choices"]
        for choice in choices[1:3]:
            for field in ("Requires", "Forbids"):
                choice[field] = [yt.PARTY if k == yt.HELD else k for k in choice[field]]
        for flags, target in (({yt.CARRIES}, "carries"),
                              ({yt.OATH_STANDS, yt.PARTY}, "judges"),
                              ({yt.OATH_STANDS}, "judges_empty"),
                              ({yt.OATH_STANDS, yt.SANG, yt.PARTY}, "judges_report"),
                              ({yt.OATH_STANDS, yt.SANG}, "judges_empty_report"),
                              ({yt.OATH_PENDING, yt.PARTY}, "judges_open")):
            self.assertEqual([c["Next"] for c in self.selected(choices, flags)], [target])

    def test_slot_cut_and_cuff_position_include_vigil_regift(self):
        slot_id = yt.Y + "visit.niche.explicit.1"
        self.assertEqual(self.node("visit.niche", "threshold2")["Choices"][0]["Next"], slot_id)
        slot = self.node("visit.niche", slot_id)
        brief = json.loads((Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/yaniel"
                            / (slot_id + ".json")).read_text(encoding="utf-8"))
        self.assertEqual(slot["Text"], brief["default_text"])
        for flags, expected in ((set(), "morning"), ({yt.CUFF_PACKED}, "morning"),
                                ({yt.CUFF_WORN}, "morning_worn"),
                                ({yt.CUFF_WORN, yt.DECLINED, yt.VIGIL}, "morning")):
            self.assertEqual([c["Next"] for c in self.selected(slot["Choices"], flags)], [expected])
        self.assertEqual(len(self.node("visit.niche", "morning2")["Choices"]), 5)

    def test_actual_witness_not_return_or_niche_completion_earns_memory(self):
        witness = yt.MORNING_WITNESS
        self.assertIn(witness, self.node("visit.niche", "sexton_seelah")["Choices"][0]["Set"])
        self.assertNotIn(witness, self.node("visit.niche", "sexton")["Choices"][0]["Set"])
        reaction = self.scenes[yt.Y + "react.seelah_after"]
        self.assertIn(witness, reaction["Requires"])
        self.assertNotIn(witness, yt.DERIVED)
        self.assertNotIn("yesterday", reaction["Nodes"][0]["Text"].lower())
        exits = self.node("visit.niche", "morning_depart")["Choices"]
        for flags, target in (({"seelah.present_now"}, "sexton_seelah"),
                              ({yt.SEELAH_DEAD}, "sexton"),
                              ({yt.SEELAH_GONE}, "sexton"),
                              ({yt.SEELAH_DEAD, yt.SEELAH_BACK, "seelah.present_now"}, "sexton_seelah"),
                              ({yt.SEELAH_GONE, yt.SEELAH_BACK, "seelah.present_now"}, "sexton_seelah"),
                              ({yt.SEELAH_DEAD, yt.SEELAH_BACK}, "sexton"),
                              ({yt.SEELAH_GONE, yt.SEELAH_BACK}, "sexton"),
                              (set(), "sexton")):
            self.assertEqual([c["Next"] for c in self.selected(exits, flags)], [target])

    def test_departure_cannot_be_restored_by_unreturned_sacrifice(self):
        mourned = self.scenes[yt.Y + "epilogue.mourned"]
        self.assertTrue({yt.LEFT_FREE, yt.CLOSED, yt.KILLED, "trickster.commander_back"} <= set(mourned["Forbids"]))
        for scene in self.scenes.values():
            if scene["Id"].startswith(yt.Y + "epilogue."):
                for node in scene["Nodes"]:
                    for choice in node["Choices"]:
                        self.assertEqual(choice["Set"], [])

    def test_lastcall_and_ledger_preserve_acquisition_and_earned_reports(self):
        from storylines import lastcall_partners as partners
        from storylines import yaniel_radiance as radiance
        part = next(p for p in partners.PARTNERS if p["key"] == "yaniel")
        page = {"Id": "page", "Paragraphs": copy.deepcopy(list(part["paragraphs"]))}
        call = {"Id": "call", "Text": part["call"]["text"]}
        debt = {"Id": "owed.yaniel", "Text": part["ledger_text"], "Lines": []}
        payload = {"Scenes": [{"Id": "yaniel.lastcall.page", "Nodes": [page]},
                              {"Id": "yaniel.lastcall.call", "Nodes": [call]}],
                   "Books": {"trickster.ledger": {"Entries": [debt]}}, "Relationships": {}}
        radiance._reconcile_lastcall(payload)

        def visible(blocks, flags):
            return [p["Text"] for p in blocks if all(k in flags for k in p["Requires"])
                    and not any(k in flags for k in p["Forbids"])
                    and (not p["AnyGroups"] or any(all(k in flags for k in g)
                                                  for g in p["AnyGroups"]))]
        for late in (False, True):
            flags = {yt.OATH_STANDS, yt.JUDGES} | ({yt.LATE} if late else set())
            text = " ".join(visible(page["Paragraphs"], flags))
            self.assertNotIn("went to the Threshold", text)
            self.assertIn("sworn on her wall" if late else "sworn underground", text)
            ledger = debt["Text"] + " ".join(visible(debt["Lines"], flags))
            self.assertNotIn("trade-back", ledger)
            self.assertNotIn("vigil together", ledger)
            self.assertEqual("Midnight Fane" in ledger, not late)
        self.assertNotIn("since the Midnight Fane", call["Text"])
        for flags, expected, absent in (
            ({yt.CARRIES, yt.HOLY, yt.Y + "iz_song_reported"}, "sung in her hands", "after Iz"),
            ({yt.CARRIES, yt.HOLY, yt.HANDED_LATE}, "after Iz", "sung in her hands"),
            ({yt.CARRIES, yt.HOLY}, "checked its edge", "sung in her hands"),
            ({yt.JUDGES, yt.SANG}, "heard Radiance sing", "sung in her hands"),
        ):
            text = " ".join(visible(page["Paragraphs"], flags))
            self.assertIn(expected, text)
            self.assertNotIn(absent, text)
        report = next(s for s in yt.SCENES if s["Id"] == yt.Y + "verdict.letter")
        sang = next(n for n in report["Nodes"] if n["Id"] == "sang")
        self.assertIn(yt.Y + "iz_song_reported", sang["Choices"][0]["Set"])

    def test_confidence_survives_all_cuff_positions_and_ending_states(self):
        for suffix in ("together", "commit", "broken", "unasked", "unsettled", "distrusted", "declined"):
            page = self.node("epilogue." + suffix, "page")
            for cuff in (set(), {yt.CUFF_WORN}, {yt.Y + "cuff_pocketed"}):
                flags = {yt.HUSK_FREED, yt.Y + "husk_told"} | cuff
                visible = self.selected(page["Paragraphs"], flags)
                self.assertFalse(any("never told anyone" in p["Text"] or "Nobody was told" in p["Text"]
                                     for p in visible))
        wall = next(s for s in yt.SCENES if s["Id"] == yt.Y + "late.wall")
        self.assertIn("while the last carts fled", next(n for n in wall["Nodes"] if n["Id"] == "wall")["Text"])

    def test_spring_answer_appends_after_existing_memorial_only_to_living_couple(self):
        payload = {"Scenes": list(self.scenes.values()) + [{"Id": "yaniel.lastcall.page", "Nodes": [{"Id": "page"}]}]}
        yt.integrate_partner_memory(payload)
        for suffix in ("together", "commit"):
            page = self.node("epilogue." + suffix, "page")
            self.assertIn("Joran", page["Paragraphs"][-2]["Text"])
            self.assertEqual(page["Paragraphs"][-1]["Requires"], [yt.DRAWN_TREE, yt.B_ROAST])
        for suffix in ("declined", "distrusted", "broken", "unasked", "unsettled", "left_free", "mourned"):
            self.assertFalse(any(p["Requires"] == [yt.DRAWN_TREE, yt.B_ROAST]
                                 for p in self.node("epilogue." + suffix, "page")["Paragraphs"]))


if __name__ == "__main__":
    unittest.main()

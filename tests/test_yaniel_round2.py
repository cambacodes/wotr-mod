"""Route-local histories for the round-two situations and their receipts."""
import copy
import json
import unittest
from pathlib import Path

from storylines import yaniel_walls as walls
from storylines import yaniel_trickster as yt



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result


def only(items):
    """Require a single structural outcome, rejecting gaps and overlap."""
    try:
        outcome, = items
    except ValueError as error:
        raise AssertionError('Expected one structural outcome') from error
    return outcome

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
                self.assertIsNotNone(only(got))
                self.assertEqual(by_contract(got, [{'Next': 'judges_plain', 'Requires': ['yaniel.radiance_in_party'], 'Forbids': ['yaniel.trickster.carries', 'yaniel.trickster.raid.holy_in_party'], 'Set': [], 'Abort': False}, {'Next': 'judges', 'Requires': ['yaniel.radiance_in_party', 'yaniel.trickster.raid.holy_in_party'], 'Forbids': ['yaniel.trickster.carries'], 'Set': [], 'Abort': False}])["Next"], "judges" if form in ("ha4", "ha6") else "judges_plain")
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
                self.assertEqual(by_contract(self.node('beat.bout', choice['Check'][result])['Choices'], [{'Next': 'end', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"], "end")
        self.assertEqual(by_contract(self.node('beat.bout', 'end')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['yaniel.trickster.beat.bout'], 'Abort': False}])["Set"], [yt.B_BOUT])
        for node in self.scenes[yt.Y + "beat.bout"]["Nodes"]:
            for choice in node["Choices"]:
                self.assertNotIn(yt.TRUSTED, choice["Set"])

    def test_prior_raid_kiss_is_optional_and_recalled_only_when_earned(self):
        choices = self.node("commit.trade", "yes")["Choices"]
        self.assertEqual([c["Next"] for c in self.selected(choices, {yt.Y + "raid_kiss"})], ["yes_raid"])
        self.assertEqual([c["Next"] for c in self.selected(choices, {yt.DRAWN_WALLS})], ["yes2"])
        self.assertEqual(by_contract(self.node('commit.trade', 'ask')['Choices'], [{'Next': 'yes', 'Requires': [], 'Forbids': [], 'Set': ['yaniel.committed', 'yaniel.trickster.cost.shackle_kept'], 'Abort': False}])["Set"], [yt.COMMITTED, yt.SHACKLE])

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
        self.assertEqual(by_contract(self.node('visit.niche', 'threshold2')['Choices'], [{'Next': 'yaniel.trickster.visit.niche.explicit.1', 'Requires': [], 'Forbids': [], 'Set': [], 'Abort': False}])["Next"], slot_id)
        slot = self.node("visit.niche", slot_id)
        brief = json.loads((Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/yaniel"
                            / (slot_id + ".json")).read_text(encoding="utf-8"))
        self.assertEqual(slot_id, slot["Id"])
        for flags, expected in ((set(), "morning"), ({yt.CUFF_PACKED}, "morning"),
                                ({yt.CUFF_WORN}, "morning_worn"),
                                ({yt.CUFF_WORN, yt.DECLINED, yt.VIGIL}, "morning")):
            self.assertEqual([c["Next"] for c in self.selected(slot["Choices"], flags)], [expected])
        self.assertEqual(["morning_sword"] * 5, [c["Next"] for c in self.node("visit.niche", "morning2")["Choices"]])

    def test_actual_witness_not_return_or_niche_completion_earns_memory(self):
        witness = yt.MORNING_WITNESS
        self.assertIn(witness, by_contract(self.node('visit.niche', 'sexton_seelah')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['yaniel.trickster.niche_seen', 'yaniel.trickster.morning_seen', 'yaniel.trickster.morning.seelah_witness'], 'Abort': False}])["Set"])
        self.assertNotIn(witness, by_contract(self.node('visit.niche', 'sexton')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['yaniel.trickster.niche_seen', 'yaniel.trickster.morning_seen'], 'Abort': False}])["Set"])
        reaction = self.scenes[yt.Y + "react.seelah_after"]
        self.assertIn(witness, reaction["Requires"])
        self.assertNotIn(witness, yt.DERIVED)
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
        part = next(p for p in partners.PARTNERS if p['key'] == 'yaniel')
        page = {'Id': 'page', 'Paragraphs': copy.deepcopy(list(part['paragraphs']))}
        call = {'Id': 'call', 'Text': part['call']['text']}
        debt = {'Id': 'owed.yaniel', 'Text': part['ledger_text'], 'Lines': []}
        payload = {'Scenes': [{'Id': 'yaniel.lastcall.page', 'Nodes': [page]},
                              {'Id': 'yaniel.lastcall.call', 'Nodes': [call]}],
                   'Books': {'trickster.ledger': {'Entries': [debt]}}, 'Relationships': {}}
        radiance._reconcile_lastcall(payload)
        underground, = (p for p in page['Paragraphs'] if p['Requires'] == [yt.OATH_STANDS]
                        and p['Forbids'] == [yt.LATE])
        wall, = (p for p in page['Paragraphs'] if p['Requires'] == [yt.OATH_STANDS, yt.LATE])
        self.assertEqual([yt.OATH_THRESHOLD], wall['Forbids'])
        for late in (False, True):
            flags = {yt.OATH_STANDS, yt.JUDGES} | ({yt.LATE} if late else set())
            self.assertEqual(not late, bool(self.selected([underground], flags)))
            self.assertEqual(late, bool(self.selected([wall], flags)))
            acquired, = self.selected([p for p in debt['Lines'] if not p['Requires'] or p['Requires'] == [yt.LATE]], flags)
            self.assertEqual([yt.LATE] if late else [], acquired['Requires'])
            self.assertFalse(self.selected([p for p in debt['Lines'] if yt.SHACKLE in p['Requires']], flags))
        expected = (([yt.CARRIES, yt.HOLY], [yt.Y + 'iz_song_reported', yt.HANDED_LATE]),
                    ([yt.CARRIES, yt.HOLY, yt.Y + 'iz_song_reported'], [yt.HANDED_LATE]),
                    ([yt.CARRIES, yt.HOLY, yt.HANDED_LATE], []),
                    ([yt.JUDGES, yt.SANG], [yt.CARRIES]))
        accounts = []
        for requires, forbids in expected:
            account, = (p for p in page['Paragraphs'] if p['Requires'] == requires)
            self.assertEqual(forbids, account['Forbids'])
            accounts.append(account)
        for flags, wanted in (({yt.CARRIES, yt.HOLY}, [yt.CARRIES, yt.HOLY]),
                              ({yt.CARRIES, yt.HOLY, yt.Y + 'iz_song_reported'}, [yt.CARRIES, yt.HOLY, yt.Y + 'iz_song_reported']),
                              ({yt.CARRIES, yt.HOLY, yt.HANDED_LATE}, [yt.CARRIES, yt.HOLY, yt.HANDED_LATE]),
                              ({yt.JUDGES, yt.SANG}, [yt.JUDGES, yt.SANG])):
            account, = self.selected(accounts, flags)
            self.assertEqual(wanted, account['Requires'])
        report = next(s for s in yt.SCENES if s['Id'] == yt.Y + 'verdict.letter')
        sang = next(n for n in report['Nodes'] if n['Id'] == 'sang')
        self.assertTrue(all(yt.Y + 'iz_song_reported' in a['Set'] for a in sang['Choices']))


    def test_spring_answer_appends_after_existing_memorial_only_to_living_couple(self):
        payload = {"Scenes": list(self.scenes.values()) + [{"Id": "yaniel.lastcall.page", "Nodes": [{"Id": "page"}]}]}
        yt.integrate_partner_memory(payload)
        for suffix in ("together", "commit"):
            page = self.node("epilogue." + suffix, "page")

            self.assertEqual(by_contract(page['Paragraphs'], [{'Requires': ['yaniel.trickster.drawn.tree', 'yaniel.trickster.beat.roast'], 'Forbids': [], 'AnyGroups': []}])["Requires"], [yt.DRAWN_TREE, yt.B_ROAST])
        for suffix in ("declined", "distrusted", "broken", "unasked", "unsettled", "left_free", "mourned"):
            self.assertFalse(any(p["Requires"] == [yt.DRAWN_TREE, yt.B_ROAST]
                                 for p in self.node("epilogue." + suffix, "page")["Paragraphs"]))


if __name__ == "__main__":
    unittest.main()

"""Gesmerha's authored round-two histories, independent of the shared ending arbitration."""
import copy
import unittest
from unittest.mock import patch

from storylines import gesmerha_campaign, gesmerha_late_campaign, gesmerha_opening, gesmerha_trickster as route


def assembled():
    payload = {"Relationships": {"gesmerha": {"Guidance": ""}}, "Scenes": copy.deepcopy(
        gesmerha_opening.SCENES + gesmerha_campaign.SCENES + gesmerha_late_campaign.SCENES + route.SCENES)}
    route.integrate(payload)
    return payload


def matches(surface, flags):
    return (set(surface.get("Requires", ())) <= flags
            and not set(surface.get("Forbids", ())) & flags
            and (not surface.get("RequiresAny") or set(surface["RequiresAny"]) & flags)
            and all(set(group) & flags for group in surface.get("RequiresAnyGroups", surface.get("AnyGroups", ()))))



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class GesmerhaRoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = assembled()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def nodes(self, sid):
        return {n["Id"]: n for n in self.scenes[sid]["Nodes"]}

    def test_partial_authored_visits_are_not_first_meetings(self):
        prefixes = ["gesmerha.invited", "gesmerha.wood_kept", "gesmerha.mark_kept",
                    "gesmerha.game_kept", "gesmerha.hour_kept", "gesmerha.opening_kept",
                    "gesmerha.story_kept", "gesmerha.verse_kept", "gesmerha.singing_kept"]
        base = {"trickster", "trickster.ever", "gesmerha.wintersun_resolved", "gesmerha.capital_guest"}
        for suffix in ("home", "capital"):
            for outcome in ("gesmerha.truth", "gesmerha.illusions"):
                history = base | {outcome}
                first = self.scenes[route.P + "missed.first_meeting_" + suffix]
                known = self.scenes[route.P + "missed.wrong_footsteps_" + suffix]
                self.assertTrue(matches(first, history))
                for prefix in prefixes:
                    history.add(prefix)
                    self.assertFalse(matches(first, history), (suffix, prefix))
                    self.assertTrue(matches(known, history), (suffix, prefix))

    def test_paid_catchup_preserves_friendship_and_all_costs(self):
        for suffix in ("home", "capital"):
            ns = self.nodes(route.P + "missed.wrong_footsteps_" + suffix)
            for nid in ("game", "honest"):
                available = [c for c in ns[nid]["Choices"] if matches(c, {"gesmerha.friendship"})]
                answer, = available
                self.assertIn("gesmerha.campaign_friends", answer["Set"])
                self.assertNotIn("gesmerha.campaign_slow", answer["Set"])
                self.assertEqual({"Resource": "Finances", "Amount": -50}, answer["Crusade"])
        for sid, amount in ((route.P + "dead.commission", -150), (route.P + "dead.pyre", -300)):
            choices = [c for n in self.scenes[sid]["Nodes"] for c in n["Choices"] if "Crusade" in c]
            self.assertEqual([amount], [c["Crusade"]["Amount"] for c in choices])
        second = saved_answer(self.nodes(route.P + "returned.second_ask")["price"]["Choices"], 0)
        self.assertEqual({"Resource": "Favors", "Amount": -100}, second["Crusade"])
        self.assertEqual([route.COMMITTED, route.HANDS], second["Set"])

    def test_audience_uses_native_speaker_and_inline_return(self):
        for sid in ("gesmerha.the_voice_at_court", route.P + "missed.wrong_footsteps_capital",
                    route.P + "missed.first_meeting_capital"):
            s = self.scenes[sid]
            self.assertEqual("de348517119791d4e9f7de7de0beab25", s["NativeReturnCue"])
            self.assertFalse(s.get("ReturnToList", False))
            self.assertNotIn("ContactUnit", s)
            self.assertIn("gesmerha.capital_guest", s["Requires"])
            self.assertEqual([route.CAPITAL_LIST], s["AnswerLists"])
            for n in s["Nodes"]:
                if n["Speaker"] == "Gesmerha":
                    self.assertEqual(route.UNIT, n["SpeakerUnit"])

    def test_player_speaks_the_account_and_can_defer(self):
        ns = self.nodes("gesmerha.the_things_still_here")
        for nid in ("catchup", "first_met"):
            answer = saved_answer(ns[nid]["Choices"], 0)
            self.assertEqual("true_account", answer["Next"])
            self.assertTrue(any(c["Abort"] for c in ns[nid]["Choices"]))
        slow = self.nodes("gesmerha.the_room_she_chose")["slow"]
        self.assertEqual("lover_answer", saved_answer(slow["Choices"], 0)["Next"])

    def test_slots_keep_the_original_aftermath_and_receipt_locations(self):
        slots = [("gesmerha.what_she_asks", "private", "after_private", 1),
                 ("gesmerha.the_room_she_chose", "night", "after_night", 1),
                 ("gesmerha.the_room_she_chose", "first_night", "after_first_night", 2),
                 (route.P + "returned.bench", "night", "morning", 1),
                 (route.P + "returned.second_ask", "night", "morning", 1),
                 (route.P + "returned.second_ask", "night_flinched", "morning", 2)]
        for sid, nid, after, index in slots:
            ns = self.nodes(sid)
            slot = sid + ".explicit." + str(index)
            self.assertEqual(after, saved_answer(ns[nid]["Choices"], 0)["Next"])
            self.assertEqual(after, saved_answer(ns[slot]["Choices"], 0)["Next"])
            self.assertFalse(saved_answer(ns[slot]["Choices"], 0)["Set"])
            incoming = [c for n in ns.values() for c in n["Choices"] if c.get("Next") == slot]
            self.assertTrue(incoming, sid)
            retired = [c for n in ns.values() for c in n["Choices"] if c.get("Next") == nid]
            self.assertTrue(retired, sid)
            self.assertTrue(all(set(c["Requires"]) & set(c["Forbids"]) for c in retired), sid)
            for flags in (set(), {"trickster.now"}):
                continuation, = [c for c in ns[slot]["Choices"] if matches(c, flags)]
                self.assertEqual(continuation["Next"], after)
        self.assertEqual([route.NIGHT_YARD], saved_answer(self.nodes(route.P + "returned.bench")["morning"]["Choices"], 0)["Set"])

    def test_farewell_waits_for_chapter_five_and_iz(self):
        s = self.scenes[route.P + "returned.likeness"]
        self.assertEqual(5, s["MinChapter"])
        self.assertEqual([5], s["Chapters"])
        history = {"trickster.ever", route.RETURNED, route.COMMITTED}
        self.assertFalse(matches(s, history))
        self.assertTrue(matches(s, history | {"iz.done"}))

    def test_ulbrig_reads_actual_commission_release(self):
        before = next(s for s in route.REACTIONS if s["Id"] == route.P + "react.ulbrig_return")
        history = {route.RETURNED, "ulbrig.in_party"}
        self.assertTrue(matches(before, history))
        for nid in ("monster", "new"):
            for choice in self.nodes(route.P + "returned.bench")[nid]["Choices"]:
                released = history | {route.WORK_FINISHED}  # runtime marks completed scenes by ID
                self.assertFalse(matches(before, released))
                self.assertNotIn(route.COMMITTED, choice["Set"])
        self.assertFalse(matches(before, history | {"ulbrig.dead"}))

    def test_objective_survives_relocation(self):
        for sid in ('gesmerha.the_voice_at_court', route.P + 'missed.wrong_footsteps_capital', route.P + 'missed.first_meeting_capital'):
            self.assertEqual(self.scenes[sid]['Relationship'], 'gesmerha')
            self.assertEqual(self.scenes[sid]['AnswerLists'], [route.CAPITAL_LIST])

    def test_shared_sacrifice_fixes_cover_exact_histories(self):
        # Ending arbitration adds sacrifice guards and placement observation receipts.
        from tests.story_fixture import fresh_story
        story = fresh_story()
        scenes = story["Scenes"]
        pages = [s for s in scenes if s["Id"].startswith(route.P + "epilogue.")]
        base = {"trickster.ever", route.RETURNED, route.DEAD, "sacrifice", "availability.observed"}
        for receipt, expected in ((None, "unvisited_mourned"),
                                  (route.DECLINED, "refusal_mourned"),
                                  (route.CLOSED, "finished_mourned")):
            history = base | ({receipt} if receipt else set())
            # Native availability has been observed; expand its existing earned-return proof.
            for _ in range(4):
                for key, groups in story["Derived"].items():
                    if key.startswith("gesmerha.present_now") and any(set(g) <= history for g in groups):
                        if not set(story.get("DerivedForbids", {}).get(key, ())) & history:
                            history.add(key)
            available = [s["Id"] for s in pages if matches(s, history)]
            self.assertEqual([route.P + "epilogue." + expected], available)

    def test_shared_lastcall_fix_excludes_unaccepted_deliveries(self):
        from tests.story_fixture import fresh_story
        story = fresh_story()
        page = next(s for s in story["Scenes"] if s["Id"] == "gesmerha.lastcall.page")
        self.assertEqual([[route.COMMITTED]], page["RequiresAnyGroups"])
        for receipt in (route.YARD, "gesmerha.presence.failure_observed"):
            history = set(page["Requires"]) | {route.RETURNED, receipt, route.P + "late_committed"}
            self.assertFalse(matches(page, history))
        self.assertEqual([["gesmerha.payoff.ordinary"]], story["Derived"]["gesmerha.payoff.partner"])

    def test_clan_memorial_and_mourning_likeness_have_distinct_receipts(self):
        self.assertEqual(self.story['Derived'][route.CLAN_DESTROYED], [[route.DEAD, 'soana.forest_dead']])
        self.assertEqual(self.story['DerivedForbids'][route.CLAN_DESTROYED], ['gesmerha.marhevok_rules'])
        for ending in ('bench', 'commit', 'commit_mourned', 'bench_mourned', 'unvisited', 'refusal', 'finished'):
            paragraphs = self.scenes[route.P + 'epilogue.' + ending]['Nodes'][0]['Paragraphs']
            for destroyed in (False, True):
                flags = {route.STATUE_TRUE} | ({route.CLAN_DESTROYED} if destroyed else set())
                reader, = [p for p in paragraphs if route.STATUE_TRUE in p['Requires'] and matches(p, flags)]
                self.assertEqual(route.CLAN_DESTROYED in reader['Requires'], destroyed)
                self.assertEqual(route.CLAN_DESTROYED in reader['Forbids'], not destroyed)
        paragraphs = self.scenes[route.P + 'epilogue.bench_mourned']['Nodes'][0]['Paragraphs']
        readers = [p for p in paragraphs if route.LIKENESS_DONE in p['Requires'] or route.LIKENESS_DONE in p['Forbids']]
        self.assertTrue(readers)
        for receipt in (route.LIKENESS_DONE, route.LIKENESS, None):
            flags = {receipt} if receipt else set()
            reader, = [p for p in readers if matches(p, flags)]
            self.assertEqual(route.LIKENESS_DONE in reader['Requires'], receipt == route.LIKENESS_DONE)
            self.assertEqual(route.LIKENESS in reader['Requires'], receipt == route.LIKENESS)

    def test_failed_placement_does_not_supply_intimacy_in_route_text(self):
        s = self.scenes[route.P + "epilogue.commit"]
        terminal, = s["Nodes"][0]["Choices"]
        self.assertFalse(terminal["Abort"])
        self.assertIsNone(saved_answer(s["Nodes"][0]["Choices"], 0)["Next"])
        self.assertEqual([], saved_answer(s["Nodes"][0]["Choices"], 0)["Set"])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        node = self.nodes(route.P + 'missed.wrong_footsteps_home')['game']
        choice = next(c for c in node['Choices'] if 'gesmerha.campaign_friends' in c['Set'])
        with patch.dict(choice['Crusade'], Amount=-25):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_paid_catchup_preserves_friendship_and_all_costs()


if __name__ == "__main__":
    unittest.main()

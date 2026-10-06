"""Gesmerha's authored round-two histories, independent of the shared ending arbitration."""
import copy
import unittest

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
                self.assertEqual(1, len(available))
                self.assertIn("gesmerha.campaign_friends", available[0]["Set"])
                self.assertNotIn("gesmerha.campaign_slow", available[0]["Set"])
                self.assertEqual({"Resource": "Finances", "Amount": -50}, available[0]["Crusade"])
        for sid, amount in ((route.P + "dead.commission", -150), (route.P + "dead.pyre", -300)):
            choices = [c for n in self.scenes[sid]["Nodes"] for c in n["Choices"] if "Crusade" in c]
            self.assertEqual([amount], [c["Crusade"]["Amount"] for c in choices])
        second = self.nodes(route.P + "returned.second_ask")["price"]["Choices"][0]
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
            answer = ns[nid]["Choices"][0]
            self.assertIn("I came hunting demons", answer["Text"])
            self.assertEqual("true_account", answer["Next"])
            self.assertTrue(any(c["Abort"] for c in ns[nid]["Choices"]))
            self.assertNotIn("You tell her", ns[nid]["Text"])
        slow = self.nodes("gesmerha.the_room_she_chose")["slow"]
        self.assertEqual("lover_answer", slow["Choices"][0]["Next"])
        self.assertIn("I want to be your lover", slow["Choices"][0]["Text"])

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
            self.assertEqual(slot, ns[nid]["Choices"][0]["Next"])
            self.assertEqual(after, ns[slot]["Choices"][0]["Next"])
            self.assertFalse(ns[slot]["Choices"][0]["Set"])
            self.assertTrue(ns[slot]["Text"].startswith("{n}"))
        self.assertEqual([route.NIGHT_YARD], self.nodes(route.P + "returned.bench")["morning"]["Choices"][0]["Set"])

    def test_clan_memorial_and_mourning_likeness_have_distinct_receipts(self):
        pred = self.story["Derived"][route.CLAN_DESTROYED]
        self.assertEqual([[route.DEAD, "soana.forest_dead"]], pred)
        self.assertEqual(["gesmerha.marhevok_rules"], self.story["DerivedForbids"][route.CLAN_DESTROYED])
        for ending in ("bench", "commit", "commit_mourned", "bench_mourned", "unvisited", "refusal", "finished"):
            s = self.scenes[route.P + "epilogue." + ending]
            paragraphs = s["Nodes"][0]["Paragraphs"]
            for destroyed in (False, True):
                flags = {route.STATUE_TRUE} | ({route.CLAN_DESTROYED} if destroyed else set())
                monster = [p["Text"] for p in paragraphs if route.STATUE_TRUE in p["Requires"] and matches(p, flags)]
                self.assertEqual(1, len(monster), (ending, destroyed))
                self.assertEqual(destroyed, "clan was dead" in monster[0])
        paragraphs = self.scenes[route.P + "epilogue.bench_mourned"]["Nodes"][0]["Paragraphs"]
        for receipt, expected in ((route.LIKENESS_DONE, "without cutting it again"),
                                  (route.LIKENESS, "finished the waiting eyes"), (None, "never settled")):
            flags = {receipt} if receipt else set()
            text = " ".join(p["Text"] for p in paragraphs if matches(p, flags))
            self.assertIn(expected, text)
            if receipt == route.LIKENESS_DONE:
                self.assertNotIn("finished the waiting eyes", text)

    def test_failed_placement_does_not_supply_intimacy_in_route_text(self):
        s = self.scenes[route.P + "epilogue.commit"]
        self.assertEqual(1, len(s["Nodes"][0]["Choices"]))
        self.assertIsNone(s["Nodes"][0]["Choices"][0]["Next"])
        self.assertEqual([], s["Nodes"][0]["Choices"][0]["Set"])
        self.assertIn("no invitation owed", s["Nodes"][0]["Text"])


if __name__ == "__main__":
    unittest.main()

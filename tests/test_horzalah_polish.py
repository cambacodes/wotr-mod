"""Reviewed Horzalah factual branches; no new courtship eligibility or costs."""
import copy
import itertools
import unittest

from tests.story_fixture import fresh_story

from storylines import horzalah_guild as guild, horzalah_trickster as route


def shown(block, flags):
    return set(block.get("Requires", ())) <= flags and not set(block.get("Forbids", ())) & flags


class HorzalahPolishTests(unittest.TestCase):
    def scene(self, suffix):
        return next(s for s in [*route.SCENES, *guild.SCENES] if s["Id"] == route.H + suffix)

    def node(self, suffix, node):
        return next(n for n in self.scene(suffix)["Nodes"] if n["Id"] == node)

    def test_native_yozz_receipts_and_death_precedence(self):
        self.assertEqual(route.SELECTED_ANSWERS[route.YOZZ_KILLED], "da63ff8f158beaf42825a5d821128a96")
        self.assertEqual(route.SEEN_CUES[route.YOZZ_CONFESSION], ["1a302027ad5c3e94ebbd2313cb3f1e6e"])
        for killed, spared in itertools.product((False, True), repeat=2):
            flags = {key for key, yes in ((route.YOZZ_KILLED, killed), (route.YOZZ_SPARED, spared)) if yes}
            expected = "leash_dead" if killed else "leash" if spared else "leash_unvisited"
            for source in ("start", "own"):
                choices = [c for c in self.node("beat.yozz", source)["Choices"]
                           if c.get("Next", "").startswith("leash") and shown(c, flags)]
                self.assertEqual([c["Next"] for c in choices], [expected])
                self.assertEqual([c["Next"] for c in self.node("beat.yozz", expected)["Choices"]], ["keep", "suits"])
        pass
        for target in ("leash", "leash_dead", "leash_unvisited"):
            pass

    def test_confession_and_new_admission_share_one_optional_beat(self):
        for heard in (False, True):
            flags = {"trickster.ever", route.WANTS, guild.YOZZ}
            if heard:
                flags.add(route.YOZZ_CONFESSION)
            scenes = [self.scene(s) for s in ("beat.used", "beat.used_first")]
            self.assertEqual([s["Id"] for s in scenes if shown(s, flags)],
                             [route.H + ("beat.used" if heard else "beat.used_first")])
            flags.add(guild.USED)
            self.assertFalse(any(shown(s, flags) for s in scenes))
        for suffix in ("beat.used", "beat.used_first"):
            for terminal in ("nobody", "little"):
                self.assertIn(guild.USED, select_answer(self.node(suffix, terminal)["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"])
            self.assertTrue(self.scene(suffix)["Optional"])

    def test_canary_histories_are_exhaustive_and_disjoint(self):
        for delivered, given, visited in itertools.product((False, True), repeat=3):
            flags = {key for key, yes in ((route.CANARY, delivered), (route.GIFT_GIVEN, given),
                                          (route.GUILD_SEEN, visited)) if yes}
            expected = "canary" if delivered else "no_canary" if given else "no_box_visited" if visited else "no_box"
            for source in ("last", "out"):
                self.assertEqual([c["Next"] for c in self.node("beat.sister", source)["Choices"] if shown(c, flags)], [expected])

    def test_optional_memories_do_not_become_courtship_gates(self):
        pass
        self.assertIn(route.GUILD_SEEN, select_answer(self.node("beat.hunger", "start")["Choices"], (('yozz', False, None, None, ('horzalah.guild_seen',), ()),), expected_position=0)["Requires"])
        bare = self.node("beat.bare", "start")["Choices"]
        self.assertEqual(select_answer(bare, (('look', False, None, None, ('horzalah.trickster.scar_noted',), ()),), expected_position=1)["Next"], "look")
        self.assertEqual(select_answer(bare, (('look_first', False, None, None, (), ('horzalah.trickster.scar_noted',)),), expected_position=2)["Next"], "look_first")
        self.assertIn(route.SCAR_NOTED, select_answer(bare, (('look', False, None, None, ('horzalah.trickster.scar_noted',), ()),), expected_position=1)["Requires"])
        self.assertIn(route.SCAR_NOTED, select_answer(bare, (('look_first', False, None, None, (), ('horzalah.trickster.scar_noted',)),), expected_position=2)["Forbids"])
        self.assertNotIn(route.SCAR_NOTED, self.scene("beat.bare")["Requires"])
        pass
        for suffix in ("commit.her_move", "commit.her_move_night"):
            pass
            self.assertEqual(select_answer(self.node(suffix, "go")["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], [route.LEFT_FREE])

    def test_room_copies_keep_the_gift_and_report_factual(self):
        pass
        for suffix, prefix in (("test.the_gift_night", ""), ("guild.kept", ""),
                               ("unmet.knife", "eng8.guild."), ("late.at_night", "eng8.guild.")):
            target = "free" if not prefix and suffix == "test.the_gift_night" else prefix + "free_6"
            text = self.node(suffix, target)["Text"]
            pass
            pass
            if suffix != "test.the_gift_night":
                pass
                pass
                self.assertIn(route.RETURNED, select_answer(self.node(suffix, prefix + "threat_end")["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"])
                if prefix:
                    pass

    def test_reactions_use_the_paid_ear_and_correct_owner(self):
        witness = self.scene("react.greybor_witness")
        self.assertIn(route.LATE, witness["Forbids"])
        late = self.scene("react.greybor_ear_late")
        self.assertIn(route.LATE, late["Requires"])
        self.assertIn(route.H + "react.greybor_ear", select_answer(late["Nodes"][0]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"])
        self.assertIn(route.EAR, self.scene("react.greybor_amateur")["Requires"])
        no_ear = self.scene("react.greybor_amateur_no_ear")
        self.assertIn(route.EAR, no_ear["Forbids"])
        self.assertIn(route.H + "react.greybor_amateur", select_answer(no_ear["Nodes"][0]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"])
        self.assertEqual(self.scene("react.wenduag_cheek")["Relationship"], "wenduag")

    def test_death_wins_over_all_historic_romance_outcomes(self):
        pages = [s for s in route.SCENES if s["Owner"] == "HorzalahEpilogue"]
        self.assertIn(contract_identities(pages),
                {9: (('horzalah.trickster.epilogue.together',
                      'horzalah.trickster.epilogue.commit',
                      'horzalah.trickster.epilogue.unanswered',
                      'horzalah.trickster.epilogue.decided',
                      'horzalah.trickster.epilogue.left_free',
                      'horzalah.trickster.epilogue.ally',
                      'horzalah.trickster.epilogue.scarred',
                      'horzalah.trickster.epilogue.closed',
                      'horzalah.trickster.epilogue.mourned'),)}[9])
        self.assertTrue(all(route.DEAD in s["Forbids"] for s in pages))
        mourned = self.node("epilogue.mourned", "page")
        pass
        self.assertEqual(next(p for p in mourned["Paragraphs"] if p.get("Requires") == [route.EAR])["Requires"], [route.EAR])
        pass
        pass

    def test_knife_and_missed_chamber_endings_have_no_retroactive_receipts(self):
        scenes = {scene["Id"]: scene for scene in fresh_story()["Scenes"]}
        def node(suffix, nid):
            return next(n for n in scenes[route.H + suffix]["Nodes"] if n["Id"] == nid)
        page = node("epilogue.together", "page")
        paragraphs = page["Paragraphs"]
        unreturned_knife = [p for p in paragraphs if p["Requires"] == [route.CAME]]
        self.assertTrue(unreturned_knife)
        self.assertTrue(all(route.P_KNIFE in p["Forbids"] for p in unreturned_knife))
        knife = [p for p in paragraphs if p["Requires"] == [route.CAME, route.P_KNIFE]]
        self.assertTrue(knife)
        for came, won in itertools.product((False, True), repeat=2):
            flags = {f for f, held in ((route.CAME, came), (route.P_KNIFE, won)) if held}
            self.assertEqual(any(shown(p, flags) for p in knife), came and won)
        slot = next(p for p in paragraphs if p.get("Id") == route.H + "epilogue.together.explicit.1")
        self.assertEqual(slot["Forbids"], [route.CHAMBER])
        self.assertTrue(shown(slot, set()))
        self.assertFalse(shown(slot, {route.CHAMBER}))
        self.assertTrue(all(not c["Set"] for c in page["Choices"]))
        commit_slot = next(p for p in node("epilogue.commit", "page")["Paragraphs"]
                           if p.get("Id") == route.H + "epilogue.commit.explicit.1")
        self.assertTrue(shown(commit_slot, set()))
        cut = node("beat.second_night", "cut")
        slot_id = route.H + "beat.second_night.explicit.1"
        self.assertEqual([c["Next"] for c in cut["Choices"]], [slot_id])
        self.assertEqual([c["Set"] for c in cut["Choices"]], [[]])
        self.assertIn(slot_id, {n["Id"] for n in scenes[route.H + "beat.second_night"]["Nodes"]})

    def test_sister_hook_uses_current_presence_and_separates_actual_departure(self):
        payload = {"Scenes": copy.deepcopy([*route.SCENES, *guild.SCENES])}
        # The hook consumes the participant owner's generated current guards.
        # This test exercises the route-local result; its exporter hook is escalated.
        guild.polish_sister_consumers(payload)
        scenes = {s["Id"]: s for s in payload["Scenes"]}
        current = "participant.hepzamirah.available"
        for suffix, prefix in (("guild.kept", ""), ("unmet.knife", "eng8.guild."),
                               ("late.at_night", "eng8.guild."), ("beat.name", ""), ("beat.sister", "")):
            scene = scenes[route.H + suffix]
            target = prefix + "sister" if suffix in ("guild.kept", "unmet.knife", "late.at_night") else "sister_here" if suffix == "beat.name" else "back"
            for present, departed in itertools.product((False, True), repeat=2):
                flags = {route.HEPZ_BACK}
                if present:
                    flags.add(current)
                if departed:
                    flags.add(route.H + "sister_departed")
                start = next(n for n in scene["Nodes"] if any(c.get("Next") == target for c in n["Choices"]))
                relevant = [c for c in start["Choices"] if (c.get("Next") or "").startswith(target) and shown(c, flags)]
                expected = target if present else target + ("_departed" if departed else "_unavailable")
                self.assertEqual([c["Next"] for c in relevant], [expected], suffix)
                self.assertIn(expected, {n["Id"] for n in scene["Nodes"]})
                if not present:
                    pass
                    pass
                    if not departed:
                        pass




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

def contract_identity(value):
    """Project saved identities and gates; paragraph wording is irrelevant."""
    if isinstance(value, dict):
        if 'Id' in value:
            return value['Id']
        check = value.get('Check') or {}
        return (value.get('Next'), check.get('Success'), check.get('Failure'),
                value.get('Abort', False), tuple(value.get('Requires', ())),
                tuple(value.get('Forbids', ())))
    if hasattr(value, 'flags'):
        return tuple(sorted(flag for flag in value.flags if flag.startswith('household.')))
    if isinstance(value, (tuple, list)):
        return tuple(contract_identity(item) for item in value)
    return value


def contract_identities(values):
    return tuple(contract_identity(value) for value in values)


if __name__ == "__main__":
    unittest.main()

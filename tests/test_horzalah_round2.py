"""Round-2 negative histories against the assembled export, including folded copies."""
import itertools
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from storylines import horzalah_trickster as route


def shown(block, flags):
    return (set(block.get("Requires", ())) <= flags
            and not set(block.get("Forbids", ())) & flags
            and all(set(group) & flags for group in block.get("AnyGroups", ())))


class HorzalahRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}

    def node(self, suffix, nid):
        return next(n for n in self.scenes[route.H + suffix]["Nodes"] if n["Id"] == nid)

    def test_cut_checkpoint_resumes_remainder_without_paid_outcome(self):
        for suffix, opening in (("mercy.gift", "guess"), ("unmet.knife", "start"), ("late.at_night", "start")):
            cut = self.node(suffix, "cut")
            if self.scenes[route.H + suffix].get("NativeReturnCue"):
                self.assertFalse(cut.get("EnterSet"))
                incoming = [answer for node in self.scenes[route.H + suffix]["Nodes"]
                            for answer in node["Choices"] if answer["Next"] == "cut"]
                self.assertTrue(incoming)
                self.assertTrue(all(route.EAR in answer["Set"] for answer in incoming))
                self.assertTrue(all(set(answer['Set']) == {route.EAR} for answer in incoming))
                flags = {route.EAR}
            else:
                flags = set(cut["EnterSet"])
            self.assertIn(route.EAR, flags)
            self.assertNotIn(route.PRIMED, flags)
            self.assertNotIn(route.RETURNED, flags)
            choices = [c for c in self.node(suffix, opening)["Choices"] if shown(c, flags)]
            self.assertEqual([c["Next"] for c in choices], ["no_priest" if suffix == "late.at_night" else "box"])
            flags.add(route.PRIMED)
            self.assertFalse(any(shown(c, flags) for c in self.node(suffix, opening)["Choices"]))

    def test_folded_arrival_and_sister_state_in_actual_export(self):
        current = "participant.hepzamirah.available"
        departed = route.H + "sister_departed"
        for suffix in ("unmet.knife", "late.at_night"):
            arrival = self.node(suffix, "eng8.guild.arrival")
            self.assertEqual(select_answer(arrival["Choices"], (('eng8.guild.start', False, None, None, (), ()),), expected_position=0)["Next"], "eng8.guild.start")
            for present, left in itertools.product((False, True), repeat=2):
                flags = {route.HEPZ_BACK}
                if present:
                    flags.add(current)
                if left:
                    flags.add(departed)
                choices = [c for c in self.node(suffix, "eng8.guild.hall")["Choices"]
                           if (c.get("Next") or "").startswith("eng8.guild.sister") and shown(c, flags)]
                target = "eng8.guild.sister" + ("" if present else "_departed" if left else "_unavailable")
                self.assertEqual([c["Next"] for c in choices], [target])

    def test_unpaid_endings_cannot_grant_guild_authority(self):
        for suffix in ('epilogue.closed', 'epilogue.mourned'):
            scene = self.scenes[route.H + suffix]
            self.assertFalse(any(route.RETURNED in c['Set'] or route.PRIMED in c['Set']
                                 for n in scene['Nodes'] for c in n['Choices']))
            self.assertTrue(all(not c['Set'] and c['Next'] is None
                                for c in self.node(suffix, 'page')['Choices']))
            self.assertEqual(scene.get('Owner'), 'HorzalahEpilogue')

    def test_legacy_ending_exits_and_chamber_travel(self):
        for suffix in ("together", "commit", "decided", "unanswered", "left_free", "ally", "scarred", "closed", "mourned"):
            choices = self.node("epilogue." + suffix, "page")["Choices"]
            _single_result, = choices
            self.assertEqual(select_answer(choices, ((None, False, None, None, (), ()),), expected_position=0)["Set"], [])
            self.assertIsNone(select_answer(choices, ((None, False, None, None, (), ()),), expected_position=0)["Next"])
            self.assertFalse(select_answer(choices, ((None, False, None, None, (), ()),), expected_position=0)["Abort"])
        for nid in ("morning2", "doorway"):
            node = self.node("visit.chamber", nid)
            terminal = select_answer(node["Choices"], ((None, False, None, None, (), ()),), expected_position=0)
            self.assertEqual(terminal["Set"], [route.CHAMBER, route.MORNING])
            self.assertIsNone(terminal["Next"])

    def test_slots_have_briefs_and_one_first_night_per_history(self):
        directory = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/horzalah"
        briefs = [json.loads(p.read_text(encoding="utf-8")) for p in directory.glob("*.json")]
        # Four built slots; tracker briefs (host_scene/host_node, no reserved node yet) name a live host instead.
        built = [b for b in briefs if "host_scene" not in b]
        trackers = [b for b in briefs if "host_scene" in b]
        self.assertIn(contract_identities(built),
                {4: (((None, None, None, False, (), ()),
                      (None, None, None, False, (), ()),
                      (None, None, None, False, (), ()),
                      (None, None, None, False, (), ())),)}[4])
        slots = {n["Id"] for s in self.scenes.values() for n in s["Nodes"] if ".explicit." in n["Id"]}
        slots.update(p["Id"] for s in self.scenes.values() for n in s["Nodes"]
                     for p in n.get("Paragraphs", ()) if ".explicit." in p.get("Id", ""))
        self.assertTrue({b["slot_id"] for b in built} <= slots)
        for brief in trackers:
            host = self.scenes[brief["host_scene"]]
            self.assertIn(brief["host_node"], {n["Id"] for n in host["Nodes"]})
        together = self.node("epilogue.together", "page")
        first = next(p for p in together["Paragraphs"] if p.get("Id") == route.H + "epilogue.together.explicit.1")
        self.assertTrue(shown(first, set()))
        self.assertFalse(shown(first, {route.CHAMBER}))




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

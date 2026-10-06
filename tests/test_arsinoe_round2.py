"""Route-local interruption and intimacy histories, without a game or build."""
import json
from pathlib import Path
import unittest

from storylines import arsinoe_opening, arsinoe_continuation, arsinoe_campaign, arsinoe_trickster


MODULES = (arsinoe_opening, arsinoe_continuation, arsinoe_campaign, arsinoe_trickster)
SCENES = {s["Id"]: s for module in MODULES for s in module.SCENES}


def visible(choice, flags):
    return set(choice.get("Requires", ())) <= flags and not set(choice.get("Forbids", ())) & flags


def paths(scene_id, flags, node_id=None):
    """Walk every selectable answer; fail on dead ends and unintended cycles."""
    scene = SCENES[scene_id]
    nodes = {n["Id"]: n for n in scene["Nodes"]}
    pending = [(node_id or scene["Nodes"][0]["Id"], set(flags), ())]
    endings = []
    while pending:
        key, state, trace = pending.pop()
        if key in trace:
            raise AssertionError((scene_id, "cycle", trace, key))
        node = nodes[key]
        state.update(node.get("EnterSet", ()))
        choices = [c for c in node["Choices"] if visible(c, state)]
        if not choices:
            raise AssertionError((scene_id, "no selectable answers", key, state))
        for choice in choices:
            after = state | set(choice.get("Set", ()))
            visited = trace + (key,)
            if choice.get("Abort"):
                continue
            if choice.get("Check"):
                for outcome in ("Success", "Failure"):
                    pending.append((choice["Check"][outcome], after, visited))
            elif choice.get("Next"):
                pending.append((choice["Next"], after, visited))
            else:
                endings.append((visited, after))
    return endings


class ArsinoeRound2Tests(unittest.TestCase):
    def test_interrupted_print_result_cannot_be_rerolled(self):
        for receipt in ("arsinoe.print_source_found", "arsinoe.print_source_uncertain"):
            outcomes = paths("arsinoe_city_on_paper", {receipt}, "picture")
            self.assertTrue(outcomes)
            for trace, flags in outcomes:
                self.assertFalse({"arsinoe.print_source_found", "arsinoe.print_source_uncertain"} <= flags)
                self.assertNotIn("uncertain" if receipt.endswith("found") else "recognized", trace)

    def test_interrupted_picture_decision_keeps_one_selection(self):
        for receipt in ("arsinoe.picture_open_space", "arsinoe.picture_stall"):
            outcomes = paths("arsinoe_first_impression", {receipt}, "omission")
            self.assertTrue(outcomes)
            for _, flags in outcomes:
                self.assertFalse({"arsinoe.picture_open_space", "arsinoe.picture_stall"} <= flags)

    def test_early_night_is_optional_and_does_not_commit(self):
        scene = "arsinoe_the_unprofitable_hour"
        for approach in ("courting", "slow", "friendship"):
            outcomes = paths(scene, {"arsinoe." + approach, "arsinoe.interest_stories"})
            self.assertTrue(outcomes)
            nights = [flags for _, flags in outcomes if "arsinoe.unprofitable_night_shared" in flags]
            self.assertEqual(approach == "courting", bool(nights))
            for _, flags in outcomes:
                self.assertNotIn("arsinoe.committed", flags)
                self.assertNotIn("arsinoe.campaign_lover", flags)
            self.assertTrue(any("arsinoe.unprofitable_night_shared" not in f for _, f in outcomes))

    def test_all_nights_reach_their_original_morning_receipts(self):
        intimacy = arsinoe_trickster.INTIMACY
        for returning in (False, True):
            flags = {"arsinoe.campaign_lover"} | ({intimacy} if returning else set())
            window = paths("arsinoe_the_window_opens", flags)
            self.assertEqual(1, sum("arsinoe.night_shared" in f for _, f in window))
            collection = paths(arsinoe_trickster.COLLECTION, flags, "stay")
            self.assertEqual(1, sum("arsinoe.trickster.collection_night_shared" in f for _, f in collection))
            for sid in ("arsinoe_the_window_opens", arsinoe_trickster.COLLECTION):
                for node in SCENES[sid]["Nodes"]:
                    if ".explicit." in node["Id"]:
                        self.assertFalse(any(c.get("Set") for c in node["Choices"]))
        business = paths(arsinoe_trickster.COLLECTION, set(), "stay")
        self.assertFalse(any("arsinoe.trickster.collection_night_shared" in f for _, f in business))

    def test_late_accepted_and_declined_menus_stay_distinct(self):
        for returning in (False, True):
            flags = {arsinoe_trickster.LATE_ACCEPTED}
            if returning:
                flags.add(arsinoe_trickster.INTIMACY)
            outcomes = paths("arsinoe.trickster.late.commit", flags)
            self.assertEqual(2, len(outcomes))
            self.assertTrue(any("deferred_evening" in t and "table" in t for t, _ in outcomes))
            self.assertFalse(any("business" in t for t, _ in outcomes))
        declined = paths("arsinoe.trickster.late.commit", {arsinoe_trickster.LATE_DECLINED})
        self.assertEqual(1, len(declined))
        self.assertIn("business", declined[0][0])
        self.assertFalse(any(".explicit." in n for n in declined[0][0]))

    def test_lost_path_keeps_ordinary_carving_answers(self):
        for path in ("legend", "dragon", "trickster.failed"):
            outcomes = paths("arsinoe_a_stone_in_hand", {"trickster", path})
            self.assertTrue(outcomes)
            self.assertFalse(any("possibility" in t for t, _ in outcomes))

    def test_each_brief_matches_its_slot_and_last_line(self):
        root = Path(__file__).resolve().parents[1]
        briefs = list((root / "tools/route_packs/explicit_slots/arsinoe").glob("*.json"))
        self.assertEqual(5, len(briefs))
        nodes = {n["Id"]: n for s in SCENES.values() for n in s["Nodes"] if ".explicit." in n["Id"]}
        self.assertEqual({p.stem for p in briefs}, set(nodes))
        for path in briefs:
            brief = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(nodes[path.stem]["Text"].endswith('"' + brief["last_line"][3:] + '"'))
            self.assertEqual(["a man", "a woman"], brief["commander_variants"])


if __name__ == "__main__":
    unittest.main()

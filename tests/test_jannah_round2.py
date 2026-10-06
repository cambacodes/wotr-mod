"""Selected-path regressions for Jannah's existing debts and factual histories."""
import unittest

from storylines import jannah_circle as circle, jannah_trickster as jan


class RouteWalk:
    """Walk one nominated answer path; never infer selection from its effects."""

    def __init__(self, flags=()):
        self.flags = set(flags) | {"trickster.ever"}
        self.visited = []

    def has(self, flag, stack=()):
        if flag in self.flags:
            return True
        if flag in stack:
            return False
        if flag == jan.P + "no_false_blood":
            return jan.LIED not in self.flags
        if flag == jan.P + "not_declined":
            return jan.DECLINED not in self.flags
        if flag == jan.P + "no_cage_killing":
            return jan.SEELAH_KILLED_AT_CAGE not in self.flags
        if flag == jan.P + "seelah_not_back":
            return jan.SEELAH_BACK not in self.flags
        return any(all(self.has(f, (*stack, flag)) for f in g)
                   for g in jan.DERIVED.get(flag, []))

    def allowed(self, choice):
        return (all(self.has(f) for f in choice.get("Requires", []))
                and not any(self.has(f) for f in choice.get("Forbids", [])))

    def walk(self, scene, selections, checks=None, on_choice=None):
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        node_id = scene["Nodes"][0]["Id"]
        for _ in range(80):
            node = nodes[node_id]
            choices = node["Choices"]
            available = [i for i, c in enumerate(choices) if self.allowed(c)]
            if not available:
                raise AssertionError((scene["Id"], node_id, "no selectable answer"))
            index = selections.get(node_id, available[0])
            if index not in available:
                raise AssertionError((scene["Id"], node_id, index, available))
            choice = choices[index]
            self.visited.append((scene["Id"], node_id, index))
            self.flags.update(choice.get("Set", []))
            if on_choice:
                on_choice(node_id, index, self.flags)
            target = choice.get("Next")
            if choice.get("Check"):
                target = choice["Check"][checks.get(node_id, "Success")]
            if target is None:
                if not choice.get("Abort"):
                    self.flags.add(scene["Id"])
                return
            node_id = target
        raise AssertionError("nonterminal path")


class JannahRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in [*jan.SCENES, *circle.SCENES]}

    def test_actual_combined_refusals_pay_each_debt_before_yes(self):
        for cause, challenge_choices, checks, repair_index in (
            (jan.THREW, {"bout": 2, "bout_again": 2}, {}, 0),
            (jan.SHAMED, {"you_first": 2}, {}, 1),
            (jan.REFUSED_YIELD, {"her_first": 1}, {"bout": "Failure"}, 2),
        ):
            with self.subTest(cause=cause):
                walk = RouteWalk({jan.RETURNED, jan.WALLS, jan.LIED, jan.HH_SEEN})
                walk.walk(self.scenes[jan.P + "challenge"], {"lie": 1, **challenge_choices}, checks)
                self.assertIn((jan.P + "challenge", "lie", 1), walk.visited)
                self.assertIn(cause, walk.flags)
                self.assertNotIn(jan.COMMITTED, walk.flags)
                if cause == jan.REFUSED_YIELD:
                    self.assertIn(jan.SHE_FIRST, walk.flags)
                def before_yes(node, index, flags):
                    if node != "repair_yes":
                        self.assertNotIn(jan.COMMITTED, flags)
                walk.walk(self.scenes[jan.P + "chalk_circle"],
                          {"open": 0, "repair_due": repair_index, "repair_yes": 0}, on_choice=before_yes)
                self.assertIn((jan.P + "chalk_circle", "repair_due", repair_index), walk.visited)
                self.assertTrue({jan.COMMITTED, jan.CONFESSED, jan.LATE_YES} <= walk.flags)
                self.assertEqual(cause == jan.SHAMED, jan.PUBLIC_REPAIR in walk.flags)
                self.assertEqual(cause == jan.REFUSED_YIELD, jan.LATE_YIELD in walk.flags)
                self.assertNotIn(jan.PUBLIC_YIELD, walk.flags)

    def test_leaving_after_confession_still_closes(self):
        walk = RouteWalk({jan.HELD_LIE, jan.LIED, jan.THREW, jan.DECLINED})
        walk.walk(self.scenes[jan.P + "chalk_circle"], {"open": 0, "repair_due": 4})
        self.assertTrue({jan.CLOSED, jan.GONE} <= walk.flags)
        self.assertNotIn(jan.COMMITTED, walk.flags)

    def test_late_readiness_never_cancels_false_blood(self):
        for confessed in (False, True):
            walk = RouteWalk({jan.WALLS, jan.LIED} | ({jan.CONFESSED} if confessed else set()))
            self.assertEqual(confessed, walk.has(jan.LATE_COMMITTED))
        for cause in (jan.THREW, jan.SHAMED, jan.REFUSED_YIELD):
            walk = RouteWalk({jan.WALLS, jan.DECLINED, cause})
            self.assertFalse(walk.has(jan.LATE_COMMITTED))

    def test_curl_and_door_full_rescue_precedence(self):
        for paid in ("kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back"):
            for native in (False, True):
                walk = RouteWalk({paid} | ({jan.SOULS} if native else set()))
                walk.walk(self.scenes[circle.CURL], {})
                self.assertIn((circle.CURL, "which_paid", 0), walk.visited)
                walk = RouteWalk({paid, jan.ELAN_DEAD})
                walk.walk(self.scenes[circle.DOOR], {})
                self.assertIn((circle.DOOR, "start_paid", 0), walk.visited)
        walk = RouteWalk({"kiana.trickster.returned", "kiana.trickster.cost.guests_robbed"})
        walk.walk(self.scenes[circle.CURL], {})
        self.assertIn((circle.CURL, "which", 0), walk.visited)

    def test_phase_and_optional_deliveries(self):
        for sid in (circle.BLADE, circle.SPARRING):
            self.assertIn(jan.P + "challenge", self.scenes[sid]["Forbids"])
        for sid in (circle.RIDE, circle.TAUGHT, circle.AFTER_WALL, circle.SONG):
            s = self.scenes[sid]
            self.assertFalse(s.get("Remote", False))
            self.assertFalse(s.get("ManualOnly", False))
            self.assertEqual(jan.PRESENCE, s["InteractionHub"])
            self.assertTrue(s["Entry"])

    def test_elapsed_budget_from_coronation_and_real_producers(self):
        spine = [jan.P + "alive.letter", jan.P + "alive.stories", jan.FORMS,
                 jan.HOUNDHEART, jan.WALLS, jan.P + "challenge", jan.P + "chalk_circle"]
        for wagon in (False, True):
            walk = RouteWalk({"trickster", "coronation.seen", jan.FREE, jan.HH_SEEN})
            elapsed = 0
            for sid in spine:
                scene = self.scenes[sid]
                elapsed += scene["DelayHours"]
                choices = {}
                if sid == jan.P + "alive.stories":
                    choices = {"start": 0, "choose": 0, "stake": 0,
                               "your_tale": 1 if wagon else 0}
                elif sid == jan.P + "challenge":
                    choices = {"bout": 2, "bout_again": 2}
                elif sid == jan.P + "chalk_circle":
                    choices = {"open": 1, "repair_yes": 0}
                # Force the native check result, not its resulting flags.
                checks = {"your_tale": "Failure" if wagon else "Success"}
                walk.walk(scene, choices, checks)
                if sid == jan.P + "alive.stories" and wagon:
                    self.assertIn(jan.POSTED, walk.flags)
                    scene = self.scenes[jan.P + "alive.wagon"]
                    elapsed += scene["DelayHours"]
                    walk.walk(scene, {"said": 0})
            self.assertIn(jan.COMMITTED, walk.flags)
            self.assertEqual(168 if wagon else 132, elapsed)

    def test_slots_keep_old_targets_and_are_not_another_first_night(self):
        night = self.scenes[jan.NIGHT]
        self.assertIn(jan.NIGHT, night["Forbids"])
        for sid in (jan.NIGHT, circle.TAUGHT):
            self.assertIn(sid + ".explicit.1", {n["Id"] for n in self.scenes[sid]["Nodes"]})
        self.assertIn(jan.NIGHT, self.scenes[circle.TAUGHT]["Requires"])


if __name__ == "__main__":
    unittest.main()

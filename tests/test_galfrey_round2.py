"""Route-source conversations and cuts; shared generated guards are escalated."""
import itertools
import json
from pathlib import Path
import unittest

from storylines import galfrey_trickster as g, galfrey_kitrane as k


class GalfreyRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in g.SCENES + k.SCENES}

    def holds(self, key, flags):
        if key.startswith("!"):
            return not self.holds(key[1:], flags)
        if key in flags:
            return True
        return any(all(self.holds(x, flags) for x in group)
                   for group in g.DERIVED.get(key, []))

    def traverse(self, scene, flags):
        """Explore every selectable answer and both outcomes of skill checks."""
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        pending = [(scene["Nodes"][0]["Id"], frozenset(flags))]
        visited = set()
        texts = []
        while pending:
            nid, state = pending.pop()
            if (nid, state) in visited:
                continue
            visited.add((nid, state))
            node = nodes[nid]
            texts.append(node["Text"])
            choices = [c for c in node["Choices"]
                       if all(self.holds(x, state) for x in c.get("Requires", []))
                       and not any(self.holds(x, state) for x in c.get("Forbids", []))]
            self.assertTrue(choices, (scene["Id"], nid, sorted(state)))
            for choice in choices:
                after = state | frozenset(choice.get("Set", []))
                destinations = ([choice["Check"][b] for b in ("Success", "Failure")]
                                if choice.get("Check") else [choice.get("Next")])
                pending.extend((dest, after) for dest in destinations if dest)
        return "\n".join(texts)

    def test_deathbed_name_and_carrier_histories_have_answers(self):
        for met, seed, manuscripts, irabeth, rank in itertools.product((False, True), repeat=5):
            flags = {"trickster", "iomedae.closed", "seelah_dead"}
            flags.update(x for x, on in ((g.MET, met), (g.CROWS_MOOTED, seed),
                         (g.MANU, manuscripts), ("irabeth_dead", irabeth), (g.KC_KEPT, rank)) if on)
            text = self.traverse(self.scenes[g.OFFER], flags)
            if not met:
                self.assertIn("I had another name ready", text)

    def test_source_returns_do_not_require_unrelated_open_relationships(self):
        for sid in (g.P + "return.kitrane", g.P + "return.kitrane_scarred",
                    g.P + "return.kitrane_stall", g.P + "return.kitrane_scarred_stall"):
            for service, cost in itertools.product((False, True), (None, g.ALONE, g.LATE_FOUND)):
                flags = {"iomedae.closed", "irabeth_dead", g.EULOGY_TRUE}
                if service:
                    flags.add(g.JOINED)
                if cost:
                    flags.add(cost)
                text = self.traverse(self.scenes[sid], flags)
                if not service:
                    self.assertNotIn("name I first wore in the war camp", text)
                    self.assertIn("name I chose for the escape", text)

    def test_unpaid_preparation_names_crows_supplies(self):
        text = self.traverse(self.scenes[g.P + "iz.alone"], {g.CROWS_MOOTED, g.KC_KEPT})
        self.assertIn("There was no purse for a hired surgeon", text)
        self.assertNotIn("boots stolen twice in the war camp", text)
        paid = self.traverse(self.scenes[g.P + "iz.alone"], {g.E_MOOTED, g.P + "standing_orders.paid"})
        self.assertNotIn("There was no purse", paid)

    def test_four_slots_resume_original_aftermaths_without_effects(self):
        directory = Path(__file__).parents[1] / "tools/route_packs/explicit_slots/galfrey"
        briefs = list(directory.glob("*.json"))
        self.assertEqual(4, len(briefs))
        for path in briefs:
            brief = json.loads(path.read_text(encoding="utf-8"))
            scene = self.scenes[brief["continuity"]["source_scene"]]
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            slot = nodes[brief["slot_id"]]
            self.assertEqual(brief["default_text"], slot["Text"])
            self.assertEqual(brief["slot_id"], nodes[brief["continuity"]["insert_after"]]["Choices"][0]["Next"])
            self.assertEqual(brief["continuity"]["resume_at"], slot["Choices"][0]["Next"])
            self.assertEqual([], slot["Choices"][0]["Set"])

    def test_tent_collects_deferred_kiss_and_returns_from_drill(self):
        for suffix in ("", "_stall"):
            scene = self.scenes[g.P + "visit.tent" + suffix]
            text = self.traverse(scene, {g.P + "kitrane.reel" + suffix + ".saved", k.CROWS_ORDER})
            self.assertIn("The fiddler cannot whistle here", text)
            self.assertIn("She comes back to the tent", text)
            self.assertIn("running the eel-girl", text)

    def test_dead_commander_keeps_her_independent_political_future(self):
        scene = self.scenes[g.P + "epilogue.widow"]
        paras = scene["Nodes"][0]["Paragraphs"]
        crowned = " ".join(p["Text"] for p in paras if g.CROWN in p["Requires"])
        retired = " ".join(p["Text"] for p in paras if g.FOREVER in p["Requires"])
        self.assertIn("answered the inquiry herself", crowned)
        self.assertIn("purse every Iz anniversary", retired)
        self.assertNotIn("Commander answered", crowned)

    def test_late_rescue_does_not_receive_preparation_credit(self):
        for suffix in ("", "_stall"):
            text = self.traverse(self.scenes[g.P + "kitrane.king" + suffix], {g.ALONE, g.LATE_FOUND})
            self.assertIn("In the chapel you offered", text)
            self.assertNotIn("standing orders left me", text)

    def test_living_waits_keep_the_four_day_trial(self):
        expected = {"alive.kitrane": 0, "alive.plan": 0, "alive.plan_report": 24,
                    "alive.trial": 0, "alive.trial_report": 96, "alive.oath": 0,
                    "alive.after_no": 48}
        self.assertEqual(expected, {name: self.scenes[g.P + name]["DelayHours"] for name in expected})
        scene = k.ALIVE_UNFINISHED
        self.assertNotIn(scene["Id"], self.scenes)
        self.assertIn(g.COMMITTED, scene["Forbids"])
        self.assertNotIn(g.COMMITTED, scene["Requires"])

    def test_disclosure_requires_irabeth_currently_present(self):
        scene = self.scenes[g.P + "kitrane.irabeth"]
        absent = self.traverse(scene, {g.CROWS_DREZEN})
        self.assertNotIn("Irabeth grips the edge", absent)
        present = self.traverse(scene, {g.CROWS_DREZEN, "irabeth.present_now"})
        self.assertIn("Irabeth grips the edge", present)

    def test_rescue_setup_and_release_agree_across_histories(self):
        prepared = self.traverse(self.scenes[g.BRIEFED_ID], set())
        self.assertIn("tries the folds himself", prepared)
        self.assertIn("Only if she commands it", prepared)
        offer = {n["Id"]: n for n in self.scenes[g.OFFER]["Nodes"]}
        self.assertIn("wind it around the crest", offer["read"]["Text"])
        self.assertIn("cannot find where to divide it", offer["blind"]["Text"])
        self.assertIn("Neither the dragon nor the priestess", offer["pitch"]["Text"])
        for suffix in ("", "_stall"):
            vigil = {n["Id"]: n for n in self.scenes[g.P + "iz.eulogy" + suffix]["Nodes"]}
            self.assertIn("unfolds the cloak", vigil["tent"]["Text"])
        for paid in (False, True):
            flags = {g.CROWS_MOOTED, g.KC_KEPT}
            if paid:
                flags.add(g.P + "standing_orders.paid")
            letter = self.traverse(self.scenes[g.P + "iz.alone"], flags)
            self.assertIn("instructions", letter)
            self.assertNotIn("I think it", letter)

    def test_late_recovery_is_performed_before_she_speaks(self):
        nodes = {n["Id"]: n for n in self.scenes[g.P + "iz.cortege"]["Nodes"]}
        self.assertIn("Salt has crusted", nodes["in"]["Text"])
        self.assertIn("wind it around her sword", nodes["in"]["Text"])
        for key in ("flare", "flare_told", "flare_told.unworn"):
            self.assertIn("pull your shadow across it", nodes[key]["Text"])
        self.assertIn("thread still joins", nodes["sergeant"]["Text"])
        self.assertIn("shadow slips away", nodes["rest"]["Text"])

    def test_private_restitution_does_not_require_reclaiming_crown(self):
        for suffix in ("", "_stall"):
            coffin = self.traverse(self.scenes[g.P + "kitrane.coffin" + suffix], set())
            self.assertIn("private petition", coffin)
            self.assertNotIn("only person", coffin)
            crown = self.traverse(self.scenes[g.P + "kitrane.crown" + suffix], {g.KEPT})
            self.assertIn("help her petition", crown)
        for ending in ("kitrane", "sworn", "late", "widow"):
            paragraphs = self.scenes[g.P + "epilogue." + ending]["Nodes"][0]["Paragraphs"]
            for paragraph in paragraphs:
                if g.FOREVER in paragraph["Requires"] and "purse" in paragraph["Text"]:
                    self.assertIn("signed by the surviving Crows", paragraph["Text"])


if __name__ == "__main__":
    unittest.main()

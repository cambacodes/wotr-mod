"""eng8-q8c / E-Q8-04: mapped age labels, speech boundaries and exact controls."""
import copy
import json
from pathlib import Path
import unittest
from tools import player_text_lint as player, text_structure_lint as structure, player_text_baseline as baseline
from tools.game_blueprints import game_dir

ROOT = Path(__file__).resolve().parents[1]


def payload(text, scene="fixture", location="start", **extra):
    return {"Scenes": [{"Id": scene, "Nodes": [{"Id": location, "Text": text, **extra}]}]}


class PlayerTextInventory2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = expansion.make_expansion()
        cls.surfaces = {(s, n): t for s, n, t, _, _ in player.surfaces(cls.story)}

    def test_all_four_mapped_age_labels_are_exact_visible_diagnostics(self):
        rows = player.check(self.story)["review"]
        mapped = (("arsinoe_borrowed_court", "start", "broad-shouldered adult woman"),
                  ("arsinoe_courtyard_company", "public", "young adult courier"),
                  ("arsinoe_courtyard_company", "private", "an adult courier"),
                  ("arsinoe_after_rain", "passage", "stocky adult woman"))
        for sid, loc, wording in mapped:
            with self.subTest(scene=sid, location=loc):
                text = self.surfaces[sid, loc]
                self.assertIn(wording, text)
                found = [r for r in rows if (r["scene"], r["location"], r["code"]) == (sid, loc, "age-certification")]
                self.assertEqual(len(found), 1)
                self.assertEqual(text[found[0]["start"]:found[0]["end"]], "adult")
                fixed = payload(text.replace("adult ", ""), sid, loc)
                self.assertFalse([r for r in player.check(fixed)["review"] if r["code"] == "age-certification"])
                # This diagnostic debt cannot permit a changed or extra label.
                changed = payload(text + " {n}An adult courier arrives.{/n}", sid, loc)
                self.assertTrue([r for r in baseline.new_findings(changed, player.check(changed)["review"])
                                 if r["code"] == "age-certification"])

    def test_missing_collection_closer_and_valid_controls(self):
        sid = "arsinoe.trickster.cauldron.collection"
        text = self.surfaces[sid, "start"]
        self.assertIn('I do not do that. So."\n', text)
        self.assertEqual(structure.spans(text), ([], []))
        broken = text.replace('I do not do that. So."\n', 'I do not do that. So.\n')
        rows = structure.check(payload(broken, sid), draft=True)["review"]
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["code"], "speech-boundary-review")
        self.assertTrue(row["draft"])
        self.assertTrue(row["match"].startswith('"The roads south'))
        for text in ('"First paragraph.\n"Second paragraph."',
                     '"First paragraph,\n"Second paragraph," {n}she says.{/n} "The last."',
                     '"Stay," {n}she says.{/n} "Here."',
                     '{n}A sign says "Road closed."{/n}\n"Keep walking."',
                     '“Stay.”\n{n}She waits.{/n}\n“Here.”'):
            self.assertEqual(structure.spans(text), ([], []), text)
        for text in ('"Stay.\n{n}She waits.{/n}\n"Here."',
                     '“Stay.\n{n}She waits.{/n}\n“Here.”'):
            self.assertTrue(structure.spans(text)[1], text)

    def test_reviewed_continuation_is_exact_not_a_blanket_exception(self):
        sid = "targona.the_unscheduled_door"
        text = self.surfaces[sid, "start"]
        self.assertFalse(structure.check(payload(text, sid))["review"])
        self.assertTrue(structure.check(payload(text + " ", sid))["review"])
        self.assertTrue(structure.check(payload(text, "different"))["review"])
        self.assertTrue(structure.check(payload(text, sid), exceptions={})["review"])

    def test_meaningful_age_distinctions_require_whole_surface_review(self):
        policy = json.loads(player.EXCEPTIONS.read_text())
        for exception in [e for e in policy["exceptions"] if e["code"] == "age-certification"]:
            story = payload(exception["text"], exception["scene"], exception["location"])
            self.assertFalse([r for r in player.check(story)["review"] if r["code"] == "age-certification"])
            changed = payload(exception["text"] + " {n}An adult courier arrives.{/n}", exception["scene"], exception["location"])
            self.assertTrue([r for r in player.check(changed)["review"] if r["code"] == "age-certification"])
            broken_policy = copy.deepcopy(policy)
            for e in broken_policy["exceptions"]:
                e.pop("reason", None)
            self.assertTrue([r for r in player.check(story, broken_policy)["review"] if r["code"] == "age-certification"])
        # Native Greybor dragon-age discussion; verify the exact localization
        # when installed, then review only this complete display surface.
        key = "351dcde6-b3d3-436d-b599-f7129acad809"
        path = game_dir() / "Wrath_Data/StreamingAssets/Localization/enGB.json"
        text = json.loads(path.read_text(encoding="utf-8"))["strings"][key]
        self.assertIn("A large adult female?", text)
        reviewed = {"exceptions": [dict(scene="native/Greybor/" + key, location="start", code="age-certification",
            match="adult", text=text, reason="An adult dragon, distinct from a young dragon, is a different paid quarry.")]}
        story = payload(text, "native/Greybor/" + key)
        self.assertFalse(player.check(story, reviewed)["review"])
        self.assertTrue(player.check(story, {})["review"])

    def test_native_romance_residue_remains_reported_on_every_surface_and_draft(self):
        rows = player.check(self.story)["review"]
        self.assertTrue(any(r["scene"] == "wenduag.lastcall.page" and r["location"] == "page/paragraph/3"
                            and r["code"] == "tooling-residue" for r in rows))
        text = "The native romance continues."
        story = payload(text, Choices=[{"Text": text}], Paragraphs=[{"Text": text}])
        story["Books"] = {"test": {"Text": text}}
        story["Journals"] = {"test": {"Text": text}}
        rows = [r for r in player.check(story, draft=True)["review"] if r["code"] == "tooling-residue"]
        self.assertEqual(len(rows), 5)
        self.assertEqual({r["location"] for r in rows}, {"start", "start/choice/0", "start/paragraph/0", "Text"})
        self.assertTrue(all(r["draft"] for r in rows))

    def test_age_diagnostics_cover_choices_paragraphs_books_journals_and_drafts(self):
        text = "An adult courier waits."
        story = payload(text, Choices=[{"Text": text}], Paragraphs=[{"Text": text}])
        story["Books"] = {"test": {"Text": text}}
        story["Journals"] = {"test": {"Text": text}}
        rows = [r for r in player.check(story, draft=True)["review"] if r["code"] == "age-certification"]
        self.assertEqual(len(rows), 5)
        self.assertTrue(all(r["draft"] and r["match"] == "adult" for r in rows))

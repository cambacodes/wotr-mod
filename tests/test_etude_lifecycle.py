"""E3 (18-ETUDE-BINDING-AUDIT): the native etude lifecycle gate in tools/etude_lifecycle.py and rrt_verify's reachability
model. A Playing-only Story.Etudes binding read where its etude cannot be Playing (a remote letter, another area, a
relationship or Derived use, a chapter after its ancestor's cascade, an audit "never_reads" ruling) is a HARD failure and
unreachable in the matrix; a latch, PermanentEtudes or a SeenCues binding is the fix."""
import copy
import json
from pathlib import Path
import sys
import unittest
from tests.story_fixture import fresh_story

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import etude_lifecycle as el  # noqa: E402
import rrt_verify as rv  # noqa: E402

IZ, DREZEN = "2ccc6731787b6ec41ab5adc13f1b9ce9", "2570015799edf594daf2f076f2f975d8"
G_AREA, G_CASCADE, G_NEVER, G_REVIEWED, G_HOLD = ("a" * 32, "c" * 32, "d" * 32, "e" * 32, "f" * 32)
TABLE = {
    G_AREA: dict(name="MonsterDead", traits=["area"], areas={IZ: "Iz"}, conditional=[], cascade_chapter=None),
    G_CASCADE: dict(name="ColyphyrHepzamirahDead", traits=["area", "cascade"], areas={"b" * 32: "ColyphyrDungeon"},
                    conditional=[], cascade_chapter=5),
    G_NEVER: dict(name="ArueshalaeRomance_Fail", traits=["event_cascade"], areas={}, conditional=[], cascade_chapter=None,
                  ruling="never_reads", note="warning etude"),
    G_REVIEWED: dict(name="FoolKingGone", traits=["area"], areas={DREZEN: "DrezenCapital"}, conditional=[],
                     cascade_chapter=None, ruling="reviewed", note="capital only"),
    G_HOLD: dict(name="Hold", traits=["hold"], areas={}, conditional=[], cascade_chapter=None),
}


def scene(id, requires=(), forbids=(), remote=False, areas=(), lists=False, chapters=(5,), choices=None):
    s = dict(Id=id, Title=id, Owner="Anevia", Relationship="x", MinChapter=min(chapters), MaxChapter=max(chapters),
             Chapters=list(chapters), Requires=list(requires), Forbids=list(forbids), Remote=remote, Areas=list(areas),
             Nodes=[dict(Id="start", Text="t", Choices=choices or [dict(Text="Continue", Set=["x.committed"])])])
    if lists:
        s["AnswerLists"] = ["1" * 32]
    return s


def story(*scenes, etudes=None, latches=None, permanent=(), derived=None, unavailable=()):
    return dict(Scenes=list(scenes), Etudes=dict(etudes or {}), Latches=dict(latches or {}), Derived=dict(derived or {}),
                PermanentEtudes=list(permanent),
                Relationships={"x": dict(Title="X", StartedFlag="x.started", ClosedFlag="x.closed", CommittedFlag="x.committed",
                                         UnavailableFlags=list(unavailable))})


def hard(st):
    return el.check(st, TABLE)[1]


class GateTests(unittest.TestCase):
    def test_area_key_in_remote_letter_is_hard(self):
        st = story(scene("letter", requires=["iz.monster_dead"], remote=True), etudes={"iz.monster_dead": G_AREA})
        self.assertEqual(len(hard(st)), 1)
        self.assertIn("area Iz", hard(st)[0])

    def test_area_key_in_another_area_and_in_derived_is_hard(self):
        st = story(scene("capital", requires=["iz.anemora_dead"], areas=[DREZEN]), etudes={"iz.anemora_dead": G_AREA},
                   derived={"ravener": [["iz.anemora_dead"]]})
        self.assertEqual(len(hard(st)), 2)

    def test_area_key_in_its_own_area_or_as_latch_source_is_ok(self):
        st = story(scene("inside", requires=["iz.monster_dead.live"], areas=[IZ]),
                   scene("letter", requires=["iz.monster_dead"], remote=True),
                   etudes={"iz.monster_dead.live": G_AREA}, latches={"iz.monster_dead": ["iz.monster_dead.live"]})
        self.assertEqual(hard(st), [])

    def test_native_list_without_areas_is_a_warning_only(self):
        st = story(scene("list", requires=["iz.monster_dead"], lists=True), etudes={"iz.monster_dead": G_AREA})
        rows, h, w = el.check(st, TABLE)
        self.assertEqual(h, [])
        self.assertEqual(len(w), 1)

    def test_cascade_key_after_its_chapter_needs_permanent(self):
        ghost = scene("ghost", requires=["hepzamirah.dead"], lists=True, chapters=(5,))
        self.assertEqual(len(hard(story(ghost, etudes={"hepzamirah.dead": G_CASCADE}))), 1)
        self.assertEqual(hard(story(ghost, etudes={"hepzamirah.dead": G_CASCADE}, permanent=["hepzamirah.dead"])), [])
        # Chapter 4, on a Colyphyr list: its own dungeon, before the cascade (area unproven -> warning, not hard).
        offer = scene("offer", forbids=["hepzamirah.dead"], lists=True, chapters=(4,))
        self.assertEqual(hard(story(offer, etudes={"hepzamirah.dead": G_CASCADE})), [])

    def test_never_reads_ruling_is_hard_anywhere(self):
        st = story(scene("chaplain", requires=["arueshalae.failed"], lists=True), etudes={"arueshalae.failed": G_NEVER})
        self.assertEqual(len(hard(st)), 1)

    def test_reviewed_and_hold_keys_pass(self):
        st = story(scene("king", forbids=["fool_king.gone"], remote=True), scene("any", requires=["hold"], remote=True),
                   etudes={"fool_king.gone": G_REVIEWED, "hold": G_HOLD}, unavailable=["fool_king.gone"])
        self.assertEqual(hard(st), [])

    def test_relationship_unavailable_flag_of_area_key_is_hard(self):
        st = story(scene("s", lists=True), etudes={"iz.monster_dead": G_AREA}, unavailable=["iz.monster_dead"])
        self.assertEqual(len(hard(st)), 1)

    def test_choice_gates_count(self):
        choices = [dict(Text="a", Requires=["iz.left_early"], Set=["x.committed"]), dict(Text="b", Forbids=["iz.left_early"])]
        st = story(scene("late", remote=True, choices=choices), etudes={"iz.left_early": G_AREA})
        self.assertEqual(len(hard(st)), 1)   # one use per scene, reported once


class ReachTests(unittest.TestCase):
    """rrt_verify's Reach treats an unreadable gate as impossible (Requires) or never forced (Forbids)."""

    def reach(self, st, true=()):
        model = rv.Model(st)
        model.lifecycle = TABLE
        return rv.Reach(model, rv.World("t", true=true))

    def test_remote_letter_on_area_key_is_unreachable_until_latched(self):
        before = story(scene("letter", requires=["iz.monster_dead"], remote=True), etudes={"iz.monster_dead": G_AREA})
        self.assertNotIn("letter", self.reach(before, true=["iz.monster_dead"]).reached)
        after = story(scene("letter", requires=["iz.monster_dead"], remote=True), etudes={"iz.monster_dead.live": G_AREA},
                      latches={"iz.monster_dead": ["iz.monster_dead.live"]})
        self.assertIn("letter", self.reach(after).reached)

    def test_permanent_cascade_key_reachable_in_chapter_five(self):
        ghost = scene("ghost", requires=["hepzamirah.dead"], lists=True, chapters=(5,))
        self.assertNotIn("ghost", self.reach(story(ghost, etudes={"hepzamirah.dead": G_CASCADE}), true=["hepzamirah.dead"]).reached)
        fixed = story(copy.deepcopy(ghost), etudes={"hepzamirah.dead": G_CASCADE}, permanent=["hepzamirah.dead"])
        self.assertIn("ghost", self.reach(fixed, true=["hepzamirah.dead"]).reached)

    def test_unreadable_forbid_is_never_forced(self):
        st = story(scene("letter", forbids=["iz.monster_dead"], remote=True), etudes={"iz.monster_dead": G_AREA})
        self.assertIn("letter", self.reach(st, true=["iz.monster_dead"]).reached)


class StoryTests(unittest.TestCase):
    """The shipped story: every audited binding is fixed and the checked-in table leaves no HARD use."""

    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.table = el.load()
        # Terendelev M21 first consumes this existing shared native binding.
        # The checked-in lifecycle row is coordinator-owned; classify only this
        # route's newly referenced etude from the supplied blueprints meanwhile.
        cls.delayed_guid = "50bab3193d6d41c390494ab755765f43"
        if cls.table is not None and cls.delayed_guid not in cls.table:
            from tools.game_blueprints import game_dir
            verified = el.build({"Etudes": {"storyteller.dead_delayed": cls.delayed_guid}}, game_dir())
            cls.table = dict(cls.table)
            cls.table[cls.delayed_guid] = verified[cls.delayed_guid]

    def test_table_present_and_no_hard_use(self):
        self.assertIsNotNone(self.table, "tools/etude-lifecycle.json missing: python tools/etude_lifecycle.py")
        rows, h, w = el.check(self.story, self.table)
        self.assertEqual(h, [])
        self.assertTrue(all(r["traits"] != ["unclassified"] for r in rows), [r["key"] for r in rows if r["traits"] == ["unclassified"]])

    def test_terendelev_delayed_usher_native_lifecycle(self):
        self.assertEqual(self.story["Etudes"]["storyteller.dead_delayed"], self.delayed_guid)
        entry = self.table[self.delayed_guid]
        self.assertEqual(entry["name"], "StorytellerDeadDelayed")
        self.assertEqual(entry["traits"], ["hold"])
        self.assertEqual(entry["chain"], ["StorytellerDeadDelayed", "Storyteller",
                                         "ImportantNPCs_fate", "WrathOfTheRighteous"])
        self.assertEqual(entry["areas"], {})
        self.assertEqual(entry["conditional"], [])
        self.assertIsNone(entry["cascade_chapter"])

    def test_minagho_freed_by_azata_is_classified(self):
        guid = "1d466fd4271fdc14ea1c077760c63ca5"
        entry = self.table[guid]
        self.assertEqual(entry["traits"], ["hold"])
        self.assertEqual(entry["name"], "MinaghoSetFreeByAzata")
        self.assertEqual(entry["chain"], ["MinaghoSetFreeByAzata", "Minagho", "ImportantNPCs_fate", "WrathOfTheRighteous"])
        self.assertEqual(entry["areas"], {})
        self.assertIsNone(entry["cascade_chapter"])
        # No area/chapter parent retires this release; the normal Playing reader remains valid outside the Abyss.
        st = story(scene("freed", requires=["minagho.freed_by_azata"], remote=True),
                   etudes={"minagho.freed_by_azata": guid})
        self.assertEqual(el.check(st, self.table)[1], [])

    def test_audited_bindings(self):
        s = self.story
        self.assertIn("hepzamirah.dead", s["PermanentEtudes"])
        self.assertEqual(s["Derived"]["iz.monster_dead"], [["iz.monster_dead.latched"]])
        self.assertEqual(s["Latches"]["iz.monster_dead.latched"], ["iz.monster_dead.live"])
        for key in ("iz.left_early", "iz.anemora_dead", "jannah.condemned", "soana.bear_dead"):
            self.assertEqual(s["Latches"][key], [key + ".live"], key)
            self.assertNotIn(key, s["Etudes"], key)
        for key in ("arueshalae.failed", "jannah.dead", "jannah.dead_known", "jannah.free", "jannah.prison"):
            self.assertIn(key, s["SeenCues"], key)
            self.assertNotIn(key, s["Etudes"], key)


if __name__ == "__main__":
    unittest.main()

"""Minimal synthetic regression fixtures for all six audit classes."""
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools import crossroute_lint as lint
from tools.crossroute_checks import (other_woman, commander_alive, location_staging,
                                    late_commitment, world_facts, left_trickster)
from tools.crossroute_checks.common import AND, OR, lit, Proof, blocks, verify


def relationship(name):
    return dict(StartedFlag=name + ".started", ClosedFlag=name + ".closed", CommittedFlag=name + ".committed",
                UnavailableFlags=[name + ".dead", name + ".departed", name + ".refused", "trickster.failed"],
                UnavailableOverrides={name + ".dead": name + ".returned"}, FailureFlags=[])


def fixture(text="{n}The fire burns.{/n}", epilogue=False):
    return dict(Relationships={"galfrey": relationship("galfrey"), "seelah": relationship("seelah")},
                Derived={"trickster.commander_back": [["earned_back"]]},
                Scenes=[dict(Id="galfrey.test", Relationship="galfrey", Owner="GalfreyEpilogue" if epilogue else "Galfrey",
                             Requires=[], Forbids=[], MinChapter=3, MaxChapter=3,
                             Nodes=[dict(Id="start", Speaker="Narrator", Text=text,
                                         Choices=[dict(Text="Continue")])])])


def run(module, story):
    model = verify.Model(copy.deepcopy(story))
    return module.check(model, list(blocks(model)), Proof(model))


class PresenceTests(unittest.TestCase):
    def test_devotion_does_not_stage_the_goddess_after_romance_closure(self):
        # eng7-f6c: keep Irabeth's unconditional faith without granting divine contact.
        for verb in ("pray", "prays", "prayed", "praying", "prayers"):
            s = fixture("{n}The paladin's words: %s to Iomedae.{/n}" % verb)
            s["Relationships"]["iomedae"] = relationship("iomedae")
            self.assertEqual(run(other_woman, s), [])
        for text in ("{n}She prayed to Iomedae. Iomedae stood beside her.{/n}",
                     "{n}Iomedae answers the prayer.{/n}",
                     "{n}She prayed to Iomedae's hand resting on her brow.{/n}"):
            s = fixture(text)
            s["Relationships"]["iomedae"] = relationship("iomedae")
            self.assertTrue(run(other_woman, s))
        s["Scenes"][0]["Nodes"][0].update(Speaker="Iomedae", Text="You prayed to Iomedae.")
        self.assertTrue(run(other_woman, s))

    def test_all_mentions_and_speaking_cues(self):
        s = fixture("{n}Seelah stands beside the hearth.{/n}")
        self.assertEqual({f["subject"] for f in run(other_woman, s)}, {"seelah", "seelah:physical"})
        s["Scenes"][0]["Nodes"][0].update(Speaker="Seelah", Text="A hard night.")
        self.assertEqual(len(run(other_woman, s)), 2)

    def test_guarded_household_participant(self):
        s = fixture("{n}Seelah joins you at the table.{/n}")
        s["Scenes"][0]["Participants"] = ["seelah"]
        self.assertEqual(run(other_woman, s), [])

    def test_named_guard_does_not_prove_physical_presence(self):
        s = fixture("{n}Seelah stands beside the hearth.{/n}")
        s["Derived"]["seelah.guard"] = [["ready"]]
        s["DerivedOpenRoutes"] = {"seelah.guard": ["seelah"]}
        s["Scenes"][0]["Requires"] = ["seelah.guard"]
        findings = run(other_woman, s)
        self.assertEqual([f["subject"] for f in findings], ["seelah:physical"])

    def test_scene_chapter_window_supplies_central_presence_input(self):
        s = fixture("{n}Seelah stands beside the hearth.{/n}")
        s["Derived"]["seelah.guard"] = [["chapter_one"], ["chapter_later"]]
        s["DerivedOpenRoutes"] = {"seelah.guard": ["seelah"]}
        s["Presences"] = {"seelah.presence": dict(Area="drezen", Requires=["seelah.guard"], MinChapter=3, MaxChapter=3)}
        s["Scenes"][0].update(Areas=["drezen"], Forbids=["seelah.closed", "seelah.dead", "seelah.departed", "seelah.refused", "trickster.failed"])
        self.assertEqual(run(other_woman, s), [])

    def test_matching_presence_and_earned_return(self):
        s = fixture("{n}Seelah stands beside the hearth.{/n}")
        s["Presences"] = {"seelah.presence": dict(Unit="unit", Area="drezen", Requires=["seelah.guard"], MinChapter=3, MaxChapter=3)}
        s["Derived"]["seelah.guard"] = [["ready"]]
        s["DerivedOpenRoutes"] = {"seelah.guard": ["seelah"]}
        s["Scenes"][0].update(Areas=["drezen"], Requires=["seelah.guard"])
        self.assertEqual(run(other_woman, s), [])
        # A latch on yesterday's guard cannot prove today's presence.
        s["Latches"] = {"seelah.was_here": ["seelah.guard"]}
        s["Scenes"][0]["Requires"] = ["seelah.was_here"]
        self.assertEqual(len(run(other_woman, s)), 2)

    def test_paragraph_and_all_incoming_paths(self):
        s = fixture()
        scene = s["Scenes"][0]
        s["Derived"]["seelah.guard"] = [["ready"]]
        s["DerivedOpenRoutes"] = {"seelah.guard": ["seelah"]}
        scene["Nodes"][0]["Paragraphs"] = [dict(Text="Seelah's letter lies on the desk.", Requires=["seelah.guard"])]
        self.assertEqual(run(other_woman, s), [])
        scene["Nodes"][0]["Choices"] = [dict(Text="Read", Requires=["seelah.guard"], Next="letter")]
        scene["Nodes"].append(dict(Id="letter", Text="Seelah's letter lies on the desk."))
        self.assertEqual(run(other_woman, s), [])
        scene["Nodes"][0]["Choices"].append(dict(Text="Skip ahead", Next="letter"))
        self.assertEqual(len(run(other_woman, s)), 1)

    def test_single_woman_seat_does_not_prove_other_woman_present(self):
        s = fixture("{n}Seelah stands beside the fire.{/n}")
        s["Relationships"]["pair"] = relationship("pair")
        s["Relationships"]["pair"]["UnavailableFlags"] = ["seelah.dead", "galfrey.dead"]
        s["SeatWomen"] = {"seelah": dict(Relationship="pair", UnavailableFlags=["seelah.dead"]),
                          "galfrey": dict(Relationship="pair", UnavailableFlags=["galfrey.dead"])}
        s["Scenes"][0].update(Relationship="household", Participants=["pair"], ParticipantWomen=["galfrey"])
        s["Relationships"]["household"] = relationship("household")
        # Synthetic pair seats are normally routes without independent ids.
        del s["Relationships"]["seelah"]
        del s["Relationships"]["galfrey"]
        self.assertEqual(len(run(other_woman, s)), 2)


class CommanderTests(unittest.TestCase):
    def test_unreturned_sacrifice_and_return(self):
        s = fixture("{n}You sit beside her after the war.{/n}", True)
        self.assertEqual(len(run(commander_alive, s)), 1)
        s["Scenes"][0].update(Forbids=["sacrifice"], ForbidOverrides={"sacrifice": "trickster.commander_back"})
        self.assertEqual(run(commander_alive, s), [])
        s["Scenes"][0]["ForbidOverrides"] = {"sacrifice": "unearned_guess"}
        self.assertEqual(len(run(commander_alive, s)), 1)

    def test_paragraph_guard_and_lastcall(self):
        s = fixture("", True)
        scene = s["Scenes"][0]
        scene["Nodes"][0]["Paragraphs"] = [dict(Text="{n}You sit beside her.{/n}", Forbids=["sacrifice"])]
        self.assertEqual(run(commander_alive, s), [])
        scene.update(Id="lastcall.visit", Owner="Galfrey")
        scene["Nodes"][0]["Paragraphs"][0]["Forbids"] = []
        self.assertEqual(len(run(commander_alive, s)), 1)


class LocationTests(unittest.TestCase):
    def test_drezen_window_at_wrong_area_and_chapter(self):
        s = fixture("{n}She stands at a window in Drezen's citadel.{/n}")
        scene = s["Scenes"][0]
        scene.update(Areas=["3538511f16d45f44f8249ff710777e2d"], MinChapter=5, MaxChapter=6)
        self.assertEqual(len(run(location_staging, s)), 1)
        scene.update(Areas=["2570015799edf594daf2f076f2f975d8"], MinChapter=5, MaxChapter=5)
        self.assertEqual(run(location_staging, s), [])

    def test_actual_setting_vs_recollection_destination(self):
        s = fixture("{n}She remembers the window in Drezen's citadel.{/n}")
        self.assertEqual(run(location_staging, s), [])
        s["Scenes"][0]["Nodes"][0]["Text"] = "{n}She will meet you in Drezen.{/n}"
        self.assertEqual(run(location_staging, s), [])

    def test_nexus_chapter_and_multiple_areas(self):
        s = fixture("{n}She waits in the Nexus camp.{/n}")
        s["Scenes"][0].update(Areas=["7847c3e3537104f4694167af0b9fcd0e"], MinChapter=4, MaxChapter=4)
        self.assertEqual(run(location_staging, s), [])
        s["Scenes"][0]["Areas"].append("wrong")
        self.assertEqual(len(run(location_staging, s)), 1)

    def test_explicit_authored_travel_and_mental_imagery(self):
        s = fixture("{n}It is like being searched. Drezen's walls, the war tables.{/n}")
        self.assertEqual(run(location_staging, s), [])
        s["Scenes"][0]["Nodes"] = [dict(Id="start", Text="{n}The room folds shut around you and opens again somewhere hot.{/n}",
                                       Choices=[dict(Text="Continue", Next="destination")]),
                                  dict(Id="destination", Text="{n}She stands in the chamber in Alushinyrra.{/n}")]
        self.assertEqual(run(location_staging, s), [])
        # A bypass that never took the authored journey cannot stage the chamber.
        s["Scenes"][0]["Nodes"].insert(0, dict(Id="entry", Text="Choose.", Choices=[dict(Text="Travel", Next="start"), dict(Text="Bypass", Next="destination")]))
        self.assertEqual(len(run(location_staging, s)), 1)


class CommitmentTests(unittest.TestCase):
    def test_epilogue_commitment_does_not_get_automatic_route_guard(self):
        s = fixture(epilogue=True)
        s["Scenes"][0]["Nodes"][0]["Choices"] = [dict(Text="Stay", Set=["galfrey.committed"])]
        self.assertEqual(len(run(late_commitment, s)), 1)
        s["Derived"]["galfrey.open"] = [["ready"]]
        s["DerivedOpenRoutes"] = {"galfrey.open": ["galfrey"]}
        s["Scenes"][0]["Requires"] = ["galfrey.open"]
        self.assertEqual(run(late_commitment, s), [])

    def test_foresight_page_is_not_a_route_eligibility_witness(self):
        s = fixture(epilogue=True)
        s["Derived"]["foresight.page_taken"] = [["trickster.now", "trickster.foresight.accepted"]]
        s["Scenes"][0]["Requires"] = ["foresight.page_taken"]
        s["Scenes"][0]["Nodes"][0]["Choices"] = [dict(Text="Commit", Set=["galfrey.committed"])]
        self.assertTrue(any(f["subject"] == "galfrey" for f in run(late_commitment, s)))

    def test_refusal_during_dialogue_invalidates_entry_guard(self):
        s = fixture()
        s["Scenes"][0]["Nodes"] = [dict(Id="start", Text="Choose.", Choices=[dict(Text="Refuse", Set=["galfrey.closed"], Next="late")]),
                                  dict(Id="late", Text="Choose again.", Choices=[dict(Text="Commit", Set=["galfrey.committed"])])]
        self.assertEqual(len(run(late_commitment, s)), 1)

    def test_unrelated_set_preserves_incoming_current_path_guard(self):
        s = fixture()
        s["Derived"]["trickster.now"] = [["trickster"]]
        s["DerivedForbids"] = {"trickster.now": ["trickster.failed"]}
        s["Scenes"][0]["Requires"] = ["trickster.ever"]
        s["Scenes"][0]["Nodes"] = [dict(Id="start", Text="Choose.", Choices=[dict(Text="Continue", Requires=["trickster.now"], Set=["unrelated"], Next="commit")]),
                                  dict(Id="commit", Text="Choose again.", Choices=[dict(Text="Commit", Set=["galfrey.committed"])])]
        self.assertEqual(run(late_commitment, s), [])

    def test_live_trickster_not_historical_latch(self):
        s = fixture()
        s["Scenes"][0]["Nodes"][0]["Choices"] = [dict(Text="Commit", Set=["galfrey.committed"])]
        s["Scenes"][0]["Requires"] = ["trickster.ever"]
        self.assertEqual([f["subject"] for f in run(late_commitment, s)], ["current-path"])
        s["Scenes"][0]["Requires"].append("trickster.now")
        self.assertEqual(run(late_commitment, s), [])

    def test_ordinary_reward_after_earned_return_needs_no_new_power(self):
        s = fixture("{n}You kiss her.{/n}")
        s["Scenes"][0]["Requires"] = ["trickster.ever"]
        self.assertEqual(run(late_commitment, s), [])

    def test_late_epilogue_yes_requires_current_power(self):
        s = fixture(epilogue=True)
        s["Scenes"][0].update(Id="galfrey.trickster.epilogue.commit", Requires=["trickster.ever"])
        self.assertTrue(any(f["subject"] == "current-path" for f in run(late_commitment, s)))

    def test_existing_refusal_and_control_repairs(self):
        for route, blocked, repaired in (("jannah", "jannah.trickster.declined", "jannah.trickster.chalk_circle.walked_in"),
                                          ("nenio", "nenio.trickster.tampered", "nenio.trickster.replicated")):
            s = fixture("{n}You kiss her.{/n}")
            s["Relationships"][route] = relationship(route)
            scene = s["Scenes"][0]
            scene.update(Relationship=route, Owner=route.title())
            # Independent producers establish the known vocabulary, not today's
            # eligibility. No route content or guard is invented by the lint.
            s["Scenes"].append(dict(Id="producer", Relationship=route, Owner=route.title(),
                                   Nodes=[dict(Id="start", Text="Choose.", Choices=[dict(Text="Fail", Set=[blocked]), dict(Text="Repair", Set=[repaired])])]))
            self.assertTrue(any(f["subject"] == "refusal/control" for f in run(late_commitment, s)))
            scene["Requires"] = [repaired]
            self.assertFalse(any(f["subject"] == "refusal/control" for f in run(late_commitment, s)))

    def test_earned_clean_commitment_with_no_later_contamination(self):
        s = fixture("{n}You kiss her.{/n}", True)
        s["Relationships"]["nenio"] = relationship("nenio")
        s["Scenes"][0].update(Relationship="nenio", Owner="NenioEpilogue", Requires=["nenio.committed"],
                              Forbids=["nenio.closed", "nenio.dead", "nenio.departed", "nenio.refused", "trickster.failed"])
        s["Scenes"].append(dict(Id="experiment", Relationship="nenio", Owner="Nenio", Forbids=["nenio.committed"],
                                Nodes=[dict(Id="start", Text="Experiment.", Choices=[dict(Text="Tamper", Set=["nenio.trickster.tampered"])])]))
        s["Scenes"].append(dict(Id="nenio.trickster.commit.replication", Relationship="nenio", Owner="Nenio", Nodes=[dict(Id="start", Text="Results.", Choices=[
            dict(Text="Clean", Forbids=["nenio.trickster.tampered"], Set=["nenio.committed"]),
            dict(Text="Replication", Set=["nenio.committed", "nenio.trickster.replicated"])])]))
        self.assertFalse(any(f["subject"] == "refusal/control" for f in run(late_commitment, s)))
        s["Scenes"][-2]["Forbids"] = []
        self.assertTrue(any(f["subject"] == "refusal/control" for f in run(late_commitment, s)))


class WorldFactTests(unittest.TestCase):
    def test_worldwound_closure_not_crossroads(self):
        s = fixture("{n}The Worldwound was closed.{/n}", True)
        s["Etudes"] = {"ending.wound_closed": "10cf0442f31a4796af8b28281f35e944", "ending.crossroads": "f7343e290a8d4ed887af8f04d1b3446b"}
        s["Scenes"][0]["Requires"] = ["ending.crossroads"]
        self.assertEqual(len(run(world_facts, s)), 1)
        s["Scenes"][0]["Requires"] = ["ending.wound_closed"]
        self.assertEqual(run(world_facts, s), [])

    def test_all_or_arms_must_establish_fact(self):
        s = fixture("{n}The Worldwound was closed.{/n}", True)
        s["Etudes"] = {"ending.wound_closed": "10cf0442f31a4796af8b28281f35e944"}
        s["Scenes"][0]["RequiresAnyGroups"] = [["ending.wound_closed", "unrelated"]]
        self.assertEqual(len(run(world_facts, s)), 1)
        s["Scenes"][0]["RequiresAnyGroups"] = [["ending.wound_closed"], ["unrelated"]]
        self.assertEqual(run(world_facts, s), [])

    def test_conditional_claim_and_paragraph_variant(self):
        s = fixture("If the Worldwound was closed, she could return.", True)
        self.assertEqual(run(world_facts, s), [])
        s["Etudes"] = {"closed_native": "10cf0442f31a4796af8b28281f35e944"}
        s["Scenes"][0]["Nodes"][0]["Paragraphs"] = [dict(Text="The Worldwound was closed.", Requires=["closed_native"])]
        self.assertEqual(run(world_facts, s), [])

    def test_later_negative_clause_does_not_hide_assertion(self):
        s = fixture("The Worldwound was closed; she never regretted it.", True)
        self.assertEqual(len(run(world_facts, s)), 1)

    def test_path_ascension_and_rebuilt_evidence(self):
        cases = [("You became a god.", "ascend_all", "07ad18ffb08145b69522f8eee0230857", "Etudes"),
                 ("The Commander is a demon.", "demon", "9a3739370f84b0b4196d0e4d326ea3a8", "Etudes"),
                 ("Kenabres was rebuilt.", "rebuilt_witness", "fc65929e0c9e4a9fa03309418c2d29bb", "SeenCues")]
        for text, key, guid, kind in cases:
            s = fixture(text, True)
            s[kind] = {key: guid}
            self.assertEqual(len(run(world_facts, s)), 1)
            s["Scenes"][0]["Requires"] = [key]
            self.assertEqual(run(world_facts, s), [])

    def test_native_finale_proves_path_but_historical_latch_does_not(self):
        s = fixture("You are a Trickster.", True)
        s["Etudes"] = {"ending.crossroads": "f7343e290a8d4ed887af8f04d1b3446b"}
        s["Scenes"][0]["Requires"] = ["trickster.ever"]
        self.assertEqual(len(run(world_facts, s)), 1)
        s["Scenes"][0]["Requires"] = ["ending.crossroads"]
        self.assertEqual(run(world_facts, s), [])


class LeftTricksterTests(unittest.TestCase):
    def test_reuse_t7_return_producer(self):
        s = fixture()
        s["Scenes"][0]["Requires"] = ["trickster.ever"]
        s["Scenes"][0]["Nodes"][0]["Choices"] = [dict(Text="Bring her back", Set=["galfrey.returned"])]
        findings = run(left_trickster, s)
        self.assertTrue(any(f["subject"] == "T7" and f["slot"] == "choice[0]" for f in findings))
        s["Scenes"][0]["Requires"].append("trickster.now")
        self.assertFalse(any(f["subject"] == "T7" for f in run(left_trickster, s)))

    def test_native_rewrite_when_and_variants(self):
        s = fixture(epilogue=True)
        s["NativeEpilogueEdits"] = {"native-cue": dict(Replacement="galfrey.test", When=[["trickster.ever"]],
                              Variants=[dict(Replacement="galfrey.test", When=[["trickster.now"]])])}
        self.assertTrue(any(f["subject"] == "native edit native-cue" for f in run(left_trickster, s)))
        s["NativeEpilogueEdits"]["native-cue"]["When"] = [["trickster.now"]]
        self.assertFalse(any(f["subject"] == "native edit native-cue" for f in run(left_trickster, s)))


class ReportingTests(unittest.TestCase):
    def test_strict_baseline_and_new_text(self):
        with tempfile.TemporaryDirectory(prefix="rrt-crossroute-") as tmp:
            story, baseline, report, text = [Path(tmp) / name for name in ("Story.json", "baseline.json", "report.json", "report.txt")]
            story.write_text(json.dumps(fixture("{n}Seelah stands by the fire.{/n}")), encoding="utf-8")
            args = ["--story", str(story), "--baseline", str(baseline), "--json", str(report), "--text", str(text)]
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(lint.main(args), 0)
                self.assertEqual(lint.main(args + ["--strict"]), 1)
                self.assertEqual(lint.main(args + ["--write-baseline"]), 0)
                self.assertEqual(lint.main(args + ["--strict"]), 0)
                data = json.loads(story.read_text(encoding="utf-8"))
                data["Scenes"][0]["Nodes"][0]["Text"] += " A different unguarded beat."
                story.write_text(json.dumps(data), encoding="utf-8")
                self.assertEqual(lint.main(args + ["--strict"]), 1)
            self.assertIn("L1", text.read_text(encoding="utf-8"))
            self.assertTrue(json.loads(report.read_text(encoding="utf-8"))["new_findings"])

    def test_deterministic_order_and_no_baseline_self_approval(self):
        s = fixture("Seelah's name is written on the page.")
        self.assertEqual(lint.check(copy.deepcopy(s)), lint.check(copy.deepcopy(s)))
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            lint.main(["--strict", "--write-baseline"])

    def test_cycles_and_latches_cannot_prove_live_power(self):
        s = fixture()
        s["Derived"].update(a=[["b"]], b=[["a", "trickster.now"]])
        s["Latches"] = {"past": ["trickster.now"]}
        m = verify.Model(s)
        proof = Proof(m)
        self.assertFalse(proof.implies(lit("a"), lit("trickster.now")))
        self.assertFalse(proof.implies(lit("past"), lit("trickster.now")))
        self.assertTrue(proof.implies(lit("trickster.now"), lit("past")))

    def test_live_retained_observer_not_historical_return(self):
        s = fixture()
        s["Revivals"] = {"konomi": dict(Relationship="konomi", DeathFlag="konomi.retained_dead")}
        s["Relationships"]["konomi"] = relationship("konomi")
        s["Latches"] = {"konomi.dead.latched": ["konomi.retained_dead"]}
        s["Derived"]["konomi.dead.unreturned"] = [["konomi.dead.latched"], ["konomi.death_unreturned"]]
        s["DerivedForbids"] = {"konomi.dead.unreturned": ["konomi.death_restored"]}
        m = verify.Model(s)
        proof = Proof(m)
        self.assertTrue(proof.implies(lit("konomi.dead.unreturned", False), lit("konomi.retained_dead", False)))
        self.assertFalse(proof.implies(lit("konomi.retained_return_confirmed"), lit("konomi.retained_dead", False)))


if __name__ == "__main__":
    unittest.main()

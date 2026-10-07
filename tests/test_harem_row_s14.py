"""S14's approved paths and fail-closed integration boundary, using Rules mirrors."""
import copy
import unittest

from storylines.harem_rows import s14
from storylines import contract_j01
from tools import rrt_verify as rules


class S14Tests(unittest.TestCase):
    def fixture(self, branch="good", returned=False, crown=False, retry=False):
        story = dict(Scenes=[], Etudes={}, Relationships={
            name: dict(StartedFlag=name + ".started", ClosedFlag=name + ".closed",
                       CommittedFlag=name + ".committed", UnavailableFlags=[])
            for name in ("household", *s14.PAIR)}, RestAllowances={"household.protected": 2})
        s14.register(story, story["Scenes"], story["Etudes"])
        story.update(Presences={"galfrey.presence": {"Unit": "11111111111111111111111111111111"},
                                "arueshalae.presence.evil": {"Unit": "22222222222222222222222222222222"}},
                     Revivals={"arueshalae": {"Unit": "33333333333333333333333333333333"}},
                     SeatWomen={}, DepartureEpochs={})
        contract_j01.install(story)
        model = rules.Model(story)
        sid = s14.P + ("retry." if retry else "settle.") + branch
        scene = next(s for s in model.scenes if s["Id"] == sid)
        state = rules.SimState(5, 100)
        state.flags.update(s14.COMMON)
        state.flags.discard(s14.ATTENDANCE)
        state.flags.update(("galfrey.present_now", "arueshalae.present_now"))
        state.available_contacts = {option["Units"][0] for contact in scene["ParticipantContacts"].values()
                                    for option in contact["Options"]}
        state.area = scene["Areas"][0]
        state.flags.add("arueshalae." + ("redeemed" if branch == "good" else "corrupted"))
        if returned:
            state.flags.add("galfrey.trickster.returned")
        if crown:
            state.flags.add("galfrey.trickster.crown_reclaimed")
        if retry:
            state.flags.update((s14.P + "settle.failed", s14.P + "failed." + branch))
            state.times[s14.P + "settle.failed"] = 52
        rules.sim_complete(model, state)
        return story, model, scene, state

    def test_registration_is_local_idempotent_and_only_derives_approved_stages(self):
        story, _, _, _ = self.fixture()
        before = copy.deepcopy(story)
        s14.register(story, story["Scenes"], story["Etudes"])
        self.assertEqual(before, story)
        self.assertEqual(len(story["Scenes"]), 4)
        for key, groups in s14.STAGES.items():
            self.assertEqual(story["Derived"][key], groups)
        self.assertFalse(any(key.endswith(".lover") for key in story["Derived"]))
        self.assertTrue({s14.ATTENDANCE, *s14.ENMITY, *s14.ENMITY.values()} <= set(story["PendingHooks"]))
        produced = {f for s in story["Scenes"] for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]}
        self.assertNotIn(s14.ATTENDANCE, produced)
        self.assertFalse(any(word in flag for flag in produced
                             for word in ("attitude", "enmity", "reconciled", "committed", "closed")))

    def test_missing_body_input_blocks_even_paid_committed_present_histories(self):
        _, model, scene, state = self.fixture()
        self.assertTrue(rules.sim_available(model, scene, state))
        self.assertNotIn(s14.ATTENDANCE, state.flags)
        state.available_contacts.clear()
        state.flags.add(s14.ATTENDANCE)  # A stale/manufactured flag cannot stand in for bodies.
        self.assertFalse(rules.sim_available(model, scene, state))

    def test_all_four_personality_title_combinations_and_reclaimed_crown(self):
        for branch in ("good", "evil"):
            for returned, crown in ((False, False), (True, False), (True, True)):
                with self.subTest(branch=branch, returned=returned, crown=crown):
                    _, model, scene, state = self.fixture(branch, returned, crown)
                    self.assertTrue(rules.sim_available(model, scene, state))
                    placed = next(n for n in scene["Nodes"] if n["Id"] == "placed")
                    available = [i for i, c in enumerate(placed["Choices"]) if rules.sim_choice_available(c, state)]
                    self.assertEqual(available, [1 if returned and not crown else 0])
                    for n in scene["Nodes"]:
                        self.assertTrue(any(rules.sim_choice_available(c, state) for c in n["Choices"]), n["Id"])

    def test_corruption_wins_and_unknown_selects_neither(self):
        _, model, good, state = self.fixture()
        evil = next(s for s in model.scenes if s["Id"] == s14.P + "settle.evil")
        state.flags.add("arueshalae.corrupted")
        rules.sim_complete(model, state)
        self.assertFalse(rules.sim_available(model, good, state))
        self.assertTrue(rules.sim_available(model, evil, state))
        state.flags.difference_update(("arueshalae.corrupted", "arueshalae.redeemed"))
        rules.sim_complete(model, state)
        self.assertFalse(rules.sim_available(model, good, state))
        self.assertFalse(rules.sim_available(model, evil, state))

    def test_every_step_rechecks_page_current_path_closure_and_later_loss(self):
        for branch in ("good", "evil"):
            for retry in (False, True):
                _, model, scene, state = self.fixture(branch, returned=True, retry=retry)
                for missing in s14.COMMON:
                    if missing == s14.ATTENDANCE:
                        continue
                    probe = copy.deepcopy(state)
                    probe.flags.remove(missing)
                    self.assertFalse(rules.sim_available(model, scene, probe), (scene["Id"], missing))
                for loss in s14.LOSSES:
                    probe = copy.deepcopy(state)
                    probe.flags.add(loss)
                    self.assertFalse(rules.sim_available(model, scene, probe), (scene["Id"], loss))
                for woman in s14.PAIR:
                    probe = copy.deepcopy(state)
                    probe.flags.add(woman + ".epoch_unavailable")
                    self.assertFalse(rules.sim_contact_available(model, scene, probe))
                for unit in ("11111111111111111111111111111111",
                             "33333333333333333333333333333333" if branch == "good"
                             else "22222222222222222222222222222222"):
                    probe = copy.deepcopy(state)
                    probe.available_contacts.remove(unit)
                    self.assertFalse(rules.sim_available(model, scene, probe))
                    for node in scene["Nodes"]:
                        self.assertFalse(rules.sim_contact_available(model, scene, probe), node["Id"])
                for chapter in (3, 4, 6):
                    probe = copy.deepcopy(state)
                    probe.chapter = chapter
                    self.assertFalse(rules.sim_available(model, scene, probe))

    def test_wrong_body_or_venue_cannot_supply_attendance(self):
        for branch in ("good", "evil"):
            for returned in (False, True):
                _, model, scene, state = self.fixture(branch, returned=returned)
                # Keep only the other Galfrey form and the other Arueshalae branch.
                state.available_contacts = {"8c5dcc93d68d0ed44afd43902201da40" if returned
                                            else "11111111111111111111111111111111",
                                            "22222222222222222222222222222222" if branch == "good"
                                            else "33333333333333333333333333333333"}
                self.assertFalse(rules.sim_available(model, scene, state))
                state.available_contacts.update(option["Units"][0] for contact in scene["ParticipantContacts"].values()
                                                for option in contact["Options"])
                state.area = "wrong venue"
                self.assertFalse(rules.sim_available(model, scene, state))

    def test_retry_uses_stamped_failure_not_ready_and_stays_personality_specific(self):
        _, model, scene, state = self.fixture(retry=True)
        for hour, available in ((99, False), (100, True)):
            state.hour = hour
            self.assertEqual(rules.sim_available(model, scene, state), available)
        state.flags.add(s14.P + "settle.done")
        self.assertFalse(rules.sim_available(model, scene, state))
        state.flags.remove(s14.P + "settle.done")
        state.flags.remove(s14.P + "failed.good")
        state.flags.add(s14.P + "failed.evil")
        self.assertFalse(rules.sim_available(model, scene, state))

    def test_enmity_uses_only_existing_matching_reconciliation(self):
        _, model, scene, state = self.fixture()
        for loss, override in s14.ENMITY.items():
            probe = copy.deepcopy(state)
            probe.flags.add(loss)
            self.assertFalse(rules.sim_available(model, scene, probe))
            probe.flags.add(override)
            self.assertTrue(rules.sim_available(model, scene, probe))
            probe.flags.add("galfrey.closed")
            self.assertFalse(rules.sim_available(model, scene, probe))

    def test_deed_stages_keep_asymmetry_and_matching_enmity_precedence(self):
        _, model, _, state = self.fixture()
        state.flags.update((s14.P + "settle.seen", *s14.DEEDS))
        stages = ("galfrey.harem.attitude.arueshalae.respect",
                  "arueshalae.harem.attitude.galfrey.friend")
        rules.sim_complete(model, state)
        self.assertTrue(all(stage in state.flags for stage in stages))
        self.assertNotIn("galfrey.harem.attitude.arueshalae.rival", state.flags)
        self.assertNotIn("arueshalae.harem.attitude.galfrey.respect", state.flags)
        self.assertFalse(any(flag.endswith(".lover") for flag in state.flags))
        for enmity, receipt in s14.ENMITY.items():
            probe = copy.deepcopy(state)
            probe.flags.add(enmity)
            rules.sim_complete(model, probe)
            self.assertFalse(any(stage in probe.flags for stage in stages))
            wrong = next(value for value in s14.ENMITY.values() if value != receipt)
            probe.flags.add(wrong)
            rules.sim_complete(model, probe)
            self.assertFalse(any(stage in probe.flags for stage in stages))
            probe.flags.add(receipt)
            rules.sim_complete(model, probe)
            self.assertTrue(all(stage in probe.flags for stage in stages))

    def test_exhaustive_terminals_indices_abort_and_protected_budget(self):
        for raw in s14.SCENES:
            retry = ".retry." in raw["Id"]
            branch = raw["Id"].rsplit(".", 1)[1]
            nodes = {n["Id"]: n for n in raw["Nodes"]}
            self.assertEqual([c["Next"] for c in nodes["start"]["Choices"]],
                             ["placed", "refused", None] if retry else ["placed", "unplaced", "refused", None])
            later = nodes["start"]["Choices"][-1]
            self.assertTrue(later["Abort"])
            self.assertEqual(later["Set"], [])
            expected = [s14.P + ("retry" if retry else "settle") + ".seen",
                        s14.P + ("retry" if retry else "settle") + ".done"]
            if retry:
                expected.append(s14.P + "settle.done")
            expected += [s14.P + "settle." + branch + "_done", *s14.DEEDS, s14.P + "cost.commander_placement"]
            self.assertTrue(all(c["Set"] == expected for c in nodes["placed"]["Choices"]))
            if not retry:
                self.assertEqual(nodes["unplaced"]["Choices"][0]["Set"],
                    [s14.P + "settle.seen", s14.P + "settle.failed", s14.P + "failed." + branch])
            self.assertEqual(nodes["refused"]["Choices"][0]["Set"],
                [raw["HouseholdWitness"], s14.P + ("retry" if retry else "settle") + ".refused", s14.P + "unsettled"])
            self.assertFalse(any(n.get("Paragraphs") for n in nodes.values()))
            self.assertFalse(any("explicit" in n for n in nodes))
            _, model, scene, state = self.fixture(branch, retry=retry)
            state.rest_spent["household.protected"] = 2
            self.assertFalse(rules.sim_available(model, scene, state))

    def test_prose_has_no_unwitnessed_fane_recall_or_fallen_redemption(self):
        for scene in s14.SCENES:
            text = " ".join(n["Text"] for n in scene["Nodes"])
            self.assertNotIn("Fane", text)
            if scene["Id"].endswith("evil"):
                for term in ("redemption", "Desna", "forgive", "grateful"):
                    self.assertNotIn(term, text)

    def test_terminal_reloads_cannot_replay_shared_wrapper_and_abort_spends_nothing(self):
        for branch in ("good", "evil"):
            for retry in (False, True):
                for returned in (False, True):
                    _, model, scene, state = self.fixture(branch, returned=returned, retry=retry)
                    state.flags.add("household.started")
                    before = copy.deepcopy(state.__dict__)
                    later = scene["Nodes"][0]["Choices"][-1]
                    self.assertFalse(rules.sim_play(model, scene, state, {}, plan=((), [later])))
                    self.assertEqual(before, state.__dict__)
                    nodes = {n["Id"]: n for n in scene["Nodes"]}
                    for destination in ("placed", "refused", *(("unplaced",) if not retry else ())):
                        loaded = copy.deepcopy(state)
                        entry = next(c for c in nodes["start"]["Choices"] if c["Next"] == destination)
                        terminal = next(c for c in nodes[destination]["Choices"]
                                        if rules.sim_choice_available(c, loaded))
                        self.assertTrue(rules.sim_play(model, scene, loaded, {}, plan=((), [entry, terminal])))
                        self.assertEqual(loaded.rest_spent, {"household.protected": 1})
                        self.assertEqual(loaded.times[scene["HouseholdWitness"]], loaded.hour)
                        saved = copy.deepcopy(loaded)
                        saved.rest_spent.clear()
                        saved.flags.discard(scene["Id"])
                        self.assertFalse(rules.sim_available(model, scene, saved))
                        twin = next(s for s in model.scenes if s["Id"] == scene["Id"].rsplit(".", 1)[0]
                                    + (".evil" if branch == "good" else ".good"))
                        self.assertFalse(rules.sim_available(model, twin, saved))


if __name__ == "__main__":
    unittest.main()

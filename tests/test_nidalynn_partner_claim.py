"""Nidalynn's preserved gates and earned histories (redesign T-CLASS/T-REPAIR).

Expected identities come from the approved truth artifact, never a fresh export.
Traversal uses the existing verifier's Rules mirrors, including payment receipts,
live derived readers, contact checks and the actual retry clock.
"""
import copy
import itertools
import json
from pathlib import Path
import unittest

from expansion import make_expansion
from storylines import lastcall_partners, nidalynn_trickster as route
from tests.story_fixture import fresh_story
from tools import rrt_verify as verify, savecompat


TRUTH = Path(__file__).resolve().parents[1] / "tools/route_packs/redesign/nidalynn/truth.json"
PAIR = "household.pair.nidalynn_devarra."
CHAPLAIN = [route.P + "chaplain_prayed", route.P + "chaplain_sent_away"]
DEPARTURE = {
    "wolves": {"trickster.ever", route.P + "goat.lie_kept"},
    "apart": {"trickster.ever", route.P + "met", route.CLOSED},
    "claimed": {"trickster.ever", route.P + "left_with_it"},
    "lie": {"trickster.ever", route.P + "lie_kept"},
    "given": {"trickster.ever", route.P + "given_to_the_crowd"},
}


def visible(block, flags):
    return (set(block.get("Requires", [])) <= flags
            and not set(block.get("Forbids", [])) & flags
            and all(set(group) & flags for group in block.get("AnyGroups", [])))


class NidalynnPartnerClaimTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.truth = json.loads(TRUTH.read_text(encoding="utf-8"))
        # Apply only the coordinator's explicit amendments to the frozen oracle.
        # unreturned still conflicts with the decision in the export: escalate
        # its containing-page gate rather than encode a new failing regression.
        for scene in cls.truth["scene_contracts"]:
            if scene["Id"] in {route.P + "epilogue." + e for e in DEPARTURE}:
                scene["Requires"] = [f for f in scene["Requires"] if f != "nidalynn.present_now"]
            if scene["Id"] == route.P + "kiln.the_chaplain":
                scene["Forbids"].insert(scene["Forbids"].index(CHAPLAIN[0]) + 1, CHAPLAIN[1])
                for node in scene["Nodes"]:
                    if node["Id"] in ("after_prayer", "leave", "end"):
                        node["Choices"][0]["Set"] = {"after_prayer": [CHAPLAIN[0]],
                            "leave": [CHAPLAIN[1]], "end": []}[node["Id"]]
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.model = verify.Model(cls.story)
        cls.contracts = {s["Id"]: s for s in cls.truth["scene_contracts"]}
        cls.appends = {s["scene"]: s for s in cls.truth["audit_append_acceptance"]}
        cls.families = {f["id"]: {c["id"]: c for c in f["cases"]}
                        for f in cls.truth["history_families"]}

    def assert_case(self, family, case, state):
        when = self.families[family][case]["when"]
        self.assertTrue(set(when["all"]) <= state.flags, (family, case))
        self.assertFalse(set(when["none"]) & state.flags, (family, case))

    def test_frozen_scene_reader_and_shared_producer_contracts(self):
        """B01-B28: preserve gates, ordered choices, effects and save IDs."""
        for expected in self.truth["scene_contracts"]:
            actual = self.scenes[expected["Id"]]
            with self.subTest(scene=expected["Id"]):
                for field, value in expected.items():
                    if field not in ("Nodes", "export_index", "Entry", "ReturnText"):
                        if expected["Id"] == route.P + "epilogue.unreturned" and field == "Requires":
                            # Containing presence/payoff conflict is escalated to fix15.
                            self.assertTrue({"trickster.ever", "sacrifice"} <= set(actual[field]))
                            continue
                        self.assertEqual(actual.get(field), value, field)
                self.assertEqual([n["Id"] for n in actual["Nodes"]],
                                 [n["Id"] for n in expected["Nodes"]])
            for node, frozen in zip(actual["Nodes"], expected["Nodes"]):
                with self.subTest(scene=expected["Id"], node=frozen["Id"]):
                    for field, value in frozen.items():
                        if field not in ("Choices", "Paragraphs", "text_sha256", "sayable_claims_source", "Text"):
                            self.assertEqual(node.get(field), value, field)
                    self.assertEqual(len(node["Choices"]), len(frozen["Choices"]))
                identities = savecompat.choice_identities(actual, node)
                for answer in frozen["Choices"]:
                    index = answer["index"]
                    with self.subTest(scene=expected["Id"], node=frozen["Id"], choice=index):
                        choice = node["Choices"][index]
                        for field, value in answer.items():
                            if field not in ("index", "save_identity", "Text"):
                                self.assertEqual(choice.get(field), value, field)
                        self.assertEqual(identities[index], answer["save_identity"])
                for paragraph in frozen["Paragraphs"]:
                    with self.subTest(scene=expected["Id"], node=frozen["Id"], paragraph=paragraph["index"]):
                        self.assert_predicate_present(node, paragraph)
        for section, entries in self.truth["reader_contracts"].items():
            for key, expected in entries.items():
                with self.subTest(reader=section, key=key):
                    self.assertEqual(self.story[section][key], expected)
        for expected in self.truth["read_only_pair_producers"]:
            actual = self.scenes[expected["Id"]]
            with self.subTest(producer=expected["Id"]):
                for field, value in expected.items():
                    if field != "transitions":
                        self.assertEqual(actual.get(field), value, field)
            nodes = {n["Id"]: n for n in actual["Nodes"]}
            for transition in expected["transitions"]:
                with self.subTest(producer=expected["Id"], node=transition["node"], choice=transition["index"]):
                    choice = nodes[transition["node"]]["Choices"][transition["index"]]
                    for field, value in transition.items():
                        if field not in ("node", "index"):
                            self.assertEqual(choice.get(field), value, field)

    def test_every_reveal_answer_records_the_disguise(self):
        reveal = self.scenes[route.P + "hearth.listening"]
        name = next(n for n in reveal["Nodes"] if n["Id"] == "name")
        self.assertEqual([c["Next"] for c in name["Choices"]], ["dragon", "belly", "second"])
        for choice in name["Choices"]:
            self.assertEqual(choice["Set"], [route.REVEALED, route.PARTNER_DISGUISE])

    def test_both_commitments_keep_the_existing_choices_and_record_history(self):
        expected = {
            route.P + "ridge.first_flight": ("offer", [route.COMMITTED, route.SALT, route.PROPOSED]),
            route.P + "kiln.the_heel": ("wait", [route.COMMITTED, route.SALT]),
        }
        actual = []
        for scene in self.story["Scenes"]:
            if scene.get("Relationship") != route.REL:
                continue
            for node in scene["Nodes"]:
                for index, choice in enumerate(node["Choices"]):
                    if route.COMMITTED not in choice.get("Set", []):
                        continue
                    actual.append(scene["Id"])
                    node_id, old_flags = expected[scene["Id"]]
                    self.assertEqual((node["Id"], index), (node_id, 0))
                    self.assertEqual(choice["Set"], [*old_flags, route.PARTNER_DISGUISE])
                    self.assertEqual(choice["Requires"], ["trickster.now"])
                    self.assertFalse(choice["Forbids"])
        self.assertCountEqual(actual, expected)

    def test_no_stance_or_eligibility_gate_for_a_fictional_bond(self):
        for scene in self.story["Scenes"]:
            if scene.get("Relationship") != route.REL and scene["Id"] != "nidalynn.lastcall.page":
                continue
            contexts = [scene, *scene["Nodes"]]
            contexts.extend(c for n in scene["Nodes"] for c in n["Choices"])
            contexts.extend(p for n in scene["Nodes"] for p in n.get("Paragraphs", []))
            for context in contexts:
                for field in ("Requires", "Forbids", "Set"):
                    flags = context.get(field, [])
                    self.assertFalse(any(f.startswith("nidalynn.partner_stance.") for f in flags))
                    if field != "Set":
                        self.assertNotIn(route.PARTNER_DISGUISE, flags)

    def assert_predicate_present(self, page, expected):
        """Find earned history by its gates, independently of prose placement."""
        fields = ("Requires", "Forbids", "AnyGroups")
        signature = {field: list(expected[field]) for field in fields}
        if signature["Requires"] == [CHAPLAIN[0]]:
            signature["Requires"] = []
            signature["AnyGroups"] = [CHAPLAIN]
            # Either recorded chaplain history suffices; neither grants memory.
            matches = [block for block in page.get("Paragraphs", [])
                       if block.get("AnyGroups") == [CHAPLAIN]]
            self.assertTrue(matches)
            for block in matches:
                for flag in CHAPLAIN:
                    self.assertTrue(visible(block, {flag}))
                self.assertFalse(visible(block, set()))
        self.assertIn(signature, [{field: block.get(field, []) for field in fields}
                                  for block in page.get("Paragraphs", [])])

    def test_all_nine_endings_keep_existing_paragraph_indices(self):
        """Every declared ending retains its history predicates and inert exit."""
        for ending in ("salt", "late", "heel", "wolves", "unreturned",
                       "apart", "claimed", "lie", "given"):
            scene = self.scenes[route.P + "epilogue." + ending]
            page = self.model.nodes[scene["Id"]]["page"]
            with self.subTest(ending=ending):
                self.assertIn("trickster.ever", scene["Requires"])
                frozen = self.contracts[scene["Id"]]["Nodes"][0]
                for paragraph in frozen["Paragraphs"]:
                    with self.subTest(requires=paragraph["Requires"]):
                        self.assert_predicate_present(page, paragraph)
                self.assertEqual([c["Next"] for c in page["Choices"]], [None])
                self.assertEqual([c["Set"] for c in page["Choices"]], [[]])
                if ending in DEPARTURE:
                    self.assertNotIn("nidalynn.present_now", scene["Requires"])
                    state = verify.SimState(6, 100)
                    state.flags.update(DEPARTURE[ending])
                    self.assertTrue(verify.sim_available(self.model, self.model.by_id[scene["Id"]], state))
                    for missing in DEPARTURE[ending]:
                        lost = copy.deepcopy(state)
                        lost.flags.discard(missing)
                        self.assertFalse(verify.sim_available(self.model, self.model.by_id[scene["Id"]], lost))
                if ending in ("apart", "wolves", "unreturned"):
                    for requires, forbids in (([route.KILN, route.HATCHED], []),
                                               ([route.KILN], [route.HATCHED])):
                        block = next(p for p in page["Paragraphs"]
                                     if p["Requires"] == requires and p["Forbids"] == forbids)
                        flags = set(requires)
                        self.assertTrue(visible(block, flags))
                        for missing in requires:
                            self.assertFalse(visible(block, flags - {missing}))
                        for blocker in forbids:
                            self.assertFalse(visible(block, flags | {blocker}))

    def test_frozen_prefixes_and_exact_appends(self):
        """All approved history predicates remain on their declared pages."""
        for contract in self.truth["audit_append_acceptance"]:
            page = self.model.nodes[contract["scene"]][contract["node"]]
            for kind in ("prefix", "appended"):
                for expected in contract[kind]:
                    with self.subTest(scene=contract["scene"], kind=kind,
                                      requires=expected["Requires"]):
                        self.assert_predicate_present(page, expected)

    def test_lastcall_conditional_history_and_unconditional_disguise(self):
        page = self.scenes["nidalynn.lastcall.page"]["Nodes"][0]
        self.assertEqual(page["Id"], "page")
        self.assertEqual(page["Paragraphs"][7]["Requires"],
                         ["lastcall.h2", "iomedae.trickster.buried_alive",
                          "crossroute.nidalynn.available"])
        self.assertEqual(page["Paragraphs"][7]["Forbids"], [])
        self.assertEqual(page["Paragraphs"][7]["AnyGroups"], [])
        for field in ("Requires", "Forbids", "AnyGroups"):
            self.assertFalse(page["Paragraphs"][8][field])

    def test_integration_and_repeated_assembly_are_idempotent(self):
        """T-IDEMP executes independently even when another test's count fails."""
        def partner():
            return copy.deepcopy(next(p for p in lastcall_partners.PARTNERS if p["rel"] == route.REL))
        payload = {"Presences": {}, "SeenCues": {}, "Derived": {}}
        route.integrate(payload)
        first, first_payload = partner(), copy.deepcopy(payload)
        route.integrate(payload)
        self.assertEqual(first, partner())
        self.assertEqual(first_payload, payload)
        for expected in self.truth["audit_append_acceptance"][-1]["prefix"][8:]:
            self.assertEqual(sum(p["Text"] == expected["Text"] for p in first["paragraphs"]), 1)
        def route_slice(story):
            return {s["Id"]: s for s in story["Scenes"]
                    if s["Id"] in self.contracts}
        first_story = route_slice(make_expansion())
        first_partner = partner()
        second_story = route_slice(make_expansion())
        self.assertEqual(first_story, second_story)
        self.assertEqual(first_partner, partner())

    def advance(self, state, hours):
        state.hour += hours
        state.rest_spent.clear()
        verify.sim_complete(self.model, state)

    def walk(self, state, sid, selections=None, failures=(), wait=True):
        """Choose indices from the frozen graph, then execute fresh exported answers.

        The shadow state chooses only compatible continuations. Check outcomes
        are supplied explicitly; the resulting path must follow the recorded
        success/failure target. No history flag is synthesized from prose.
        """
        scene = self.model.by_id[sid]
        if wait:
            self.advance(state, scene["DelayHours"])
        self.assertTrue(verify.sim_available(self.model, scene, state), sid)
        frozen = self.contracts.get(sid)
        if frozen:
            nodes = {n["Id"]: n for n in frozen["Nodes"]}
        else:
            producer = next(s for s in self.truth["read_only_pair_producers"] if s["Id"] == sid)
            nodes = {}
            for answer in producer["transitions"]:
                nodes.setdefault(answer["node"], {"Choices": []})["Choices"].append(answer)
        actual = {n["Id"]: n for n in scene["Nodes"]}
        flags, path = set(state.flags), []
        node_id = scene["Nodes"][0]["Id"]
        visited = set()
        while node_id is not None:
            self.assertNotIn(node_id, visited, (sid, node_id))
            visited.add(node_id)
            flags.update(nodes[node_id].get("EnterSet", []))
            candidates = nodes[node_id]["Choices"]
            selected = (selections or {}).get(node_id)
            if selected is None:
                selected = next(c["index"] for c in candidates
                                if set(c["Requires"]) <= flags and not set(c["Forbids"]) & flags)
            expected = candidates[selected]
            self.assertTrue(set(expected["Requires"]) <= flags, (sid, node_id, selected))
            self.assertFalse(set(expected["Forbids"]) & flags, (sid, node_id, selected))
            choice = actual[node_id]["Choices"][selected]
            path.append(choice)
            flags.update(expected["Set"])
            if expected["Abort"]:
                break
            if expected.get("Check"):
                result = "Failure" if node_id in failures else "Success"
                self.assertEqual(choice["Check"], expected["Check"])
                node_id = expected["Check"][result]
            else:
                node_id = expected.get("PostPayment") or expected["Next"]
        completed = verify.sim_play(self.model, scene, state, {}, plan=(None, path))
        verify.sim_complete(self.model, state)
        return completed

    def native_start(self, chapter=3):
        state = verify.SimState(chapter, 0)
        state.flags.update(("trickster", "chapter_later"))
        if chapter == 5:
            state.flags.add(route.CH5)
        presence = self.truth["reader_contracts"]["Presences"]["nidalynn.presence"]
        state.area = presence["Area"]
        state.available_contacts = {presence["Unit"]}
        state.crusade_resources = dict(Materials=1000, Favors=1000, Finances=1000)
        verify.sim_complete(self.model, state)
        return state

    def courtship(self, body="widow", entry="golems_kept", failed=False, late=False, delayed=False):
        """Reach hatched/renounced ch5 from a native entry, not a flag soup."""
        state = self.native_start(5 if late and entry != "golems_kept" else 3)
        if entry == "golems_kept":
            self.walk(state, route.P + "eggs.lamp_black", {"look": 0}, ("look",) if failed else ())
        else:
            native = "eggs.project" if entry == "vault_kept" else "eggs.druids"
            self.assertIn(native, self.truth["reader_contracts"]["Etudes"])
            verify.sim_record_flags([native], [], state)
            verify.sim_complete(self.model, state)
            suffix, check_node = ("eggs.vault", "vault") if entry == "vault_kept" else ("eggs.straw", "vault")
            self.walk(state, route.P + suffix, failures=(check_node,) if failed else ())
        self.assert_case("entry", entry, state)
        if late:
            state.chapter = 5
            state.flags.add(route.CH5)
        if route.HEARTH not in state.flags:
            self.walk(state, route.P + "hearth.grey_stone")
        self.walk(state, route.P + "steps.widow")
        self.walk(state, route.P + "hearth.listening")
        self.walk(state, route.P + "kiln.fire")
        before = state.crusade_resources["Favors"]
        self.walk(state, route.P + "kiln.hatching", {"her": 1 if delayed else
                  {"golems_kept": 0, "vault_kept": 3, "straw_kept": 4}[entry]})
        if delayed:
            self.assertEqual(state.crusade_resources["Favors"], before)
            self.walk(state, route.P + "kiln.truth_owed", {"salt": 0})
        self.assertEqual(state.crusade_resources["Favors"] - before, -150 if delayed else -100)
        self.walk(state, route.P + "kiln.whose", {"choose": 0})
        self.assert_case("custody", "renounced", state)
        state.chapter = 5
        state.flags.add(route.CH5)  # observed native Chapter05 etude
        if body == "chosen":
            self.choose_form(state)
        verify.sim_complete(self.model, state)
        return state

    def test_entry_care_truth_and_early_late_chronology_histories(self):
        """T-ENTRY/MEET/CARE/TRUTH/CHRONO use compatible native histories."""
        for entry, failed, late, delayed in itertools.product(
                ("golems_kept", "vault_kept", "straw_kept"), (False, True), (False, True), (False, True)):
            with self.subTest(entry=entry, failed=failed, late=late, delayed=delayed):
                state = self.courtship(entry=entry, failed=failed, late=late, delayed=delayed)
                self.assertEqual(route.PRIMED in state.flags, entry != "straw_kept")
                self.assertEqual(route.HAND in state.flags, entry == "golems_kept" and failed)
                self.assertEqual(route.PALMS in state.flags, entry == "vault_kept" and failed)
                self.assertEqual(route.CLERK in state.flags, entry == "vault_kept" and failed)
                self.assertEqual(route.QUARTERMASTER in state.flags, entry == "straw_kept" and failed)
                self.assertEqual(route.P + "met_before_abyss" in state.flags, not late)
                reunion = self.model.by_id[route.P + "door.home_from_the_dark"]
                self.advance(state, reunion["DelayHours"])
                self.assertEqual(verify.sim_available(self.model, reunion, state), not late)

    def test_entry_disposal_failed_alarm_and_unsaved_meeting_exclusions(self):
        for skill, failed, crush in itertools.product((0, 1), (False, True), (False, True)):
            with self.subTest(skill=skill, failed=failed, crush=crush):
                state = self.native_start()
                sid = route.P + "eggs.lamp_black"
                self.walk(state, sid, {"look": skill, "held": int(crush)}, ("look",) if failed else ())
                case = "golem_egg_crushed" if crush else "golems_kept"
                self.assert_case("entry", case, state)
                terminal = next(n for n in self.scenes[sid]["Nodes"]
                                if n["Id"] == ("crushed" if crush else "packed"))
                selected = [c for c in terminal["Choices"] if visible(c, state.flags)]
                self.assertEqual(len(selected), 1)
                self.assertEqual(selected[0].get("NativeNext"), route.GOLEM_ALARM if failed else None)
                self.advance(state, 24)
                self.assertEqual(verify.sim_available(self.model, self.model.by_id[route.P + "hearth.grey_stone"], state), not crush)
        for case in ("unprimed_omelet", "unprimed_destroyed", "rescue_not_taken"):
            with self.subTest(entry=case):
                state = self.native_start()
                state.flags.update(self.families["entry"][case]["when"]["all"])
                verify.sim_complete(self.model, state)
                self.assert_case("entry", case, state)
                for suffix in ("hearth.grey_stone", "steps.widow", "eggs.vault", "eggs.straw"):
                    self.assertFalse(verify.sim_available(self.model, self.model.by_id[route.P + suffix], state), suffix)

    def test_postponed_heel_refusal_and_current_path_keep_their_earned_gates(self):
        for answer in (0, 1, 2):
            with self.subTest(offer=answer):
                state = self.courtship("chosen")
                self.walk(state, route.P + "wall.wings")
                self.walk(state, route.P + "ridge.first_flight", {"offer": answer})
                state.chapter = 6
                verify.sim_complete(self.model, state)
                salt = self.model.by_id[route.P + "epilogue.salt"]
                late = self.model.by_id[route.P + "epilogue.late"]
                heel = self.model.by_id[route.P + "epilogue.heel"]
                self.assertEqual(verify.sim_available(self.model, salt, state), answer == 0)
                self.assertFalse(verify.sim_available(self.model, late, state))
                self.assertEqual(verify.sim_available(self.model, heel, state), answer == 1)
                if answer == 1:
                    state.chapter = 5
                    self.walk(state, route.P + "kiln.the_heel", {"wait": 0})
                    state.chapter = 6
                    verify.sim_complete(self.model, state)
                    self.assert_case("romance", "committed", state)
                    self.assertTrue(verify.sim_available(self.model, salt, state))
                    self.assertFalse(verify.sim_available(self.model, heel, state))
        state = self.ending_history(self.courtship("chosen"), "late")
        self.assertTrue(verify.sim_available(self.model, self.model.by_id[route.P + "epilogue.late"], state))
        state.flags.discard("trickster")
        state.flags.add("legend")
        verify.sim_complete(self.model, state)
        self.assertFalse(verify.sim_available(self.model, self.model.by_id[route.P + "epilogue.late"], state))

    def choose_form(self, state):
        self.walk(state, route.P + "door.own_form")
        state.available_contacts = {self.truth["reader_contracts"]["Presences"]["nidalynn.presence.chosen"]["Unit"]}
        self.assert_case("romance", "own_face_not_kissed", state)

    def initial_delivery(self, body, road):
        state = self.courtship(body)
        self.walk(state, PAIR + "notice." + body)
        before = state.crusade_resources["Materials"]
        index = dict(checked=0, hired=1, failed=0, refused=2)[road]
        self.walk(state, PAIR + "custody." + body, {"start": index},
                  ("start",) if road == "failed" else ())
        # A paid terminal completes before its PostPayment continuation aborts.
        self.assertIn(PAIR + "custody." + body, state.flags)
        self.assertEqual(state.crusade_resources["Materials"] - before, -100 if road == "hired" else 0)
        if road == "hired":
            scene = self.model.by_id[PAIR + "custody." + body]
            hire = next(n for n in scene["Nodes"] if n["Id"] == "hire")
            self.assertIn(verify.payment_key(scene, hire["Choices"][0]), state.flags)
        if road in ("failed", "refused"):
            self.assert_case("household_custody", "pair_" + road, state)
        else:
            self.assert_case("household_custody", "pair_paid_resolved", state)
        return state

    def ending_history(self, source, ending, called=True, late=False):
        state = copy.deepcopy(source)
        if route.FORM not in state.flags:
            self.choose_form(state)
        self.walk(state, route.P + "wall.wings")
        if ending != "late" and not late:
            self.walk(state, route.P + "ridge.first_flight", {"offer": 0})
            self.assert_case("romance", "committed", state)
        else:
            self.assert_case("romance", "kissed_late", state)
        if ending == "lastcall":
            state.chapter = 6
            # Native finale opens the existing Last Call; its call is actually played.
            state.flags.add("trickster.lastcall.open")
            if called:
                self.assertFalse(late, "The existing call requires eaten salt")
                self.walk(state, "nidalynn.lastcall.call", {"call": 0})
            state.flags.update(("trickster.lastcall.taken", "ending.trickster"))
        state.chapter = 6
        self.advance(state, 0)
        return state

    def custody_memory(self, state, ending):
        sid, index = (("nidalynn.lastcall.page", 12) if ending == "lastcall" else
                      (route.P + "epilogue." + ending, 26 if ending == "salt" else 22))
        return self.append_visible(state, sid, index)

    def append_visible(self, state, sid, index):
        """Render the containing page before matching an independently frozen claim."""
        scene = self.model.by_id[sid]
        if not verify.sim_available(self.model, scene, state):
            return False
        page = scene["Nodes"][0]
        rendered = [p["Text"] for p in page["Paragraphs"] if visible(p, state.flags)]
        expected = next(p for p in self.appends[sid]["appended"] if p["index"] == index)
        return expected["Text"] in rendered

    def test_paid_delivery_and_repair_histories_render_in_each_earned_page(self):
        """PA-01/02: four positives × both bodies × salt/late/LastCall."""
        for body, road in itertools.product(self.truth["paid_repair_acceptance"]["bodies"],
                                            ("checked", "hired", "failed", "refused")):
            with self.subTest(body=body, road=road):
                state = self.initial_delivery(body, road)
                if road in ("failed", "refused"):
                    repair = self.model.by_id[PAIR + "repair." + body]
                    self.assertFalse(verify.sim_available(self.model, repair, state))
                    self.advance(state, 47)
                    self.assertFalse(verify.sim_available(self.model, repair, state))
                    self.advance(state, 1)
                    before = state.crusade_resources["Materials"]
                    # PostPayment's exit aborts the dialogue after the paid
                    # terminal already published completion and its receipt.
                    self.walk(state, repair["Id"], {"start": 0}, wait=False)
                    self.assertIn(repair["Id"], state.flags)
                    self.assertEqual(state.crusade_resources["Materials"] - before, -150)
                    self.assertIn(verify.payment_key(repair, repair["Nodes"][0]["Choices"][0]), state.flags)
                    self.assert_case("household_custody", "pair_repaired_after_" + road, state)
                    self.assertIn(PAIR + "custody." + road, state.flags)
                    if road == "failed":
                        self.assertIn(PAIR + "cost.commander_feed_spilled", state.flags)
                    self.assertIn(PAIR + "repair.seen", state.flags)
                    self.assertFalse(verify.sim_available(self.model, repair, state))
                self.assert_case("household_custody", "pair_paid_resolved", state)
                for key in ("guardian_kept", "feed_delivered", "cost.commander_luxury_lost",
                            "cost.nidalynn_guard_night", "cost.nidalynn_own_feed"):
                    self.assertIn(PAIR + key, state.flags)
                self.assertEqual(PAIR + "cost.commander_delivery_paid" in state.flags, road != "checked")
                self.assertFalse(verify.sim_available(self.model, self.model.by_id[PAIR + "repair." + body], state))
                for ending in ("salt", "late", "lastcall"):
                    with self.subTest(body=body, road=road, ending=ending):
                        final = self.ending_history(state, ending)
                        self.assertTrue(self.custody_memory(final, ending))
                        # Creditor absence does not remove historical completed work.
                        final.flags.add("devarra.epoch_unavailable")
                        verify.sim_complete(self.model, final)
                        self.assertNotIn("devarra.present_now", final.flags)
                        self.assertTrue(self.custody_memory(final, ending))

    def test_incomplete_and_refused_repairs_never_earn_delivery_memory(self):
        for body, first, outcome in itertools.product(
                self.truth["paid_repair_acceptance"]["bodies"], ("failed", "refused"),
                ("unplayed", "eligible", "unaffordable", "later", "second_refusal")):
            with self.subTest(body=body, first=first, outcome=outcome):
                state = self.initial_delivery(body, first)
                repair = self.model.by_id[PAIR + "repair." + body]
                before = state.crusade_resources["Materials"]
                if outcome != "unplayed":
                    self.advance(state, 48)
                    self.assertTrue(verify.sim_available(self.model, repair, state))
                    if outcome == "unaffordable":
                        state.crusade_resources["Materials"] = before = 149
                        self.assertFalse(verify.sim_choice_available(repair["Nodes"][0]["Choices"][0], state))
                        self.assertFalse(self.walk(state, repair["Id"], {"start": 0}, wait=False))
                    elif outcome == "later":
                        self.assertFalse(self.walk(state, repair["Id"], {"start": 2}, wait=False))
                    elif outcome == "second_refusal":
                        self.assertTrue(self.walk(state, repair["Id"], {"start": 1}, wait=False))
                self.assertEqual(state.crusade_resources["Materials"], before)
                self.assertIn(PAIR + "custody." + first, state.flags)
                if first == "failed":
                    self.assertIn(PAIR + "cost.commander_feed_spilled", state.flags)
                self.assertNotIn(route.CLOSED, state.flags)
                for key in ("resolved", "feed_delivered", "cost.commander_delivery_paid",
                            "cost.commander_luxury_lost", "cost.nidalynn_guard_night", "cost.nidalynn_own_feed"):
                    self.assertNotIn(PAIR + key, state.flags)
                self.assertEqual(PAIR + "repair.seen" in state.flags, outcome == "second_refusal")
                if outcome == "second_refusal":
                    self.assert_case("household_custody", "pair_repair_refused", state)
                    self.assertIn(PAIR + "guardian_kept", state.flags)
                    self.assertIn(PAIR + "unanswered", state.flags)
                else:
                    self.assert_case("household_custody", "pair_repair_incomplete_after_" + first, state)
                for ending in ("salt", "late", "lastcall"):
                    final = self.ending_history(state, ending)
                    self.assertFalse(self.custody_memory(final, ending), ending)

    def test_paid_history_does_not_override_later_loss_closure_or_fatal_sacrifice(self):
        for body, first in itertools.product(self.truth["paid_repair_acceptance"]["bodies"], ("failed", "refused")):
            source = self.initial_delivery(body, first)
            self.walk(source, PAIR + "repair." + body, {"start": 0})
            for ending in ("salt", "late", "lastcall"):
                final = self.ending_history(source, ending)
                for family, case in (("actor_loss_override", "nidalynn_lost"),
                                     ("actor_loss_override", "nidalynn_actor_lost"),
                                     ("actor_loss_override", "own_route_closed"),
                                     ("custody", "left_with_youngster")):
                    with self.subTest(body=body, first=first, ending=ending, loss=case):
                        lost = copy.deepcopy(final)
                        # Documented negative modifier from truth; this is not a return recipe.
                        lost.flags.update(self.families[family][case]["when"]["all"])
                        verify.sim_complete(self.model, lost)
                        self.assert_case(family, case, lost)
                        self.assertFalse(self.custody_memory(lost, ending))
                        self.assertEqual(lost.crusade_resources, final.crusade_resources)
                        self.assertIn(PAIR + "custody." + first, lost.flags)
                        self.assert_case("household_custody", "pair_paid_resolved", lost)
                # Build sacrifice from native ending history, never active-only soup.
                with self.subTest(body=body, first=first, ending=ending, loss="sacrifice"):
                    dead = copy.deepcopy(final)
                    dead.flags.discard("ending.trickster")
                    dead.flags.update(("sacrifice", "ending.wound_closed"))
                    verify.sim_complete(self.model, dead)
                    self.assert_case("commander_and_finale", "fatal_unreturned", dead)
                    self.assertFalse(self.custody_memory(dead, ending))
                    dead.flags.discard("ending.wound_closed")
                    dead.flags.add("ending.trickster")
                    verify.sim_complete(self.model, dead)
                    self.assert_case("commander_and_finale", "commander_returned", dead)
                    self.assertTrue(self.custody_memory(dead, ending))

    def test_each_missing_custody_cost_hides_append_in_predicate_fixtures(self):
        """Isolated predicate negatives supplement, rather than replace, paid walks."""
        source = self.initial_delivery("chosen", "hired")
        costs = self.families["household_custody"]["pair_paid_resolved"]["when"]["all"]
        for ending, missing in itertools.product(("salt", "late", "lastcall"), costs):
            with self.subTest(ending=ending, missing=missing):
                final = self.ending_history(source, ending)
                self.assertTrue(self.custody_memory(final, ending))
                final.flags.remove(missing)
                verify.sim_complete(self.model, final)
                self.assertFalse(self.custody_memory(final, ending))

    def test_windstep_appends_require_carried_inspected_or_unanswered_history(self):
        """T-APPENDS siblings: actual notice/cell/inspection, in both bodies."""
        prefix = "household.pair.nidalynn_areelu."
        for body, outcome in itertools.product(self.truth["paid_repair_acceptance"]["bodies"],
                                               ("accounted", "pending", "unanswered", "none")):
            with self.subTest(body=body, outcome=outcome):
                state = self.courtship(body)
                if outcome != "none":
                    self.walk(state, prefix + "notice." + body,
                              {"start": 1 if outcome == "unanswered" else 0})
                if outcome == "accounted":
                    self.walk(state, prefix + "cell", {"start": 0})
                    self.assertNotIn(prefix + "accounted", state.flags)
                    self.walk(state, prefix + "receipt." + body, {"start": 0})
                self.assert_case("household_windstep", outcome, state)
                for ending in ("salt", "lastcall"):
                    final = self.ending_history(state, ending)
                    sid = "nidalynn.lastcall.page" if ending == "lastcall" else route.P + "epilogue.salt"
                    self.assertTrue(verify.sim_available(self.model, self.model.by_id[sid], final))
                    page = self.model.by_id[sid]["Nodes"][0]
                    # Indices are frozen in truth; no expected player prose is pinned here.
                    indices = {"accounted": 13, "unanswered": 14, "pending": 15} if ending == "lastcall" else {"accounted": 27}
                    for claim, index in indices.items():
                        with self.subTest(body=body, outcome=outcome, ending=ending, claim=claim):
                            block = page["Paragraphs"][index]
                            self.assertEqual(visible(block, final.flags), outcome == claim)
                            self.assertEqual(self.append_visible(final, sid, index), outcome == claim)
                            if outcome == claim:
                                # Isolated predicate fixtures: each required reader/cost
                                # is absent, without manufacturing an alternate traversal.
                                for missing in block["Requires"]:
                                    self.assertFalse(visible(block, final.flags - {missing}), missing)
                                for forbidden in block["Forbids"]:
                                    self.assertFalse(visible(block, final.flags | {forbidden}), forbidden)
                if outcome == "accounted":
                    final = self.ending_history(state, "lastcall")
                    final.flags.add("areelu.epoch_unavailable")
                    verify.sim_complete(self.model, final)
                    block = self.model.by_id["nidalynn.lastcall.page"]["Nodes"][0]["Paragraphs"][13]
                    self.assertFalse(visible(block, final.flags))
                    self.assertFalse(self.append_visible(final, "nidalynn.lastcall.page", 13))
                    self.assert_case("household_windstep", "accounted", final)

    def test_lastcall_named_refused_debt_is_history_not_a_creditor_cameo(self):
        """Compatible historical mother modifiers from truth, not presence grants."""
        state = self.ending_history(self.courtship("chosen"), "lastcall")
        page = self.model.by_id["nidalynn.lastcall.page"]["Nodes"][0]
        self.assertFalse(visible(page["Paragraphs"][11], state.flags))
        self.assert_case("devarra_debt_and_presence", "owed_not_named", state)
        for case in ("named_bill_uncalled", "mother_refused"):
            state.flags.update(self.families["devarra_debt_and_presence"][case]["when"]["all"])
        state.flags.add("devarra.epoch_unavailable")
        verify.sim_complete(self.model, state)
        self.assert_case("devarra_debt_and_presence", "named_bill_uncalled", state)
        self.assert_case("devarra_debt_and_presence", "mother_refused", state)
        self.assertNotIn("devarra.present_now", state.flags)
        block = page["Paragraphs"][11]
        self.assertTrue(visible(block, state.flags))
        self.assertTrue(self.append_visible(state, "nidalynn.lastcall.page", 11))
        self.assertFalse(visible(page["Paragraphs"][10], state.flags))
        for missing in block["Requires"]:
            with self.subTest(missing=missing):
                self.assertFalse(visible(block, state.flags - {missing}))

    def test_lastcall_called_uncalled_and_late_histories_keep_local_staging(self):
        """B27: earned salt enables the call; a late kiss enables only the page."""
        for body, called, late in itertools.product(
                self.truth["paid_repair_acceptance"]["bodies"], (False, True), (False, True)):
            if called and late:
                continue
            with self.subTest(body=body, called=called, late=late):
                source = self.initial_delivery(body, "hired")
                state = self.ending_history(source, "lastcall", called=called, late=late)
                self.assert_case("commander_and_finale", "lastcall_called" if called else "lastcall_uncalled", state)
                scene = self.model.by_id["nidalynn.lastcall.page"]
                self.assertTrue(verify.sim_available(self.model, scene, state))
                self.assertTrue(self.custody_memory(state, "lastcall"))
                page = scene["Nodes"][0]
                for index, shown in ((0, called), (9, not called and not late), (5, late)):
                    expected = self.appends[scene["Id"]]["prefix"][index]
                    rendered = [p["Text"] for p in page["Paragraphs"] if visible(p, state.flags)]
                    self.assertEqual(expected["Text"] in rendered, shown, index)
                if late:
                    call = self.model.by_id["nidalynn.lastcall.call"]
                    # Isolate the native before-taken window; missing salt still rejects it.
                    before_taken = copy.deepcopy(state)
                    before_taken.flags.discard("trickster.lastcall.taken")
                    verify.sim_complete(self.model, before_taken)
                    self.assertFalse(verify.sim_available(self.model, call, before_taken))

    def test_containing_pages_reject_each_missing_earned_history(self):
        """T-SALT/LATE/LASTCALL: negative predicate fixtures cannot grant a page."""
        source = self.initial_delivery("chosen", "hired")
        for ending in ("salt", "late", "lastcall"):
            final = self.ending_history(source, ending)
            scene = self.model.by_id["nidalynn.lastcall.page" if ending == "lastcall"
                                     else route.P + "epilogue." + ending]
            # Remove producer inputs, then recompute all live readers. Never remove a
            # derived output and treat that as a plausible alternative history.
            for missing in ("trickster", "trickster.ever", route.KISSED, route.HATCHED,
                            route.RENOUNCED, route.COMMITTED, route.SALT,
                            "trickster.lastcall.taken"):
                if ending in ("late", "lastcall") and missing in (route.HATCHED, route.RENOUNCED,
                                                                   route.COMMITTED, route.SALT):
                    continue  # Late eligibility is the existing earned kiss, not a new gate.
                if ending != "lastcall" and missing == "trickster.lastcall.taken":
                    continue
                if ending != "late" and missing == "trickster":
                    continue  # These existing historical consumers allow conversion.
                with self.subTest(ending=ending, missing=missing):
                    negative = copy.deepcopy(final)
                    negative.flags.discard(missing)
                    if missing == "trickster.ever":
                        negative.flags.discard("trickster")  # prevent the native latch restoring it
                    verify.sim_complete(self.model, negative)
                    self.assertFalse(verify.sim_available(self.model, scene, negative))
                    self.assertFalse(self.custody_memory(negative, ending))
            with self.subTest(ending=ending, revoker="proposal_refused"):
                negative = copy.deepcopy(final)
                negative.flags.update(self.families["romance"]["proposal_refused"]["when"]["all"])
                verify.sim_complete(self.model, negative)
                self.assertFalse(verify.sim_available(self.model, scene, negative))
                self.assertFalse(self.custody_memory(negative, ending))
            # The kept-wolves producer writes closure as well as its history.
            # Walk it after the earned kiss/salt, rather than inventing a lone
            # goat marker that never occurred in a shipped history.
            negative = copy.deepcopy(final)
            negative.chapter = 5
            self.walk(negative, route.P + "kiln.the_goat.chosen",
                      {"her": 2, "after_wolves": 2})
            self.assert_case("goat_consequence", "wolves_lie_kept", negative)
            self.assertIn(route.CLOSED, negative.flags)
            negative.chapter = 6
            verify.sim_complete(self.model, negative)
            with self.subTest(ending=ending, revoker="wolves_lie_kept"):
                self.assertFalse(verify.sim_available(self.model, scene, negative))
                self.assertFalse(self.custody_memory(negative, ending))
        # A missed rescue followed by native disposition provides no earned kiss
        # or commitment. Full native/derived readers reject every living page.
        for case in ("unprimed_omelet", "unprimed_destroyed", "rescue_not_taken"):
            state = self.native_start(5)
            state.flags.update(self.families["entry"][case]["when"]["all"])
            state.chapter = 6
            state.flags.update(("trickster.lastcall.taken", "ending.trickster"))
            verify.sim_complete(self.model, state)
            for ending in ("salt", "late", "lastcall"):
                with self.subTest(entry=case, ending=ending):
                    self.assertFalse(self.custody_memory(state, ending))

    def test_lastcall_buried_alive_memory_requires_all_three_facts(self):
        """T-LASTCALL prefix[7] is conditional; disguise prefix[8] is unconditional."""
        state = self.ending_history(self.courtship("chosen"), "lastcall")
        state.flags.discard("ending.trickster")
        state.flags.update(("ending.wound_closed", "sacrifice",
                            "trickster.lastcall.pillar.bottle"))
        # Independent predicate fixture for the other route's already-earned
        # appointment, using its frozen source inputs, not a derived flag grant.
        state.flags.update(self.truth["reader_contracts"]["Derived"]["iomedae.appointment_kept"][0])
        verify.sim_complete(self.model, state)
        self.assertIn("trickster.commander_back", state.flags)
        scene = self.model.by_id["nidalynn.lastcall.page"]
        self.assertTrue(verify.sim_available(self.model, scene, state))
        block = scene["Nodes"][0]["Paragraphs"][7]
        self.assertTrue(visible(block, state.flags))
        for missing in self.appends[scene["Id"]]["prefix"][7]["Requires"]:
            with self.subTest(missing=missing):
                self.assertFalse(visible(block, state.flags - {missing}))

    def test_historical_windstep_complaint_cannot_bypass_later_actor_loss(self):
        """History can stay true when its containing living page is unavailable."""
        prefix = "household.pair.nidalynn_areelu."
        state = self.courtship("chosen")
        self.walk(state, prefix + "notice.chosen", {"start": 1})
        final = self.ending_history(state, "lastcall")
        self.assertTrue(self.append_visible(final, "nidalynn.lastcall.page", 14))
        for case in ("nidalynn_lost", "nidalynn_actor_lost", "own_route_closed"):
            with self.subTest(loss=case):
                lost = copy.deepcopy(final)
                lost.flags.update(self.families["actor_loss_override"][case]["when"]["all"])
                verify.sim_complete(self.model, lost)
                self.assert_case("household_windstep", "unanswered", lost)
                block = self.model.by_id["nidalynn.lastcall.page"]["Nodes"][0]["Paragraphs"][14]
                self.assertTrue(visible(block, lost.flags))
                self.assertFalse(self.append_visible(lost, "nidalynn.lastcall.page", 14))


if __name__ == "__main__":
    unittest.main()

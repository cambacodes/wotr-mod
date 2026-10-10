"""J03 approval histories: earned deeds, current channels, pending failure.

Use the assembled export, including J01 live contacts and J02 first-wins
publication. Walk every selectable answer and both arms of each actual check.
"""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from tests.story_fixture import fresh_story
from tests.harem_row_walk import walk
from tools import rrt_verify as rules, savecompat


PAIRS = ("seelah_camellia", "arueshalae_nocticula", "horzalah_hepzamirah",
         "nocticula_shamira", "herrax_chivarro", "hepzamirah_minagho", "arsinoe_nurah")
ROOT = Path(__file__).resolve().parents[1]



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class J03Contracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.rows = [s for s in cls.model.scenes if any(
            s["Id"].startswith("household.pair." + pair + ".") for pair in PAIRS)]

    def state(self, body):
        state = rules.SimState(5, 1000)
        state.available_contacts = set()
        state.flags.update(body["Requires"])
        state.flags.add("trickster.now")
        for group in body["RequiresAnyGroups"]:
            state.flags.add(group[0])
        for route in body["Participants"]:
            eligible = route + ".harem.eligible"
            state.flags.add(eligible)
            state.flags.update(self.model.composites.get(eligible, [[]])[0])
        for woman in body["ParticipantWomen"]:
            state.flags.update(self.story["SeatWomen"][woman]["Requires"])
        for contact in body["ParticipantContacts"].values():
            state.flags.update(contact["Requires"])
            if contact["Kind"] == "body":
                option = next((option for option in contact["Options"]
                               if "arueshalae.corrupted" in option["Requires"]), contact["Options"][0]) \
                         if "arueshalae.corrupted" in state.flags else contact["Options"][0]
                state.flags.update(option["Requires"])
                state.available_contacts.add(option["Units"][0])
        state.times.update({key: -1000 for key in state.flags})
        return state

    def body(self, pair, suffix):
        return self.model.by_id["household.pair." + pair + "." + suffix]

    def test_all_selectable_paths_keep_an_answer_and_publish_only_complete_deeds(self):
        costs = {
            "seelah_camellia": ("seelah_blessing_withheld", "camellia_cover_limited"),
            "arueshalae_nocticula": ("arueshalae_renounced", "nocticula_rank_answered"),
            "horzalah_hepzamirah": ("horzalah_terms_kept", "hepzamirah_terms_kept"),
            "nocticula_shamira": ("nocticula_claim_answered", "shamira_title_answered"),
            "herrax_chivarro": ("herrax_turf_terms_kept", "chivarro_house_terms_kept"),
            "hepzamirah_minagho": ("minagho_screened", "hepzamirah_struck", "job_held"),
            "arsinoe_nurah": ("arsinoe_flaw_named", "nurah_author_named"),
        }
        for body in self.rows:
            with self.subTest(scene=body["Id"]):
                state = self.state(body)
                self.assertTrue(rules.sim_available(self.model, body, state))
                outcomes = walk(self, self.model, body, state)
                prefix = body["Id"].split(".")[2]
                p = "household.pair." + prefix + "."
                for end in outcomes:
                    if p + "resolved" in end.flags:
                        self.assertTrue({p + deed for deed in costs[prefix]} <= end.flags)
                        self.assertTrue(any(f.startswith(p + "cost.") for f in end.flags))
                    self.assertFalse(any(f.endswith(".returned") and f not in state.flags for f in end.flags))
                    self.assertNotIn("household.docket.horzalah_hepzamirah.captivity_remedy_delivered", end.flags)

    def test_each_retry_is_one_failure_clock_not_an_attendance_timestamp(self):
        sources = {
            "seelah_camellia": "settle.failed", "arueshalae_nocticula": "settle.failed",
            "horzalah_hepzamirah": "truce.failed", "herrax_chivarro": "turf.failed",
            "hepzamirah_minagho": "job.failed", "arsinoe_nurah": "audit.failed",
        }
        for body in self.rows:
            if ".retry" not in body["Id"]:
                continue
            with self.subTest(scene=body["Id"]):
                pair = body["Id"].split(".")[2]
                source = "household.pair." + pair + "." + sources[pair]
                state = self.state(body)
                self.assertEqual(body["DelayHours"], 48)
                state.times[source] = 0
                state.hour = 47
                self.assertFalse(rules.sim_available(self.model, body, state))
                state.hour = 48
                self.assertTrue(rules.sim_available(self.model, body, state))
                state.flags.remove(source)
                self.assertFalse(rules.sim_available(self.model, body, state))
                state.flags.add(source)
                state.flags.add(body["HouseholdWitness"])
                self.assertFalse(rules.sim_available(self.model, body, state))

    def test_page_path_closed_table_and_commander_loss_never_grant_progression(self):
        for body in self.rows:
            for gate in ("trickster", "foresight.page_taken", "household.table.kept"):
                with self.subTest(scene=body["Id"], gate=gate):
                    state = self.state(body)
                    state.flags.discard(gate)
                    self.assertFalse(rules.sim_available(self.model, body, state))
            state = self.state(body)
            state.flags.add("engine.l12.commander_unreturned")
            self.assertFalse(rules.sim_available(self.model, body, state))

    def test_live_contacts_are_rechecked_after_delay_and_before_terminal(self):
        for body in self.rows:
            for woman, contact in body["ParticipantContacts"].items():
                with self.subTest(scene=body["Id"], woman=woman):
                    state = self.state(body)
                    self.assertTrue(rules.sim_contact_available(self.model, body, state))
                    state.flags.add(woman + ".epoch_unavailable")
                    self.assertFalse(rules.sim_available(self.model, body, state))
                    self.assertFalse(rules.sim_contact_available(self.model, body, state))
                    state = self.state(body)
                    state.flags.discard(contact["Requires"][0])
                    self.assertFalse(rules.sim_contact_available(self.model, body, state))
                    if contact["Kind"] == "body":
                        state = self.state(body)
                        state.available_contacts.clear()
                        self.assertFalse(rules.sim_contact_available(self.model, body, state))

    def test_failure_then_success_has_no_synthesized_enmity_and_final_target_is_exact(self):
        policy = json.loads((ROOT / "tools/route_packs/plans/j02-policy.json").read_text(encoding="utf-8"))
        for rule in policy["failures"]:
            if rule["ruling"] not in (1, 2, 4, 18, 19, 20):
                continue
            bodies = [s for s in self.rows if s["Id"].startswith(rule["prefix"])]
            final_found = False
            for body in bodies:
                state = self.state(body)
                outcomes = walk(self, self.model, body, state)
                for end in outcomes:
                    if rule["prefix"] + "resolved" in end.flags:
                        self.assertFalse(any(".harem.enmity." in f for f in end.flags))
                    if set(rule["terminal"]) <= end.flags:
                        final_found = True
                        self.assertIn(rule["enmity"], end.flags)
                        self.assertNotIn(rule["enmity"].replace(".enmity.", ".reconciled."), end.flags)
                    if (any(f.endswith(".failed") for f in end.flags)
                            and not rule["prefix"] + "permanent_refusal" in end.flags):
                        self.assertFalse(any(".harem.enmity." in f for f in end.flags))
            self.assertTrue(final_found, rule)
            # A prior reconciled first target still occupies the historical slot.
            from storylines.harem_rows.zz_contract_controller import owner
            for body in bodies:
                state = self.state(body)
                state.flags.add(owner(rule["enmity"]))
                for end in walk(self, self.model, body, state):
                    self.assertNotIn(rule["enmity"], end.flags)

    def test_confession_is_retained_disclosed_evidence_not_native_inventory(self):
        body = self.body("seelah_camellia", "settle")
        p = "household.pair.seelah_camellia."
        root = body["Nodes"][0]["Choices"]
        state = self.state(body)
        self.assertFalse(rules.sim_choice_available(saved_answer(root, 1), state))
        self.assertFalse(rules.sim_choice_available(saved_answer(root, 5), state))
        state.flags.add("camellia.mireya_unmasked")
        self.assertTrue(rules.sim_choice_available(saved_answer(root, 5), state))
        self.assertFalse(rules.sim_choice_available(saved_answer(root, 1), state))
        record = saved_answer(next(n for n in body["Nodes"] if n["Id"] == "confession_record")["Choices"], 0)
        self.assertEqual(set(record["Set"]), {p + "confession_kept", p + "seelah_confession_heard"})
        state.flags.update(record["Set"])
        self.assertTrue(rules.sim_choice_available(saved_answer(root, 1), state))
        self.assertFalse(any(p in str(v) for v in self.story.get("InventoryItems", {}).values()))
        retry = self.body("seelah_camellia", "retry")
        self.assertFalse(rules.sim_choice_available(saved_answer(retry["Nodes"][0]["Choices"], 0), self.state(retry)))
        for step in (body, retry):
            word = saved_answer(step["Nodes"][0]["Choices"], 2)
            self.assertEqual(set(word["Set"]), {"trickster.wmt.use.seelah_camellia", "household.wmt.debt.seelah_camellia"})
            self.assertIn("trickster.wmt.available", word["Requires"])

    def test_seals_council_silence_captive_and_unknown_personality_remain_negative(self):
        for body in self.rows:
            if "arueshalae_nocticula" in body["Id"] or body["Id"].endswith("precedence.live"):
                state = self.state(body)
                state.flags.add("noct.acq.council_fight")
                self.assertFalse(rules.sim_contact_available(self.model, body, state))
                state = self.state(body)
                state.flags.discard("noct.acq.seal_received")
                self.assertFalse(rules.sim_available(self.model, body, state))
        live = self.body("nocticula_shamira", "precedence.live")
        state = self.state(live)
        state.flags.add("shamira.trickster.cost.kept_captive")
        self.assertFalse(rules.sim_contact_available(self.model, live, state))
        history = self.body("nocticula_shamira", "precedence")
        self.assertTrue(rules.sim_available(self.model, history, self.state(history)))
        for body in [s for s in self.rows if "arueshalae_nocticula" in s["Id"]]:
            state = self.state(body)
            state.flags.difference_update(["arueshalae.redeemed", "arueshalae.corrupted"])
            self.assertFalse(rules.sim_available(self.model, body, state))
            if body["Id"].endswith("redeemed"):
                state.flags.update(["arueshalae.redeemed", "arueshalae.corrupted"])
                self.assertFalse(rules.sim_available(self.model, body, state))
            for choice in body["Nodes"][0]["Choices"]:
                if "remaining Nocticula favour" in choice["Text"]:
                    self.assertFalse(rules.sim_choice_available(choice, self.state(body)))

    def test_s08_either_earned_correspondence_form_is_sufficient(self):
        channels = {"noct.acq.channel_provisional", "noct.acq.channel_letters_only"}
        for step in ("settle", "retry"):
            for branch in ("redeemed", "corrupted"):
                body = self.body("arueshalae_nocticula", step + "." + branch)
                self.assertEqual(body["RequiresAnyGroups"], [list(sorted(channels, reverse=True))])
                state = self.state(body)
                state.flags.difference_update(channels)
                self.assertFalse(rules.sim_available(self.model, body, state))
                for channel in channels:
                    state.flags.difference_update(channels)
                    state.flags.add(channel)
                    state.times[channel] = -1000
                    self.assertTrue(rules.sim_available(self.model, body, state), (body["Id"], channel))
                    self.assertTrue(rules.sim_contact_available(self.model, body, state), (body["Id"], channel))

    def test_s08_retry_roll_failure_is_owed_until_explicit_refusal(self):
        p = "household.pair.arueshalae_nocticula."
        for branch in ("redeemed", "corrupted"):
            body = self.body("arueshalae_nocticula", "retry." + branch)
            state = self.state(body)
            failed = next(n for n in body["Nodes"] if n["Id"] == "failed")
            pending, refuse = failed["Choices"]
            self.assertEqual(set(pending["Set"]), {p + "retry.seen", p + "unsettled"})
            state.flags.update(pending["Set"])
            rules.sim_complete(self.model, state)
            self.assertNotIn(p + "permanent_refusal", state.flags)
            self.assertNotIn("arueshalae.harem.enmity.nocticula", state.flags)
            self.assertFalse(rules.sim_available(self.model, body, state))
            self.assertEqual(refuse["Next"], "refused")
            final = saved_answer(next(n for n in body["Nodes"] if n["Id"] == "refused")["Choices"], 0)
            self.assertIn(p + "permanent_refusal", final["Set"])
            self.assertIn("arueshalae.harem.enmity.nocticula", final["Set"])

    def test_approved_dcs_and_retired_tools_do_not_add_payments(self):
        for pair, suffix, index, skill, dc in (
                ("seelah_camellia", "settle", 0, "SkillLoreReligion", 30),
                ("arueshalae_nocticula", "settle.redeemed", 0, "CheckDiplomacy", 37),
                ("arueshalae_nocticula", "settle.corrupted", 0, "CheckDiplomacy", 37),
                ("hepzamirah_minagho", "job", 1, "SkillThievery", 28)):
            check = saved_answer(self.body(pair, suffix)["Nodes"][0]["Choices"], index)["Check"]
            self.assertEqual((check["Skill"], check["DC"], check["CommanderOnly"]), (skill, dc, True))
        for body in self.rows:
            for node in body["Nodes"]:
                for choice in node["Choices"]:
                    self.assertFalse(choice.get("Crusade"), (body["Id"], node["Id"]))
        body = self.body("hepzamirah_minagho", "job")
        self.assertFalse(rules.sim_choice_available(saved_answer(body["Nodes"][0]["Choices"], 0), self.state(body)))

    def test_shared_incident_exhaustion_cannot_spend_again_through_a_wrapper(self):
        for pair, suffixes, witness in (
                ("arueshalae_nocticula", ("settle.redeemed", "settle.corrupted"), "settle.seen"),
                ("arueshalae_nocticula", ("retry.redeemed", "retry.corrupted"), "retry.seen"),
                ("nocticula_shamira", ("precedence", "precedence.live"), "precedence.seen"),
                ("herrax_chivarro", ("turf", "turf.history", "turf.live"), "turf.seen")):
            for suffix in suffixes:
                body = self.body(pair, suffix)
                state = self.state(body)
                state.flags.add("household.pair." + pair + "." + witness)
                self.assertFalse(rules.sim_available(self.model, body, state), body["Id"])

    def test_hepzamirah_ghost_and_hunt_absence_cannot_perform_either_job(self):
        from storylines import hepzamirah_trickster as hep
        for pair, primary in (("horzalah_hepzamirah", "truce"), ("hepzamirah_minagho", "job")):
            for suffix in (primary, "retry"):
                body = self.body(pair, suffix)
                state = self.state(body)
                state.available_contacts.remove(hep.BODY_UNIT)
                state.available_contacts.add(hep.GHOST_UNIT)
                state.flags.add(hep.P + "bond.the_hunt")
                self.assertFalse(rules.sim_available(self.model, body, state))
                self.assertFalse(rules.sim_contact_available(self.model, body, state))
                state.available_contacts.add(hep.BODY_UNIT)
                state.flags.add(hep.CONFINED)
                self.assertFalse(rules.sim_available(self.model, body, state))
                self.assertFalse(rules.sim_contact_available(self.model, body, state))
                state.flags.add(hep.RELEASED)
                self.assertTrue(rules.sim_available(self.model, body, state))
                self.assertTrue(rules.sim_contact_available(self.model, body, state))
                state.flags.add(hep.PRESENCE_FAILED)
                self.assertFalse(rules.sim_contact_available(self.model, body, state))

    def test_qualified_woman_does_not_require_her_absent_partner(self):
        for pair, suffix, absent in (
                ("hepzamirah_minagho", "job", "chivarro"),
                ("hepzamirah_minagho", "retry", "chivarro"),
                ("herrax_chivarro", "turf.live", "minagho"),
                ("herrax_chivarro", "retry", "minagho")):
            body = self.body(pair, suffix)
            state = self.state(body)
            state.flags.update([absent + ".dead", absent + ".epoch_unavailable"])
            state.flags.difference_update([absent + ".present_now", "participant." + absent + ".available"])
            self.assertTrue(rules.sim_available(self.model, body, state), body["Id"])
            self.assertTrue(rules.sim_contact_available(self.model, body, state), body["Id"])
            self.assertNotIn(absent, body["ParticipantContacts"])

    def test_s04_notes_follow_discovery_method_and_terminal_history(self):
        entries = self.story["Books"]["trickster.ledger"]["Entries"]
        old = next(e for e in entries if e["Id"] == "seating.seelah.camellia")
        self.assertIn("camellia.mireya_unmasked", old["Requires"])
        self.assertIn("household.pair.seelah_camellia.settle.seen", old["Forbids"])
        note = next(e for e in entries if e["Id"] == "seating.seelah_camellia.faith")
        p = "household.pair.seelah_camellia."
        self.assertEqual(note["Requires"], [p + "settle.seen"])
        for line in note["Lines"]:
            if p + "settle.failed" in line["Requires"]:
                self.assertEqual(set(line["Forbids"]), {p + "resolved", p + "permanent_refusal"})
            if p + "method.confession" in line["Requires"]:
                self.assertTrue({p + "confession_kept", p + "seelah_confession_heard"} <= set(line["Requires"]))
        self.assertFalse(any("present_now" in flag for flag in note["Requires"]))

    def test_s35_existing_lien_word_and_nonroll_retry_remain_exact(self):
        body = self.body("arsinoe_nurah", "audit")
        root = body["Nodes"][0]["Choices"]
        self.assertEqual(saved_answer(root, 0)["Check"], dict(Skill="SkillKnowledgeWorld", DC=30,
                         Success="audit_held", Failure="missed", CommanderOnly=True))
        self.assertIn("arsinoe.trickster.cost.lien", saved_answer(root, 1)["Requires"])
        self.assertFalse(saved_answer(root, 1).get("Crusade"))
        self.assertEqual(set(saved_answer(root, 2)["Set"]), {"trickster.wmt.use.arsinoe_nurah", "household.wmt.debt.arsinoe_nurah"})
        retry = self.body("arsinoe_nurah", "retry")
        self.assertFalse(any(c.get("Check") or c.get("Crusade") or c["Set"]
                             for c in retry["Nodes"][0]["Choices"]))

    def test_absent_herrax_leaves_only_the_earned_historical_account(self):
        history = self.body("herrax_chivarro", "turf.history")
        live = self.body("herrax_chivarro", "turf.live")
        state = self.state(history)
        state.flags.update(["herrax.closed", "herrax.epoch_unavailable", "crossroute.herrax.unavailable"])
        self.assertTrue(rules.sim_available(self.model, history, state))
        outcomes = walk(self, self.model, history, state)
        self.assertTrue(any("household.pair.herrax_chivarro.historical" in end.flags for end in outcomes))
        self.assertTrue(all("household.pair.herrax_chivarro.resolved" not in end.flags for end in outcomes))
        self.assertFalse(rules.sim_available(self.model, live, state))
        self.assertFalse(rules.sim_contact_available(self.model, live, state))

    def test_no_new_intimacy_echo_or_native_changes_and_pending_prose_is_tracked(self):
        rows = json.loads((ROOT / "tools/route_packs/plans/prose-pending.json").read_text(encoding="utf-8"))
        index = {(r["scene"], r.get("node")) for r in rows["pending"]}
        for body in self.rows:
            for node in body["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                self.assertNotIn("explicit", node["Id"])
                if node["Text"].startswith("[PROSE PENDING:"):
                    self.assertIn((body["Id"], node["Id"]), index)
        self.assertEqual(savecompat.check(self.story), [])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = self.body('seelah_camellia', 'settle')
        choice = next(n for n in scene['Nodes'] if n['Id'] == 'confession_record')['Choices'][0]
        with patch.dict(choice, Set=[]):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_confession_is_retained_disclosed_evidence_not_native_inventory()


if __name__ == "__main__":
    unittest.main()

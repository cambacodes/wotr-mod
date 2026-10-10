"""Round-2 debt, branch-exit and append-only checks on the authored route."""
import copy
import json
import unittest

from storylines import chivarro_setpieces as polish
from storylines import minagho_chivarro_continuation as continuation
from storylines import minagho_chivarro_stance as stance
from storylines import minagho_chivarro_trickster as trickster


class ChivarroSetpieceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = {"Scenes": copy.deepcopy(continuation.SCENES + trickster.SCENES)}
        stance.integrate(payload)
        cls.before = copy.deepcopy(payload)
        polish.integrate(payload)
        cls.pages = {page["Id"]: page for page in payload["Scenes"]}

    def nodes(self, suffix):
        return {node["Id"]: node for node in self.pages[polish.P + suffix]["Nodes"]}

    def test_merged_rounds_preserve_inserts_and_public_reckoning(self):
        from storylines import minagho_round2
        from storylines import lastcall_partners
        saved = copy.deepcopy(lastcall_partners.PARTNERS)
        try:
            payload = {"Scenes": copy.deepcopy(continuation.SCENES + trickster.SCENES)}
            stance.integrate(payload)
            minagho_round2.integrate(payload)
            before = copy.deepcopy(payload["Scenes"])
            polish.integrate(payload)
            pages = {page["Id"]: page for page in payload["Scenes"]}
            for original in before:
                revised = pages[original["Id"]]
                ids = [node["Id"] for node in revised["Nodes"]]
                self.assertEqual(len(ids), len(set(ids)))
                self.assertEqual([node["Id"] for node in original["Nodes"]],
                                 ids[:len(original["Nodes"])])
            page = pages[polish.P + "after.the_price_of_her_name_letter"]
            nodes = {node["Id"]: node for node in page["Nodes"]}
            self.assertEqual(nodes["start"]["Choices"][0]["Next"], "reckoning_receipt")
            self.assertEqual(nodes["reckoning_receipt"]["Choices"][0]["Next"], "verdict_paid")
            self.assertEqual(nodes["start"]["Choices"][0]["Set"], [])
            self.assertEqual(set(nodes["verdict_paid"]["Choices"][0]["Set"]),
                             {trickster.T_NAME, trickster.PALM_TABLE})
            clean = pages[polish.P + "alone.chivarro"]
            clean_nodes = {node["Id"]: node for node in clean["Nodes"]}
            insert = clean_nodes[clean_nodes["threshold_clean"]["Choices"][0]["Next"]]
            self.assertIn(".explicit.", insert["Id"])
            self.assertEqual(insert["Choices"][0]["Set"], [])
            self.assertIsNone(insert["Choices"][0]["Next"])
            wardrobe = pages[polish.P + "reunion.wardrobe"]
            wardrobe_nodes = {node["Id"]: node for node in wardrobe["Nodes"]}
            for identity in ("which", "which_debt"):
                for answer in wardrobe_nodes[identity]["Choices"]:
                    if polish.P + "chivarro_sent_back" in answer["Set"]:
                        self.assertEqual(answer["Next"], "departure_answer")
                    elif polish.P + "chivarro_in" in answer["Set"]:
                        self.assertNotIn(answer["Next"], ("departure_answer", "chivarro_leaves"))
            self.assertEqual(wardrobe_nodes["departure_answer"]["Choices"][0]["Next"], "chivarro_leaves")
        finally:
            lastcall_partners.PARTNERS[:] = saved

    def terminal(self, page, answer):
        nodes = {node["Id"]: node for node in page["Nodes"]}
        target = answer["Next"]
        seen = set()
        while target and ".explicit." in target:
            self.assertNotIn(target, seen, "insert loops instead of reaching aftermath")
            seen.add(target)
            choices = nodes[target]["Choices"]
            self.assertEqual(len(choices), 1)
            target = choices[0]["Next"]
        return target

    def test_saved_scene_node_order_and_choice_effects(self):
        for before in self.before["Scenes"]:
            after = self.pages[before["Id"]]
            self.assertEqual([x["Id"] for x in before["Nodes"]],
                             [x["Id"] for x in after["Nodes"][:len(before["Nodes"])]])
            for old, new in zip(before["Nodes"], after["Nodes"]):
                self.assertGreaterEqual(len(new["Choices"]), len(old["Choices"]))
                for index, answer in enumerate(old["Choices"]):
                    revised = new["Choices"][index]
                    if (before["Id"], old["Id"], index) == (polish.P + "after.the_price_of_her_name_letter", "start", 0):
                        self.assertEqual(revised["Set"], [])
                        self.assertEqual(self.nodes("after.the_price_of_her_name_letter")["verdict_paid"]["Choices"][0]["Set"], answer["Set"])
                    elif answer["Next"] is None and ".explicit." in (revised["Next"] or ""):
                        self.assertEqual(revised["Set"], [])
                        reached = {x["Id"]: x for x in after["Nodes"]}[revised["Next"]]
                        if reached["Choices"][0]["Next"] and reached["Choices"][0]["Next"].endswith(".after"):
                            reached = {x["Id"]: x for x in after["Nodes"]}[reached["Choices"][0]["Next"]]
                        self.assertEqual(reached["Choices"][0]["Set"], answer["Set"])
                    else:
                        self.assertEqual(answer["Set"], revised["Set"])
                    for key in ("Abort", "Revive", "Alignment", "StartEtude", "RemoveItem"):
                        self.assertEqual(answer.get(key), revised.get(key))

    def test_slots_do_not_merge_secret_discovery_exits_or_pay_twice(self):
        installed = 0
        for before in self.before["Scenes"]:
            after = self.pages[before["Id"]]
            for old, new in zip(before["Nodes"], after["Nodes"]):
                if not any(".explicit." in (a["Next"] or "") for a in new["Choices"]):
                    continue
                for answer, revised in zip(old["Choices"], new["Choices"]):
                    if len(new["Choices"]) == 1:
                        self.assertEqual(self.terminal(after, revised), answer["Next"])
                installed += 1
            for node in after["Nodes"]:
                if ".explicit." in node["Id"]:
                    for answer in node["Choices"]:
                        if answer["Next"] is not None:
                            self.assertEqual(answer["Set"], [])
                        self.assertNotIn("Crusade", answer)
        self.assertGreater(installed, 15)

    def test_epilogue_contract_paragraph_ordinals_stay_in_place(self):
        for before in self.before["Scenes"]:
            after = self.pages[before["Id"]]
            for old, new in zip(before["Nodes"], after["Nodes"]):
                original = old.get("Paragraphs", [])
                revised = new.get("Paragraphs", [])
                self.assertGreaterEqual(len(revised), len(original))
                for index, paragraph in enumerate(original):
                    for field in ("Requires", "Forbids", "AnyGroups"):
                        self.assertEqual(paragraph.get(field), revised[index].get(field))

    def test_earned_commitment_locks_out_conflicting_second_chain(self):
        continuation_pages = [page for page in self.pages.values()
                              if page["Id"].startswith("minachiv.")
                              and not page["Owner"].endswith("Epilogue")]
        self.assertTrue(continuation_pages)
        self.assertTrue(all(trickster.CHAIN in page["Forbids"] for page in continuation_pages))
        for suffix in ("after.before_the_last_road", "alone.chivarro", "alone.chivarro_letter"):
            self.assertIn(trickster.COMPLETE, self.pages[polish.P + suffix]["Forbids"])

    def test_letter_and_secret_dawn_pay_same_housing_rent_once(self):
        for suffix in ("alone.chivarro_letter", "alone.chivarro_morning"):
            nodes = self.nodes(suffix)
            paying = [a for node in nodes.values() if node["Id"] != "haggle"
                      for a in node["Choices"] if stance.P + "cost.morning_after" in a["Set"]]
            self.assertTrue(paying)
            self.assertTrue(all(a["Crusade"] == {"Resource": "Finances", "Amount": -100} for a in paying))
        nodes = self.nodes("alone.chivarro_when_it_scars")
        self.assertEqual(nodes["start"]["Choices"][0]["Crusade"]["Amount"] +
                         nodes["chv"]["Choices"][1]["Crusade"]["Amount"], 0)
        self.assertNotIn("Crusade", nodes["start"]["Choices"][1])

    def test_letter_rebuke_collects_actual_meeting_not_palm_print(self):
        nodes = self.nodes("after.the_price_of_her_name_letter")
        self.assertEqual(nodes["start"]["Choices"][0]["Next"], "verdict_paid")
        self.assertIn("closes your fingers herself", nodes["verdict_paid"]["Text"])
        self.assertIn("Minagho will be there", nodes["start"]["Text"])
        self.assertEqual(nodes["start"]["Choices"][0]["Set"], [])
        self.assertEqual(set(nodes["verdict_paid"]["Choices"][0]["Set"]),
                         {trickster.T_NAME, trickster.PALM_TABLE})

    def test_solo_clean_hand_stays_clean(self):
        text = self.nodes("alone.chivarro")["threshold_clean"]["Text"]
        self.assertNotIn("cut", text)
        self.assertNotIn("bleed", text)
        self.assertNotIn("scar", text)

    def test_installed_defaults_match_briefs_and_minagho_only_stays_owned(self):
        for path in polish.BRIEFS.glob("*.json"):
            brief = json.loads(path.read_text(encoding="utf-8"))
            sid = brief["slot_id"].split(".explicit.")[0]
            ids = {node["Id"]: node for node in self.pages[sid]["Nodes"]}
            ids.update({para["Id"]: para for node in self.pages[sid]["Nodes"]
                        for para in node.get("Paragraphs", []) if "Id" in para})
            sources = brief.get("source_nodes") or [brief["source"]["node"]]
            held = ".alone.minagho" in sid or all("minagho" in x for x in sources)
            if held:
                self.assertNotIn(brief["slot_id"], ids)
            else:
                self.assertEqual(ids[brief["slot_id"]]["Text"], brief["default_text"])


if __name__ == "__main__":
    unittest.main()

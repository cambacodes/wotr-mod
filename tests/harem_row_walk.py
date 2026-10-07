"""Walk every selectable row answer, including both check arms and full debits."""
import copy

from tools import rrt_verify as rules


def walk(test, model, scene, state):
    nodes = {node["Id"]: node for node in scene["Nodes"]}
    outcomes = []

    def visit(node_id, incoming, path):
        test.assertNotIn(node_id, path, (scene["Id"], path))
        node = nodes[node_id]
        current = copy.deepcopy(incoming)
        for flag in node.get("EnterSet", []):
            current.flags.add(flag)
            current.times.setdefault(flag, current.hour)
        choices = [c for c in node["Choices"] if rules.sim_choice_available(c, current)]
        # Main supplies an insufficient-funds abort when an otherwise selectable
        # paid answer is the only way out. Match Program.Walk's runtime exit.
        if not choices and any((c.get("Crusade") or {}).get("Amount", 0) < 0
                               for c in node["Choices"]):
            outcomes.append(current)
            return
        test.assertTrue(choices, (scene["Id"], node_id, current.crusade_resources))
        for answer in choices:
            state = copy.deepcopy(current)

            def publish():
                for flag in answer["Set"]:
                    state.flags.add(flag)
                    state.times.setdefault(flag, state.hour)
                if not answer["Abort"] and not answer["Next"] and not answer.get("Check"):
                    state.flags.add(scene["Id"])
                    state.times.setdefault(scene["Id"], state.hour)
                    allowance = scene.get("RestAllowance")
                    if allowance:
                        state.rest_spent[allowance] = state.rest_spent.get(allowance, 0) + 1

            if (answer.get("Crusade") or {}).get("Amount", 0) < 0:
                test.assertTrue(rules.sim_paid_choice(model, scene, answer, state, publish))
            else:
                publish()
            check = answer.get("Check")
            targets = [check["Success"], check["Failure"]] if check else [answer["Next"]]
            for target in targets:
                if target and not answer["Abort"]:
                    visit(target, state, (*path, node_id))
                else:
                    outcomes.append(copy.deepcopy(state))

    visit(scene["Nodes"][0]["Id"], state, ())
    return outcomes

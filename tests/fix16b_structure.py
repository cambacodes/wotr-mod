"""Graph assertions shared by the fix16b slot regression tests."""


def reachable_nodes(scene):
    """Follow declared transitions from entry, including both check outcomes."""
    nodes = {node['Id']: node for node in scene['Nodes']}
    pending = [scene['Nodes'][0]['Id']]
    reached = set()
    while pending:
        nid = pending.pop()
        if nid in reached:
            continue
        reached.add(nid)
        for choice in nodes[nid]['Choices']:
            if choice.get('Check'):
                pending.extend(choice['Check'][key] for key in ('Success', 'Failure'))
            elif choice.get('Next'):
                pending.append(choice['Next'])
    return reached


def declared_host(brief_id, brief, scenes):
    if 'host_scene' in brief:
        return brief['host_scene'], brief['host_node']
    # Reserved IDs survive scene moves; require one declared host for that ID.
    hosts = [scene['Id'] for scene in scenes.values()
             if any(node['Id'] == brief_id for node in scene['Nodes'])]
    if len(hosts) != 1:
        raise AssertionError((brief_id, 'expected one declared node host', hosts))
    return hosts[0], brief_id

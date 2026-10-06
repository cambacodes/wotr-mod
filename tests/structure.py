"""Test identities and save-shape comparisons, independent of localization."""


def without_prose(value):
    if isinstance(value, dict):
        return {key: without_prose(item) for key, item in value.items()
                if key not in {"Text", "Title", "Entry", "ReturnText", "Description", "Guidance"}}
    if isinstance(value, list):
        return [without_prose(item) for item in value]
    return value


def visible_slots(node, flags):
    """Paragraph positions are structural identities where no ID is exported."""
    result = {node["Id"]}
    for index, paragraph in enumerate(node.get("Paragraphs", [])):
        overrides = paragraph.get("ForbidOverrides", {})
        if (set(paragraph.get("Requires", [])) <= flags
                and all(flag not in flags or overrides.get(flag) in flags
                        for flag in paragraph.get("Forbids", []))
                and all(set(group) & flags for group in paragraph.get("AnyGroups", []))):
            result.add(node["Id"] + "/paragraph/" + str(index))
    return result

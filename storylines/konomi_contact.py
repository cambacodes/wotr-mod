"""Add observed native contact to audited ordinary Konomi meetings only."""

CONTACT = "ca2d58c5c65723945857e04fb85d30ce"
DREZEN = "2570015799edf594daf2f076f2f975d8"
ANSWERS = "0dc8b8604bb33c846a63f3eb62443674"
PHYSICAL_IDS = tuple("konomi." + name for name in (
    "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning",
    "return", "power", "ordinary", "farewell", "parting", "hearing", "hearing_after",
    "new_letter", "political_account", "a_useful_supper", "the_upper_passage",
    "two_bad_prices", "the_trial_day", "a_name_beside_hers", "the_evening_she_kept",
))


def integrate(payload):
    targets = []
    for id in PHYSICAL_IDS:
        matches = [item for item in payload["Scenes"] if item["Id"] == id]
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one ordinary Konomi scene: {id}")
        item = matches[0]
        if (item.get("Relationship") != "konomi" or item["Owner"] != "Konomi"
                or item.get("Remote", False) or item.get("ManualOnly", False)
                or "konomi.present" not in item["Requires"]
                or item.get("Areas") != [DREZEN] or item.get("AnswerLists") != [ANSWERS]
                or not item.get("Chapters") or not set(item["Chapters"]) <= {3, 5}
                or item.get("ContactUnit") not in (None, CONTACT)):
            raise ValueError(f"Konomi contact target no longer has its audited delivery contract: {id}")
        targets.append(item)
    # Validate every target before changing anything; repeated integration is harmless.
    for item in targets:
        item["ContactUnit"] = CONTACT

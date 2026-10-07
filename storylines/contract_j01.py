"""Approved J01 current contacts; authored metadata, no deeds or prose.

Body alternatives reuse the registered native actors and earned copies. Remote
respondents have an explicit channel and never qualify as bodily attendance.
This pass runs after the epoch registry, so later losses remain authoritative.
"""
from copy import deepcopy

from tools.departure_epochs import require

S14 = "household.pair.galfrey_arueshalae."
PRIVATE = ("household.pair.nidalynn_devarra.", "household.pair.nidalynn_areelu.")
REMOTE = {
    "household.pair.jerribeth_vellexia.": {"jerribeth": "letter", "vellexia": "letter"},
    "household.pair.iomedae_areelu.": {"iomedae": "banner", "areelu": "projection"},
}
S08 = "household.pair.arueshalae_nocticula."


def body_options(story, woman):
    if woman == "galfrey":
        return [dict(Units=["8c5dcc93d68d0ed44afd43902201da40"],
                     Requires=[], Forbids=["galfrey.trickster.returned"]),
                dict(Units=[story["Presences"]["galfrey.presence"]["Unit"]],
                     Requires=["galfrey.trickster.returned"], Forbids=[])]
    if woman == "arueshalae":
        return [dict(Units=[story["Revivals"][woman]["Unit"]],
                     Requires=["arueshalae.redeemed"], Forbids=["arueshalae.corrupted"]),
                dict(Units=list(dict.fromkeys(p["Unit"] for key, p in story["Presences"].items()
                                             if key.startswith("arueshalae.presence.evil"))),
                     Requires=["arueshalae.corrupted"], Forbids=[])]
    units = [p["Unit"] for key, p in story.get("Presences", {}).items()
             if (key.startswith(woman + ".presence")
                 or key.startswith("minagho_chivarro.presence." + woman))
             and key != "hepzamirah.presence.ghost"]
    if woman in story.get("Revivals", {}):
        units.append(story["Revivals"][woman]["Unit"])
    if woman == "arsinoe":
        units.append("a609ed9b2205d034bb3bb04d2a255681")
    return [dict(Units=list(dict.fromkeys(units)), Requires=[], Forbids=[])] if units else []


def install(story):
    """Qualify only declared participants; never infer a guest from a mention."""
    arue = story.get("SeatWomen", {}).get("arueshalae")
    if arue:
        # S03a retains this gate on its own scene. It proves native recruitment
        # for that good-branch row, not every later branch/copy's bodily presence.
        arue["Requires"] = [key for key in arue["Requires"]
                            if key != "household.pair.seelah_arueshalae.arueshalae_body"]
    for scene in story["Scenes"]:
        private = scene["Id"].startswith(PRIVATE)
        table = scene.get("InteractionHub") == "household.table"
        if not private and not table:
            continue
        if private:
            scene["PrivateParticipants"] = True
            require(scene, "trickster.now")
            scene["Forbids"] = list(dict.fromkeys([*scene["Forbids"], "engine.l12.commander_unreturned"]))
        contacts = scene.setdefault("ParticipantContacts", {})
        remote = next((kinds for prefix, kinds in REMOTE.items() if scene["Id"].startswith(prefix)), {})
        for route in scene.get("Participants", []):
            named = [w for w in scene.get("ParticipantWomen", [])
                     if story["SeatWomen"][w]["Relationship"] == route]
            women = named or (["anevia", "irabeth"] if route == "tirabade" else
                             ["minagho", "chivarro"] if route == "minagho_chivarro" else [route])
            for woman in women:
                supplied = contacts.get(woman, {})
                kind = supplied.get("Kind", "projection" if private and woman == "areelu" else remote.get(woman, "body"))
                key = woman + (".reachable_by_letter" if kind == "letter" else ".present_now")
                spec = dict(Kind=kind, Requires=[key], Forbids=[woman + ".epoch_unavailable",
                                                            woman + ".returned_actor_lost"], Options=[])
                if private and story["Relationships"][route]["ClosedFlag"] in scene["Forbids"]:
                    spec["Forbids"].append(story["Relationships"][route]["ClosedFlag"])
                if kind == "body":
                    spec["Options"] = body_options(story, woman)
                    # Delamere's route deliberately has no living actor blueprint.
                    # Keep this body requirement fail-closed; J10 must resolve the
                    # existing presentation contract without spawning her undead unit.
                elif kind == "projection":
                    spec["Requires"].extend(["areelu.trickster.lens_held"] if table else [])
                    if private:
                        spec["Forbids"].append("household.pair.nidalynn_areelu.projector_broken")
                elif kind == "banner":
                    spec["Requires"].append("iomedae.trickster.first_spoken")
                # Later owning jobs may declare a more specific current channel
                # or body window. Keep that declaration and its earned guards.
                if supplied:
                    spec["Requires"] = list(dict.fromkeys([*spec["Requires"], *supplied.get("Requires", [])]))
                    spec["Forbids"] = list(dict.fromkeys([*spec["Forbids"], *supplied.get("Forbids", [])]))
                    spec["Options"] = deepcopy(supplied.get("Options", spec["Options"]))
                contacts[woman] = spec
                if kind == "body" and woman not in story.get("SeatWomen", {}):
                    epoch = story["DepartureEpochs"].get(woman, {})
                    story.setdefault("SeatWomen", {})[woman] = dict(Relationship=route, Requires=[key],
                        UnavailableFlags=list(dict.fromkeys([*epoch.get("Losses", []), woman + ".epoch_unavailable"])),
                        UnavailableOverrides=deepcopy(epoch.get("Overrides", {})))
                if (kind == "body" and story["SeatWomen"][woman]["Relationship"] == route
                        and woman not in scene.setdefault("ParticipantWomen", [])):
                    scene["ParticipantWomen"].append(woman)
                if kind == "body":
                    # Reuse the individual's registered return for exactly the
                    # losses it answers. Latest epochs still defeat an old return;
                    # explicit kills, closures and other losses get no exception.
                    overrides = story["DepartureEpochs"].get(woman, {}).get("Overrides", {})
                    seat = story["SeatWomen"][woman]
                    for loss, returned in overrides.items():
                        if loss in seat["UnavailableFlags"]:
                            seat.setdefault("UnavailableOverrides", {}).setdefault(loss, returned)
                        if scene["Id"].startswith(S14) and loss in scene["Forbids"]:
                            scene.setdefault("ForbidOverrides", {}).setdefault(loss, returned)
        if scene["Id"].startswith(S14):
            scene["ContactWitness"] = S14 + "bodies_current"
        if scene["Id"].startswith(S08):
            # S08 remains withheld on this base. When its owning job emits it,
            # the replying seal is a current channel, never bodily attendance.
            contacts["nocticula"] = authenticated_reply(
                ["noct.acq.renewed_agreement", "noct.acq.seal_received", "noct.acq.an_answer_of_her_own_done"],
                ["noct.closed", "noct.acq.closed", "noct.acq.council_fight"])


def authenticated_reply(requires, forbids):
    """J03's S08 adapter: a seal sent earlier is not today's authenticated reply.

    The existing channel gates remain owned by S08. This contract checks them
    at every continuation before the respondent's answer can earn a deed.
    """
    return dict(Kind="letter", Requires=list(dict.fromkeys([
        "nocticula.reachable_by_letter", *requires])), Forbids=list(dict.fromkeys([
        "nocticula.epoch_unavailable", "nocticula.returned_actor_lost", *forbids])), Options=[])

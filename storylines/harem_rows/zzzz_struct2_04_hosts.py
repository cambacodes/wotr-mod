"""struct2-04: physical entries over existing bodies; no prose or new prices.

Run after row text/contract appenders. The native and returned cave doors share
one outcome witness, so taking either door retires the other. Unbound Drezen
venues remain coordinator work rather than adding another woman's body.
"""
import copy


def _physical(body):
    body.pop("Remote", None)
    body.pop("ManualOnly", None)
    body.pop("Kind", None)
    body.pop("Sender", None)


def register(payload, scenes, refs):
    from storylines import soana_trickster as soana, targona_trickster as targona
    from storylines import arueshalae_trickster as arue, minagho_chivarro_trickster as minagho

    by = {body["Id"]: body for body in scenes}
    # Both cave histories: original IDs stay on the returned hub, native copies
    # are appended. The native copy keeps the published nodes/answers verbatim.
    for step in ("settle", "retry"):
        body = by["household.pair.soana_camellia." + step]
        native = copy.deepcopy(body)
        native["Id"] += ".native"
        _physical(native)
        native["AnswerLists"] = [soana.HER_LIST]
        native["NativeReturnCue"] = soana.HER_RETURN
        native["Forbids"].append(soana.RETURNED)
        _physical(body)
        body["InteractionHub"] = "soana.presence"
        presence = payload["Presences"]["soana.presence"]
        body["Requires"] = list(dict.fromkeys([
            *body["Requires"], *presence["Requires"], "soana.presence.route_open"]))
        body["Forbids"] = list(dict.fromkeys([*body["Forbids"], *presence["Forbids"]]))
        scenes.append(native)

    # A hub interaction is an ordinary scene, not an E6 native-list reaction.
    body = by["targona.trickster.react.ix_a.yaniel"]
    _physical(body)
    body.update(InteractionHub=targona.HUB, ContactUnit=targona.UNIT,
                Reaction=False, Entry=body["Title"])
    # Yaniel's unit is resolved from the existing route module below; no guessed
    # blueprint or second presence is installed.
    from storylines import yaniel_trickster as yaniel
    body["AdditionalContactUnits"] = [yaniel.UNIT]
    # E6 previously installed these direct participant losses. Keep them when
    # changing presentation to an ordinary hub scene, alongside its composite.
    body["Forbids"] = list(dict.fromkeys([
        *body["Forbids"], yaniel.KILLED, yaniel.LEFT_FREE]))
    presence = payload["Presences"][targona.HUB]
    body["Requires"] = list(dict.fromkeys([
        *body["Requires"], *presence["Requires"], "targona.presence.route_open"]))
    body["Forbids"] = list(dict.fromkeys([*body["Forbids"], *presence["Forbids"]]))

    # The redeemed companion's native dialogue is a physical Drezen door.
    # Fallen Arueshalae has different bodies/hubs and remains held for design.
    for step in ("settle", "retry"):
        body = by["household.pair.arueshalae_minagho." + step + ".good"]
        _physical(body)
        body.pop("InteractionHub", None)
        body.update(AnswerLists=[arue.HUB], ContactUnit=arue.UNIT,
                    AdditionalContactUnits=[minagho.MIN_UNIT])

    # Reuse the existing appointment and resolution; journal text is copied
    # from authored scene titles/entry prompts, never newly written here.
    route = payload["Relationships"]["irabeth"]
    followup = by["irabeth.the_sealed_account"]
    appointment = next(node for node in by["irabeth.the_seized_wagon"]["Nodes"]
                       if node["Id"] == "next")["Choices"][0]
    route.setdefault("JournalEntries", []).append(dict(
        Id="irabeth.seized_wagon.docket", Title=followup["Title"],
        Description=appointment["Text"], OpenWhen=[["irabeth.wagon_heard"]],
        SettledWhen=[["irabeth.account_resolved"]]))

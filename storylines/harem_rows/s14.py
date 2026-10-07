"""S14: authored crusade observance, Galfrey / Arueshalae (hs-B §S14).

No native fact is changed. FaneFinal/Cue_0020 (f2ccd1c255733504093d837043db34de,
enGB fc3209bb-241b-4a9e-b5b9-ad8529d0327d) supports Galfrey's reservations,
not a universal recollection or unconditional trust. No physical intimacy.

Registration retains the read-only attendance name for saved wrappers. J01's
post-epoch pass evaluates it from current qualified bodies at the Table,
never from a saved flag or a choice's Set.
Attitude, final failure ownership, and W5 readers remain integrator-owned.
"""
import copy

from story_format import c, n, scene

P = "household.pair.galfrey_arueshalae."
PAIR = ("galfrey", "arueshalae")
ATTENDANCE = P + "bodies_current"
DEEDS = tuple(P + suffix for suffix in (
    "deed.galfrey_place_kept", "deed.arueshalae_place_kept",
    "cost.galfrey_public_judgment", "cost.arueshalae_unclaimed_place_yielded"))
# Metadata for W0c; this module never writes attitude or enmity.
STAGES = {
    "galfrey.harem.attitude.arueshalae.rival": [[P + "settle.seen"]],
    "arueshalae.harem.attitude.galfrey.respect": [[P + "settle.seen"]],
    "galfrey.harem.attitude.arueshalae.respect": [list(DEEDS)],
    "arueshalae.harem.attitude.galfrey.friend": [list(DEEDS)],
}
COMMON = ("trickster", "trickster.now", "foresight.page_taken",
          "household.stance_eligible", "household.table.kept", ATTENDANCE,
          "galfrey.harem.eligible", "arueshalae.harem.eligible",
          "galfrey.present_now", "arueshalae.present_now")
LOSSES = ("fool_king.gone", "trickster.failed", "galfrey.closed",
          "galfrey.killed_by_commander", "galfrey.epoch_unavailable",
          "galfrey.returned_actor_lost", "arueshalae.closed",
          "arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out",
          "arueshalae.kicked_out_evil", "arueshalae.epoch_unavailable",
          "arueshalae.returned_actor_lost")
ENMITY = {a + ".harem.enmity." + b: a + ".harem.reconciled." + b
          for a, b in (PAIR, PAIR[::-1])}


def _step(branch, retry=False):
    step = "retry" if retry else "settle"
    witness = P + step + ".seen"
    success = [witness, P + step + ".done"]
    if retry:
        success.append(P + "settle.done")
    success += [P + "settle." + branch + "_done", *DEEDS, P + "cost.commander_placement"]
    refused = [witness, P + step + ".refused", P + "unsettled"]
    good = branch == "good"
    opening = ('"I want them to see me beside you. Not behind you." {n}Arueshalae folds her wings close.{/n}'
               if good else
               '"Beside the banner? How flattering. Half the officers will hate it." {n}Arueshalae smiles at Galfrey.{/n} '
               '"You intend to stay there too, I hope. I would hate to be mistaken for your pet."')
    nodes = [n("start", "Galfrey",
        '{n}Beyond the tavern door, soldiers roll their blankets for the march back toward the Worldwound. '
        'Galfrey has come to settle where she and Arueshalae will stand at the gathering before they leave.{/n}\n'
        '"Here. Beside me, where the soldiers can see us. I will answer their objections myself."\n' + opening,
        c('"Finish the placement before the next observance."' if retry else
          '"Give her the place you have named."', "placed"),
        *([c('"Leave them apart."', "refused")] if retry else [
            c('"Leave the place undecided."', "unplaced"),
            c('"There will be no shared observance."', "refused")]),
        c('"Later."', abort=True)),
        n("placed", "Galfrey",
          '{n}At the gathering, Galfrey steps beneath the crusade banner. An officer looks at the succubus, '
          'then pointedly leaves a gap farther down the line. Galfrey holds her place.{/n}\n'
          '"I named this place. She will stand here."\n' + (
              '"Then I will stand here." {n}Arueshalae passes the empty place without looking at it. '
              'She turns to Galfrey rather than to you.{/n} "I hoped you would let me. Your judgment matters to me."'
              if good else
              '"At last, a useful view." {n}Arueshalae passes the empty place and settles beside Galfrey.{/n} '
              '"I think I shall enjoy your company. You make such an interesting enemy of your own officers."\n'
              '"Do not mistake this for approval of your appetites." {n}Galfrey says it without lowering her voice.{/n}\n'
              '"Oh, I heard you. I am still here." {n}Arueshalae smiles at her.{/n}'),
          c('[Keep the queen\'s chosen placement.]', flags=success, requires=(P + "voice.queen",)),
          c('[Keep Kitrane\'s chosen placement.]', flags=success, requires=(P + "voice.kitrane",))),
        n("refused", "Galfrey",
          '"Then we will stand separately." {n}Galfrey takes her cloak from the bench. '
          'Arueshalae leaves by the other side of the table; neither waits for the other.{/n}',
          c(flags=refused))]
    if not retry:
        nodes.append(n("unplaced", "Narrator",
            '{n}No place is named. When the soldiers gather, Galfrey stands with the officers; '
            'Arueshalae stays at the edge of the square. Their disagreement remains for another day.{/n}',
            c(flags=(P + "settle.seen", P + "settle.failed", P + "failed." + branch))))
    required = (P + "settle.failed", P + "failed." + branch) if retry else (P + "ready." + branch,)
    forbidden = (P + "settle.done", P + "unsettled") if retry else ()
    personality = "arueshalae.redeemed" if good else "arueshalae.corrupted"
    return scene(P + step + "." + branch, "The place under the banner", "Galfrey", 5,
        '[Galfrey and Arueshalae: the place under the banner]', nodes,
        requires=(*COMMON, personality, *required),
        forbids=(*LOSSES, *ENMITY, witness, *forbidden,
                 *(("arueshalae.corrupted",) if good else ())),
        delay=48 if retry else 0, last=5, Relationship="household", Chapters=[5],
        Areas=["2570015799edf594daf2f076f2f975d8"], InteractionHub="household.table",
        Participants=list(PAIR), ParticipantWomen=[], Pair=list(PAIR),
        ForbidOverrides=dict(ENMITY), RestAllowance="household.protected",
        HouseholdCategory="protected", HouseholdWitness=witness)


SCENES = [_step(branch, retry) for retry in (False, True) for branch in ("good", "evil")]


def register(payload, scenes, refs):
    """Append only S14 data; safe to call repeatedly on the same payload."""
    existing = {s["Id"] for s in scenes}
    scenes.extend(copy.deepcopy(s) for s in SCENES if s["Id"] not in existing)
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    for branch, personality in (("good", "redeemed"), ("evil", "corrupted")):
        derived[P + "ready." + branch] = [[
            "galfrey.harem.eligible", "arueshalae.harem.eligible",
            "galfrey.present_now", "arueshalae.present_now", "arueshalae." + personality]]
    forbids[P + "ready.good"] = ["arueshalae.corrupted"]
    derived[P + "voice.native_queen"] = [["galfrey.present_now"]]
    forbids[P + "voice.native_queen"] = ["galfrey.trickster.returned"]
    derived[P + "voice.queen"] = [[P + "voice.native_queen"], ["galfrey.trickster.crown_reclaimed"]]
    derived[P + "voice.kitrane"] = [["galfrey.trickster.returned"]]
    forbids[P + "voice.kitrane"] = ["galfrey.trickster.crown_reclaimed"]
    pending = payload.setdefault("PendingHooks", [])
    for key in (ATTENDANCE, *ENMITY, *ENMITY.values()):
        if key not in pending:
            pending.append(key)

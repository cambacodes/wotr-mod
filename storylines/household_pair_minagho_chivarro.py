"""S06 authored fixed-couple acknowledgment; no ladder, return or intimacy.

Native voice anchor: Chivarro_dialogue/Cue_0119,
7b8ff644c3d1e6848bef78edcab65193, enGB
eb303eaa-9c88-4aea-9a33-0e7913e40ad5. See the S06 build note.
"""
from copy import deepcopy

from story_format import c, n, scene
from storylines import household

P = "household.pair.minagho_chivarro."
ACK = P + "ack.seen"
R = "minagho_chivarro.trickster."
STATE = "minagho_chivarro.partner_state."
REL = "minagho_chivarro"


def voice(id, woman, text, *answers):
    return n(id, woman.capitalize(), text, *answers, portrait=woman.capitalize())


def acknowledgment(suffix, woman, women, nodes, requires=(), forbids=()):
    sid = P + "ack" + suffix
    household.CONSUMERS[sid] = household.PAGE_TAKEN
    return scene(
        sid, "Their own door", woman.capitalize(), 5,
        '"About your place in the household."', nodes,
        requires=("trickster", household.PAGE_TAKEN, woman + ".present_now",
                  "participant." + woman + ".available") + tuple(requires),
        forbids=(ACK, "minachiv.closed", "trickster.failed", "sacrifice") + tuple(forbids),
        last=5, optional=True, Relationship="household",
        Areas=[household.DREZEN], Chapters=[5],
        InteractionHub=REL + ".presence." + woman,
        ContactUnit=("565ccab37e2475742b043ec912a750fa" if woman == "minagho"
                     else "b7e819e2a9bb0804abcbffe8e7d91ba6"),
        Participants=[REL], ParticipantWomen=list(women),
        RestAllowance="household.protected", HouseholdCategory="protected",
        HouseholdWitness=ACK,
        ForbidOverrides={"sacrifice": "trickster.commander_back"})


PAIR_NODES = [
    voice("start", "chivarro",
          '{n}Chivarro has a room key hooked over one finger. Minagho reaches for it; '
          'Chivarro closes her fist. A wagon of wounded rattles past the stores.{/n} '
          '"Your soldiers can keep their barracks, honey. Our door stays ours. '
          'And before you start counting beds — she takes the side away from the window."',
          c('"And what does Minagho say?"', "minagho"),
          c("[Later.]", abort=True)),
    voice("minagho", "minagho",
          '"I say she snores." {n}Minagho pries open Chivarro\'s fist and takes the key. '
          'Chivarro catches her wrist, but Minagho brings the knuckles to her mouth.{/n} '
          '"Baphomet has had enough of me. I will not have another master, Golarian. '
          'She can keep the window. I will keep her."',
          c('"Your house, your invitations."', "held"),
          c('"Keep your door shut to me, then."', "private")),
    voice("held", "chivarro",
          '"Hear that? She will keep me. After all the trouble I went to finding her." '
          '{n}Chivarro catches Minagho by the collar and kisses her hard. When she lets go, '
          'Minagho is smiling with her teeth.{/n} "Knock, honey. Sometimes we may even '
          'let you in. Tonight I have other plans."',
          c("Continue", flags=(ACK, P + "own_house_acknowledged"))),
    voice("private", "minagho",
          '"Good. One fewer interruption." {n}Minagho pockets the key. Chivarro slips '
          'an arm through hers and steers her away from the wounded wagon.{/n} '
          '"Come, darling. Before they ask us to carry someone."',
          c("Continue", flags=(ACK, P + "private_house_acknowledged"))),
]
SCENES = [
    acknowledgment("", "chivarro", ("minagho", "chivarro"), PAIR_NODES,
                   requires=(R + "reunited", "minagho.present_now",
                             "participant.minagho.available")),
    acknowledgment(".minagho", "minagho", ("minagho",), [], forbids=("chivarro.present_now",)),
    acknowledgment(".chivarro", "chivarro", ("chivarro",), [], forbids=("minagho.present_now",)),
    acknowledgment(".spared", "minagho", ("minagho",), [],
                   requires=("minagho.spared.latched",), forbids=("chivarro.present_now",)),
]
# The spared Minagho has a distinct existing hub. Both wrappers share exhaustion.
SCENES[-1]["InteractionHub"] = REL + ".presence.minagho_spared"
SCENES[1]["Forbids"].append("minagho.spared.latched")

for page in SCENES[1:]:
    woman = page["ParticipantWomen"][0]
    other = "chivarro" if woman == "minagho" else "minagho"
    page["Nodes"] = [
        voice("start", woman,
              ('{n}Minagho sits outside the stores with a dagger across her knees. '
               'The quartermaster\'s men give her crate a wide berth.{/n} '
               '"A place at your table? I remember Chivarro. I have not given away her place. '
               'Do not start making arrangements for her."'
               if woman == "minagho" else
               '{n}Chivarro turns her room key between two fingers while the '
               'quartermaster argues over a wagon of bandages.{/n} '
               '"I have my own door, honey. Your table does not buy the key. '
               'And I remember Minagho. Her place is not yours to fill."'),
              c('"I have not forgotten her."', "dead", requires=(STATE + other + ".dead",)),
              c('"I have not forgotten her."', "distant", requires=(STATE + other + ".distant",)),
              c('"I have not forgotten her."', "unknown", requires=(STATE + other + ".unknown",)),
              c('"Your door remains yours."', "held"),
              c("[Later.]", abort=True)),
        voice("dead", woman,
              ('"She is dead. Say it." {n}Minagho digs the dagger into the crate.{/n} '
               '"I still want her. Do not mistake that for wanting a replacement."'
               if woman == "minagho" else
               '"She is dead, honey. I know." {n}Chivarro closes her hand around the key.{/n} '
               '"Leave her chair alone. I have not offered it."'),
              c("Continue", "held")),
        voice("distant", woman,
              ('"Then keep your promises to her out of your promises to me. '
               'She can answer for herself when she comes."'
               if woman == "minagho" else
               '"She has her own business. If she walks through that door, '
               'we will have ours. You do not get to settle it in her absence."'),
              c("Continue", "held")),
        voice("unknown", woman,
              ('"Neither have I. Bring me news if you have it. '
               'Until then, spare me your guesses."'
               if woman == "minagho" else
               '"No word, honey. That is all I can tell you. '
               'I will not hang mourning cloth because you need an answer."'),
              c("Continue", "held")),
        voice("held", woman,
              ('{n}Minagho pulls the dagger free.{/n} "Then we understand each other. '
               'Leave the guards outside when you visit. They smell afraid."'
               if woman == "minagho" else
               '{n}Chivarro puts the key away.{/n} "Good. You can visit. '
               'I have sold enough of them to know the difference."'),
              c("Continue", flags=(ACK, P + "solo_house_acknowledged"))),
    ]

# Mirror the existing presence contract, including its route-open observer.
# No body can be supplied by a historical invitation or a failed spawn.
for page in SCENES:
    hub = page["InteractionHub"]
    page["Requires"].append(hub + ".route_open")
    page["Forbids"].append(hub + ".failed")
    if hub.endswith(".chivarro"):
        page["Requires"].append(R + "chivarro_in")
        page["Forbids"].append(R + "chivarro_sent_back")
    elif hub.endswith(".minagho_spared"):
        page["Forbids"].extend(["minagho.dead", R + "declined_minagho"])
    else:
        page["Requires"].extend(["minagho.dead", R + "minagho_in", R + "returned_minagho"])
        page["Forbids"].extend(["minagho.epoch_redeparted", "minagho.returned_actor_lost"])

# Pair attendance also authenticates the second woman's own arrival channel.
spared_pair = deepcopy(SCENES[0])
spared_pair["Id"] += ".pair_spared"
spared_pair["Requires"].extend(["minagho.spared.latched", R + "minagho_in"])
spared_pair["Forbids"].extend(["minagho.dead", R + "declined_minagho",
                               REL + ".presence.minagho_spared.failed"])
SCENES[0]["Requires"].extend(["minagho.dead", R + "returned_minagho", R + "minagho_in"])
SCENES[0]["Forbids"].extend([REL + ".presence.minagho.failed", R + "declined_minagho"])
SCENES.append(spared_pair)
household.CONSUMERS[spared_pair["Id"]] = household.PAGE_TAKEN

# Current arrival observers, not outcomes. Alive does not mean in Drezen.
DERIVED = {
    P + "minagho_returned_here": [[R + "minagho_in", "minagho.dead",
                                  R + "returned_minagho", "minagho.present_now"]],
    P + "minagho_spared_here": [[R + "minagho_in", "minagho.spared.latched",
                                "minagho.present_now"]],
    P + "minagho_here": [[P + "minagho_returned_here"], [P + "minagho_spared_here"]],
    P + "chivarro_here": [[R + "chivarro_in", "chivarro.present_now"]],
}
DERIVED_FORBIDS = {
    P + "minagho_returned_here": [REL + ".presence.minagho.failed", R + "declined_minagho"],
    P + "minagho_spared_here": ["minagho.dead", REL + ".presence.minagho_spared.failed",
                               R + "declined_minagho"],
    P + "chivarro_here": [REL + ".presence.chivarro.failed", R + "chivarro_sent_back"],
}
for page in SCENES:
    women = page["ParticipantWomen"]
    if len(women) == 2:
        page["Requires"].extend([P + "minagho_here", P + "chivarro_here"])
        page["AdditionalContactUnits"] = ["565ccab37e2475742b043ec912a750fa"]
    else:
        other = "chivarro" if women[0] == "minagho" else "minagho"
        page["Forbids"].remove(other + ".present_now")
        page["Forbids"].append(P + other + "_here")

# This fixed couple already exists. Acknowledging their own house is not a
# new Commander-romance commitment. Use the owning route's existing contacts
# and validated solo-loss exemptions, rather than Table membership gates.
WOMEN = {}
for page in SCENES:
    women = page.pop("ParticipantWomen")
    WOMEN[page["Id"]] = women
    page.pop("Participants")
    page["Relationship"] = REL
    if len(women) == 1:
        other = "chivarro" if women[0] == "minagho" else "minagho"
        page["AbsentPartnerFlags"] = [other + ".dead"]

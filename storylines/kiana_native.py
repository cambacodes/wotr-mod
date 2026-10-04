"""Kiana's native reconciliations (engine queue 8; Writer/handoffs/trickster/kiana.md, Polish pass residuals 1-2).

8a: VendorArsinoe/Answer_0025 ("Is there any news about the poor folk whose souls were stolen?" -> Cue_0026, her search
found nothing) stays offered after the Commander ransomed or bought back the guests. A reviewed E18 gate hides it in those
worlds (the list the game already shows once Seelah's Q3 has started). Read only; warning-only on refusal.
"""
import copy

from storylines.native_overrides import register_legacy

from story_format import n, scene

from storylines import kiana_trickster as kt

# 8c: Seelah Q3's ElandKianaAftermath (dialog 27bc5f6c) opens on Cue_0001 "Elan and Kiana fall into each other's arms". A couple
# that separated (kiana.separated) gets its own line in the same place (E14i, the dialog's FirstCue); Seelah's "Let's give them
# some space" (Cue_0002) still follows. Read only, warning-only.
AFTERMATH = "kiana.native.aftermath_separated"
SCENES = [scene(AFTERMATH, "", "KianaEpilogue", 3, "", [
    n("arms", "Narrator", "{n}Elan and Kiana face each other, both alive, both whole. Kiana takes his hands and holds them a "
      "moment, and she is the one who lets go first. Whatever they had been to one another, they were not that now, and "
      "neither of them pretended otherwise in front of a crowd.{/n}")],
    # No seelah.elan_dead forbid: that etude is Playing-only in Drezen (E3), and the aftermath dialog itself needs Elan alive.
    # Engine-q2: trickster.now, not the run latch. kiana.separated is set on every path, so the path is this edit's only
    # Trickster evidence, and the aftermath can play after a Chapter 4 failure or a Summit conversion (T6a).
    requires=("trickster.now", "kiana.separated"), forbids=("kiana.bereaved",), last=99, Relationship="kiana")]

# 6b (kiana.md, Polish residual 2): a ransom or a buy-back already brought every guest home (Arsinoe broke the stones in the ward),
# so native Q3 would recover them a second time. Read only, warning-only, Trickster only.
# - JewelerFinal/Cue_0051 (Seelah pours the bowl of soul-gems into a pouch, "We have the souls..."): the settings are still in
#   Sunhammer's bowl, the sockets empty. The replacement keeps the cue's cutscene and quest steps (ReturnSouls is still given).
# - ElandKianaAftermath/Cue_0001 ("fall into each other's arms"): the couple has been awake since the ward; a second variant after
#   the separated line. Seelah's "Let's give them some space" still follows.
HOME_WORLDS = [["trickster.now", kt.RANSOMED], ["trickster.now", kt.BOUGHT]]
BOWL = "kiana.native.q3_bowl_emptied"
AFTERMATH_HOME = "kiana.native.aftermath_home"
CUE_0051 = "4255f49c18c69aa4ab4d5582d0b6f39e"
SCENES += [
    scene(BOWL, "", "KianaEpilogue", 3, "", [
        n("bowl", "Narrator", "{n}Seelah tips the bowl of jewelry into a pouch: rings, pendants, a bride's circlet, every setting from the "
          "wedding, and every socket in them empty. The stones were prised out and sold back to Drezen, and Arsinoe broke them there, "
          "one clean tap at a time.{/n} \"Empty. Every one of them. He kept the settings anyway, like receipts.\" {n}She closes the pouch "
          "all the same.{/n} \"Arsinoe will want these for her ledger. Let's go, {name}! I... don't want to stay here any longer.\"")],
        requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
    scene(AFTERMATH_HOME, "", "KianaEpilogue", 3, "", [
        n("arms", "Narrator", "{n}Elan and Kiana are waiting at the front of the crowd. They have been awake since the night the stones "
          "were broken in the ward, and they have had time to be glad already; Kiana has his arm all the same, and does not let go "
          "of it, heedless of everyone else around them.{/n}")],
        requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], forbids=("kiana.separated", "kiana.bereaved"),
        last=99, Relationship="kiana"),
]
# Authored DLC reconciliation: the paid ward release changes Q3's recovery and couple dialogue only on Trickster.
SCENES += [
    scene('kiana.native.aftermath_6_separated', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Yes, it feels good to be alive." {n}Kiana smiles at Elan, then turns to you.{/n} "And to make my own decisions again. Elan and I have spoken. The wedding can stay in the past."')],
          requires=("trickster.now", "kiana.separated",), forbids=("kiana.bereaved",), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_6_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"It feels good to be married and able to remember it." {n}Kiana smiles.{/n} "Arsinoe says I\'ve complained enough to be discharged twice. Elan is still off fighting, of course."')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], forbids=("kiana.separated", "kiana.bereaved"), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_7_separated', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"We\'re glad too," {n}Kiana replies.{/n} "The wedding was a bloody disaster. I\'m glad Elan is alive. That doesn\'t mean I want another wedding."')],
          requires=("trickster.now", "kiana.separated",), forbids=("kiana.bereaved",), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_7_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"We\'re glad too. And we\'ve finally had our wedding night." {n}Kiana grins at Elan.{/n} "You paid enough for it, Commander. I wasn\'t going to let those damned demons keep that as well!"')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], forbids=("kiana.separated", "kiana.bereaved"), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_8_separated', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Kiana..." {n}Elan reddens, then bows his head.{/n} "Yes. You\'ve told me. I won\'t argue with you here."')],
          requires=("trickster.now", "kiana.separated",), forbids=("kiana.bereaved",), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_8_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Kiana, my love!" {n}Elan blushes.{/n} "The Commander bought our freedom. That doesn\'t mean we owe every detail!"')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], forbids=("kiana.separated", "kiana.bereaved"), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_11_separated', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Neither can I. For getting us home, and for listening afterwards." {n}Kiana glances at Elan.{/n} "We needed both."')],
          requires=("trickster.now", "kiana.separated",), forbids=("kiana.bereaved",), last=99, Relationship="kiana"),
    scene('kiana.native.aftermath_11_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Neither can I. Arsinoe had barely broken the stones before he was thanking everyone in the ward." {n}Kiana laughs.{/n} "You see? We still have that in common."')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], forbids=("kiana.separated", "kiana.bereaved"), last=99, Relationship="kiana"),
    scene('kiana.native.doubt_28_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Greetings, Commander. The families are waiting. You brought these people home before Sunhammer could be stopped, and Seelah helped recover what he stole. They want to thank her. Seelah, come with me."')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
    scene('kiana.native.doubt_29_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '{n}Seelah gets to her feet.{/n} "Me? Commander brought them home. I brought back a pouch of empty settings."')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
    scene('kiana.native.doubt_30_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"And brought back the settings instead of leaving his victims with nothing. Their souls are already free. Their families still have something to say to the paladin who went after their thief."')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
    scene('kiana.native.doubt_31_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"I let that thief sell them their wedding rings in the first place." {n}Seelah looks away.{/n} "What am I supposed to tell them?"')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
    scene('kiana.native.doubt_32_home', "", "KianaEpilogue", 3, "", [n("line", "Narrator", '"Tell them what you found. They asked for you, Seelah. The families, the Houndhearts, all of them. You can argue with me afterwards. Come."')],
          requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
]
NATIVE_EPILOGUE_EDITS = {
    'a819e8c85ef23324bb0d8117bb9d7df3': dict(Parent='245ec8482e1f37b4a8702e54430c5aa7', Dialog='27bc5f6c94108a446b8273800f7da48b', Key='1aef0e95-dc1e-49fa-9852-3fba13bd5e20',
        Replacement='kiana.native.aftermath_6_separated', When=[["trickster.now", "kiana.separated"]], KeepNativeImage=False,
        Variants=[dict(Replacement='kiana.native.aftermath_6_home', When=HOME_WORLDS, KeepNativeImage=False)]),
    'df45181e1968f26459f9e8bc2b995a34': dict(Parent='245ec8482e1f37b4a8702e54430c5aa7', Dialog='27bc5f6c94108a446b8273800f7da48b', Key='0c8edca3-4bab-4535-a37b-ea3d3186213b',
        Replacement='kiana.native.aftermath_7_separated', When=[["trickster.now", "kiana.separated"]], KeepNativeImage=False,
        Variants=[dict(Replacement='kiana.native.aftermath_7_home', When=HOME_WORLDS, KeepNativeImage=False)]),
    '0e50ec24099196a42b7089ffecdc46b2': dict(Parent='df45181e1968f26459f9e8bc2b995a34', Dialog='27bc5f6c94108a446b8273800f7da48b', Key='0568c8c8-7e85-4fc3-ba62-309d2bebee00',
        Replacement='kiana.native.aftermath_8_separated', When=[["trickster.now", "kiana.separated"]], KeepNativeImage=False,
        Variants=[dict(Replacement='kiana.native.aftermath_8_home', When=HOME_WORLDS, KeepNativeImage=False)]),
    '4cd264ce0432bb94a8e80a551190150d': dict(Parent='f575d21b1fabec74da1e54484573206b', Dialog='27bc5f6c94108a446b8273800f7da48b', Key='b873d838-c522-4d2f-83e0-b017070b6102',
        Replacement='kiana.native.aftermath_11_separated', When=[["trickster.now", "kiana.separated"]], KeepNativeImage=False,
        Variants=[dict(Replacement='kiana.native.aftermath_11_home', When=HOME_WORLDS, KeepNativeImage=False)]),
    '73815b731281fdc47bbc59aba42b2126': dict(Parent='af455979c98c7484c9e74360b4645c62', Dialog='ff5c54635748e334990879498eb5429b', Key='afe4a854-e6c9-442f-8755-cc08e4fd140c',
        Replacement='kiana.native.doubt_28_home', When=HOME_WORLDS, KeepNativeImage=False,
        Variants=[]),
    'e9a5a4c03ea016f47b29d91b2ff3a00c': dict(Parent='73815b731281fdc47bbc59aba42b2126', Dialog='ff5c54635748e334990879498eb5429b', Key='6ba1cb04-8e0b-40c5-ac6d-6cf64ff0e094',
        Replacement='kiana.native.doubt_29_home', When=HOME_WORLDS, KeepNativeImage=False,
        Variants=[]),
    '2b133bf7ac66d6241a69a53dce2bf05f': dict(Parent='e9a5a4c03ea016f47b29d91b2ff3a00c', Dialog='ff5c54635748e334990879498eb5429b', Key='c2e4632d-2c47-43cf-bebb-0f8dbbab495b',
        Replacement='kiana.native.doubt_30_home', When=HOME_WORLDS, KeepNativeImage=False,
        Variants=[]),
    'b3e6076282402a1489b6f226567cf8fa': dict(Parent='2b133bf7ac66d6241a69a53dce2bf05f', Dialog='ff5c54635748e334990879498eb5429b', Key='3cb6cfc5-ab5e-4ddb-a7d1-8ce3775b987f',
        Replacement='kiana.native.doubt_31_home', When=HOME_WORLDS, KeepNativeImage=False,
        Variants=[]),
    'aeccec94d6e3246488d7f13577a8380d': dict(Parent='b3e6076282402a1489b6f226567cf8fa', Dialog='ff5c54635748e334990879498eb5429b', Key='58ee4b07-0488-4fab-a286-d50f786fe135',
        Replacement='kiana.native.doubt_32_home', When=HOME_WORLDS, KeepNativeImage=False,
        Variants=[]),
    "81109ea8fb20dbc478cf67116740f4a1": dict(Parent="27bc5f6c94108a446b8273800f7da48b", Dialog="27bc5f6c94108a446b8273800f7da48b",
                                             Key="b261aab4-14ff-41e7-bd72-21aeeab7df44", Replacement=AFTERMATH,
                                             When=[["trickster.now", "kiana.separated"]], KeepNativeImage=False,
                                             Variants=[dict(Replacement=AFTERMATH_HOME, When=HOME_WORLDS, KeepNativeImage=False)]),
    CUE_0051: dict(Parent="800706e8e47847f4e88e2c3c586706de", Dialog="fa5e885aaa9840f419939176d38d176b",
                   Key="8e4494ff-5209-44e1-9e80-98a8b9d2a6a9", Replacement=BOWL, When=HOME_WORLDS, KeepNativeImage=False, Variants=[]),
}

NATIVE_GATES = {
    "kiana.q3_recovery": dict(Target="2b4a5c01a192d1f4aa8c9d32aa149727", Relationship="kiana", When=HOME_WORLDS),
    "arsinoe.souls_search_answer": dict(Target="41d9638f7d971164fab4efdbbbffbe70", Relationship="kiana",
                                        When=HOME_WORLDS),
}


def integrate(payload):
    """Register the gates and the aftermath line (after kiana_trickster)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS, gates=NATIVE_GATES)

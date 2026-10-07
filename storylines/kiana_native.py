"""Kiana's native reconciliations (engine queue 8; Writer/handoffs/trickster/kiana.md, Polish pass residuals 1-2).

8a: VendorArsinoe/Answer_0025 ("Is there any news about the poor folk whose souls were stolen?" -> Cue_0026, her search
found nothing) stays offered after the Commander ransomed or bought back the guests. A reviewed E18 gate hides it in those
worlds (the list the game already shows once Seelah's Q3 has started). Read only; warning-only on refusal.
"""
import copy

from storylines.native_overrides import declare, register_legacy

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
    "kiana.q3_recovery": dict(Target="2b4a5c01a192d1f4aa8c9d32aa149727", Relationship="kiana", When=HOME_WORLDS + [["trickster.now", kt.RETURNED, kt.ROBBED]]),
    "arsinoe.souls_search_answer": dict(Target="41d9638f7d971164fab4efdbbbffbe70", Relationship="kiana",
                                        When=HOME_WORLDS),
}


# eng7-f1: authored paid-history wording, findings 020/021/027. Sunhammer still faces
# the native outcomes; the paid rescue is neither repeated nor granted by this edit.
NATIVE_ANSWER_EDITS = {
    "901c1edd8887dfa4b9f108e106f38423": dict(AnswerList="99ab39af138f60f468c5ea9ab3ab5249",
        Key="74e73e62-e594-4200-8f0b-51c206c927d7", Relationship="kiana", When=HOME_WORLDS,
        Text='"We brought the wedding guests home. Now we find Elan and stop Sunhammer."'),
    "01a184d01ff707748b6377c38d2912e5": dict(AnswerList="99ab39af138f60f468c5ea9ab3ab5249",
        Key="b6aadd42-09ba-48cd-86fa-4f3ef5ba83bf", Relationship="kiana", When=HOME_WORLDS,
        Text='"The guests are safe. Now we make Sunhammer answer for this."'),
    "22ced28b5ecb08348b35daa51ab112b1": dict(AnswerList="31b874c1cdd33054d8925793772901eb",
        Key="ef6faada-c7c6-4c63-b1d6-f19a00da9c17", Relationship="kiana", When=HOME_WORLDS,
        Text='"Their souls are free. Repay what you stole from their families, and I\'ll let you go."'),
}
# end eng7-f1

# eng7-f6b begin: authored DLC reconciliation of Kiana 009-032.
# A released soul stays released; Elan's choices and all native consequences stand.
# Text-only runtime delivery preserves original CueSeen/SelectedAnswers and sequence positions.
SCENES.append(scene('kiana.native.q3_reconcile_009_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"All right, here\'s the deal." {n}Seelah gets straight to the point.{/n} "The wedding guests are home, thanks to you. But Sunhammer is still out there. We have a lead on his hideout, and I mean to make sure he never does this again."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['82213327a06db644fb2b5bb1410d4654'] = dict(Parent='def14993a63a830478c3d6d6b031338c', Dialog='e17e0900947b47b47aacd875f6490626', Key='6962fab7-3d93-4c05-92fa-ca0c914d4e4d', Replacement='kiana.native.q3_reconcile_009_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_010_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '{n}A shadow crosses Elan\'s face.{/n} "Kiana is awake. They all are. I can leave the hospital without wondering whether she\'ll still be breathing when I get back. But that bastard is still free. I want to find him."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_010_single', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '{n}Elan rubs his eyes.{/n} "Kiana is awake. I keep going back to hear her speak, just to be sure. The others are still lying there, though. We can\'t leave their souls with those monsters."')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['3f29d60b9a30bbb49bc9d56eaae1f643'] = dict(Parent='d30553a00d511b8439e9cfdca0564d86', Dialog='e17e0900947b47b47aacd875f6490626', Key='5d8e7c45-94d1-4c1a-9b5c-7987b289d282', Replacement='kiana.native.q3_reconcile_010_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_010_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_011_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"I\'ll leave at once and watch the cave. We can meet there." {n}Elan\'s jaw tightens.{/n} "Kiana is home. Sunhammer must have thought that would be the end of it. He was wrong."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_011_single', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"I\'ll leave at once and watch the cave. We can meet there." {n}Elan sighs.{/n} "Kiana got out. The other guests deserve the same chance. I can\'t sit beside her bed and forget them."')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['5fa8ed029a93b4348b82ec659e6839a0'] = dict(Parent='cd580fd11d9081f45816e3a8eda2ebf9', Dialog='e17e0900947b47b47aacd875f6490626', Key='60a2a08c-7b89-429f-8956-30184ad2712e', Replacement='kiana.native.q3_reconcile_011_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_011_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_012_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"You got the victims home. Now I\'m itching to give my blade a taste of those soul-stealing cultists! We\'ll find Sunhammer and bring back what he stole."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['f750317f25d754b41b465a9533216338'] = dict(Parent='be25aa4b776039042b4de208aa557e78', Dialog='e17e0900947b47b47aacd875f6490626', Key='452340b8-848b-4057-8a4a-17435357540d', Replacement='kiana.native.q3_reconcile_012_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_013_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Suit yourself. But I\'m not leaving Sunhammer free to do this to another wedding."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['81f0222e6856efd4bbdbd5dea796716a'] = dict(Parent='8768fb1e6ba190f479377c6f29979af2', Dialog='e17e0900947b47b47aacd875f6490626', Key='baa20a60-7931-4084-b510-bf166145a1f2', Replacement='kiana.native.q3_reconcile_013_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_014_full', "", "KianaEpilogue", 5, "", [n("line", 'Arsinoe', '"The divination I attempted while the souls were missing pointed to a cave beneath a rock shaped like a gravestone, on the outskirts of the Winged Wood. The forest has been burning since the demons set it alight. The souls are home now, but that cave may still lead us to Sunhammer. I cannot tell you what awaits beneath the rock."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['a473e5412ffd0f54fbf395770a80a008'] = dict(Parent='82213327a06db644fb2b5bb1410d4654', Dialog='e17e0900947b47b47aacd875f6490626', Key='9e3e8d42-8f1c-4cb9-9dfb-d4c5712ff6d1', Replacement='kiana.native.q3_reconcile_014_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_015_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Anyway, Elan and I have decided to go there, find Sunhammer, and rough up any demon or cultist that gets in our way! We owe those families more than a bill for their freedom. We\'d love to have your help."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['124ca3b348b3dff429ef708e5b24788a'] = dict(Parent='a473e5412ffd0f54fbf395770a80a008', Dialog='e17e0900947b47b47aacd875f6490626', Key='d895a05d-ad4f-4d2d-9c28-70880a010585', Replacement='kiana.native.q3_reconcile_015_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_016_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '{n}Seelah hesitates, then shakes her head.{/n} "You saved them, {name}. I won\'t forget that. But Sunhammer is still free, and you\'re telling me to let him stay that way. I can\'t. Farewell. Come on, Elan; we have a journey to prepare for."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['613485017b96c3840a2f9eea886deff1'] = dict(Parent='d6e5897cc65cb334d8da8c46ef400d1c', Dialog='e17e0900947b47b47aacd875f6490626', Key='8b555c03-fe28-4d02-85be-b25b99bcd0b0', Replacement='kiana.native.q3_reconcile_016_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_017_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"She\'s awake, and I still catch myself watching to make sure she\'s breathing." {n}Elan draws a long breath.{/n} "I want Sunhammer stopped before anyone else has to sit beside a bed like that. Forgive me. I\'m tired."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_017_single', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"Kiana is awake, but the other beds are still full. Every time I visit her, I have to walk past them." {n}Elan draws a long breath.{/n} "We have to get the others back. Forgive me. I\'m tired."')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['086a160e51ef79c4d98750203cb4b641'] = dict(Parent='124ca3b348b3dff429ef708e5b24788a', Dialog='e17e0900947b47b47aacd875f6490626', Key='87e38061-27ad-44e8-ad6b-2f52b7429fc6', Replacement='kiana.native.q3_reconcile_017_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_017_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_018_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '{n}Elan\'s eyes burn.{/n} "A soldier fights better when there\'s a reason. You brought Kiana home. I won\'t let Sunhammer walk away from what he did to her. I will find him."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_018_single', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '{n}Elan\'s eyes burn.{/n} "A soldier fights better when there\'s a reason. Kiana is home, but the people who came to our wedding are still prisoners. I will get them back."')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['d759f7956ba304442b74a842ff6b14d5'] = dict(Parent='d6e68640b972e8e4e9ea460235fcc914', Dialog='e17e0900947b47b47aacd875f6490626', Key='a03f71db-e5e0-4f72-b29a-9834b4a48165', Replacement='kiana.native.q3_reconcile_018_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_018_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_019_full', "", "KianaEpilogue", 5, "", [n("line", 'Jannah', '"Commander..." {n}Jannah hesitates, then lifts her head.{/n} "I know you brought the wedding guests home. I want to help find Sunhammer and the cultists who did this. Let me come with you and Seelah. Please, give me another chance!"')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['ff03c12b165989e479d7c80e9ce7a8f9'] = dict(Parent='c207f647111ab6e46adeef6cad2ae929', Dialog='189401b80979be0439f3e3cb9f053d1e', Key='ec2188d1-671b-4077-8c5f-79fc07598302', Replacement='kiana.native.q3_reconcile_019_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_022_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"Greetings, Commander." {n}Elan salutes, calm and composed.{/n} "I kept watch, as you instructed. Sunhammer is here. I saw the wedding jewelry; the stones are gone, but he kept the settings. The cave is well guarded. We\'ll have to fight our way inside."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['cb2e13e1ded36e5419d746ed92162a91'] = dict(Parent='dc3a376f09759574f997995e8f07689a', Dialog='e35b026526a45204d8eeefa22a7f5a57', Key='b8064d2c-fba2-4fa6-8a6f-b6dadab2aee7', Replacement='kiana.native.q3_reconcile_022_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_023_full', "", "KianaEpilogue", 5, "", [n("line", 'Jannah', '{n}Jannah struggles to catch her breath.{/n} "Thank goodness you\'re here! Elan and I were watching the cave when he saw Sunhammer carrying the wedding jewelry. He wanted the jeweler\'s head. I told him Kiana was safe, told him to wait for you; he wouldn\'t listen. He rushed in alone and told me to stay here. He should never have gone in alone..."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_023_single', "", "KianaEpilogue", 5, "", [n("line", 'Jannah', '{n}Jannah struggles to catch her breath.{/n} "Thank goodness you\'re here! Elan saw Sunhammer carrying the soul jewelry and rushed after him. I told him to wait for you. Kiana was home, but the others weren\'t; that was all he would say. He told me to stay here. He should never have gone in alone..."')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['e65e4b85197e6aa42a40d34abcea889c'] = dict(Parent='563d9ab3629492b458369e281f28b033', Dialog='e35b026526a45204d8eeefa22a7f5a57', Key='a4e4b388-60b7-4030-9aaf-4f06f807f1e4', Replacement='kiana.native.q3_reconcile_023_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_023_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_024_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"One more thing: Darek Sunhammer is here. I saw him by the cave entrance, turning the stolen jewelry over in his hands. The stones were gone, but he still seemed pleased with his work. He must be someone of consequence in this cult. We should expect a fight."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['be05eef615c2eac44ac30ec0a2e49603'] = dict(Parent='5bf8f4fc37225f544b9244b683287899', Dialog='e35b026526a45204d8eeefa22a7f5a57', Key='697942a5-46b2-4c85-975c-602efa20836b', Replacement='kiana.native.q3_reconcile_024_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_025_full', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"Traps... so many traps. I saw Sunhammer with the jewelry. I wanted to kill him... didn\'t look at the door." {n}Elan convulses and groans.{/n} "Kiana\'s home. Tell her... I\'m sorry. Seelah, don\'t let him do this again..." {n}Another spasm passes through him. Then he lies still.{/n}')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_025_single', "", "KianaEpilogue", 5, "", [n("line", 'Elan', '"Traps... so many traps. I saw Sunhammer with the jewelry. The others\' souls... I ran after him. Didn\'t look at the door." {n}Elan convulses and groans.{/n} "Kiana\'s home. Tell her... I\'m sorry. Save the others, Seelah..." {n}Another spasm passes through him. Then he lies still.{/n}')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['5736cff83ea67644bb11346947b1eb2f'] = dict(Parent='b0369d1b8d8ba2d40a5eec0401ea7407', Dialog='9907442d488449a4fb33e182f3f732af', Key='ba2425dd-420f-4ff6-abaa-2b5f0ae95741', Replacement='kiana.native.q3_reconcile_025_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_025_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_026_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Don\'t say that! Kiana was safe, but he couldn\'t let go of what Sunhammer did to her. He wanted the bastard dead. He should have waited for us..."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
SCENES.append(scene('kiana.native.q3_reconcile_026_single', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Don\'t say that! Kiana was safe, but his other friends were still prisoners. He saw Sunhammer with those stones and couldn\'t stand to wait. He should have waited for us..."')],
    requires=("trickster.now", kt.RETURNED), forbids=(kt.RANSOMED, kt.BOUGHT), last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['dd9956385abff89418d83075e1b7774c'] = dict(Parent='c0db5a85736dae247835254af7a2bd37', Dialog='9907442d488449a4fb33e182f3f732af', Key='8fbff9f7-a739-4a19-b5cd-8102b2299891', Replacement='kiana.native.q3_reconcile_026_full', When=HOME_WORLDS, KeepNativeImage=False, Variants=[dict(Replacement='kiana.native.q3_reconcile_026_single', When=[["trickster.now", kt.RETURNED, "!" + kt.RANSOMED, "!" + kt.BOUGHT]], KeepNativeImage=False)])
SCENES.append(scene('kiana.native.q3_reconcile_028_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '{n}Seelah sits with her hands clasped, staring at the floor.{/n} "There you are, {name}. Arsinoe is gathering the families. They\'ve been awake since you brought the stones home. I should be glad. I am glad. I just..." {n}She looks down at her hands again.{/n}')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['75220bf8ab5be034ea55b84d24c58de2'] = dict(Parent='ff5c54635748e334990879498eb5429b', Dialog='ff5c54635748e334990879498eb5429b', Key='43e11168-7f70-4aa8-b527-b657268d390f', Replacement='kiana.native.q3_reconcile_028_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_029_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Ugh, where do I even start? There\'s something I have to ask you, {name}. Curl is awake with the rest of them. What if Sunhammer was telling the truth, and Curl really did work with the cultists? What will you do to him?"')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['096dd0fc12adbaf438bca7c7c9ebb4ba'] = dict(Parent='f967c3e0543a53846852152359ad90ee', Dialog='ff5c54635748e334990879498eb5429b', Key='cbbe11fe-01ff-4ba9-8f1f-2b2a9b4940a6', Replacement='kiana.native.q3_reconcile_029_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_030_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Not long. Arsinoe wants to examine everyone again and have their families there when we return the jewelry. She\'ll call us when they\'re ready."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['3bdbd8728bc75bf4eadae1152a34f26b'] = dict(Parent='04c5a2a333bf6e34eaf1982ed7a58fa0', Dialog='ff5c54635748e334990879498eb5429b', Key='cd9de62b-2a56-4220-b057-6c1a3ea86b25', Replacement='kiana.native.q3_reconcile_030_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_031_full', "", "KianaEpilogue", 5, "", [n("line", 'Seelah', '"Everyone is home. Elan is alive. Jannah came through for us. When I took my oath, I swore to guard the honor of my fellows, have faith in them, and learn the weight of my sword... I tried. But I can\'t stop thinking about what Sunhammer said before he died. He was being spiteful, right? Poison, not truth."')],
    requires=("trickster.now",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['01a1c98b38a78fd4abeaa0c09f3a5be9'] = dict(Parent='f9abfcd9d014f5944b25dd1b3acc841d', Dialog='ff5c54635748e334990879498eb5429b', Key='9abb4bcf-bb04-4a8c-bd1c-4cbcb3de1e3e', Replacement='kiana.native.q3_reconcile_031_full', When=HOME_WORLDS, KeepNativeImage=False)
SCENES.append(scene('kiana.native.q3_reconcile_032_full', "", "KianaEpilogue", 5, "", [n("line", 'Kiana', '{n}Kiana clasps her hands against her chest.{/n} "We had already parted. I thought the worst thing left was telling him why." {n}She swallows.{/n} "Now he\'s dead. Elan... you bloody fool."')],
    requires=("trickster.now", "kiana.separated"), RequiresAnyGroups=[["kiana.bereaved", "seelah.elan_dead"]], Areas=[kt.DREZEN], last=5, Relationship="kiana"))
NATIVE_EPILOGUE_EDITS['aebbc1845e827dd4da4e28014e7b4162'] = dict(Parent='6a197b1557eb815458304ec649228fb8', Dialog='6a197b1557eb815458304ec649228fb8', Key='1b2e5ca9-c1b5-42b0-9523-5460c6d33a2c', Replacement='kiana.native.q3_reconcile_032_full', When=[["trickster.now", "kiana.separated", "kiana.bereaved"], ["trickster.now", "kiana.separated", "seelah.elan_dead"]], KeepNativeImage=False)
# eng7-f6b: 010 sibling, same native question/answer identity and hospital history.
NATIVE_ANSWER_EDITS["5d02b3f1d1f6774419ea9fd3795596e8"] = dict(
    AnswerList="a5888720b68047b48b9791bed94e22c8", Key="12e922e5-7d4c-4e06-a130-765d91876379",
    Relationship="kiana", When=HOME_WORLDS, Text='"How did the infirmary hold out while we were gone?"')
# eng7-f6b end

def integrate(payload):
    """Register the gates and the aftermath line (after kiana_trickster)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    payload.setdefault("NativeTextEdits", {}).update(copy.deepcopy(NATIVE_TEXT_EDITS))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS, gates=NATIVE_GATES)
    # eng7-f1
    for target, spec in NATIVE_ANSWER_EDITS.items():
        declare(payload, source=__name__, target=target, target_type="answer", action="REPLACE", spec=spec)
    # end eng7-f1


# Authored DLC-tier consequences of the existing ransom or con.
# These reviewed text fields keep every native speaker, choice, action and quest step.
PARTIAL_WORLDS = [["trickster.now", kt.RETURNED, kt.ROBBED]]
SEPARATED_WORLDS = [["trickster.now", "kiana.separated"]]
NATIVE_TEXT_EDITS = {}


def _text(guid, key, paid, partial=None, *, field="Text", kind="BlueprintCue", separated=False):
    variants = [dict(Text=paid, When=SEPARATED_WORLDS if separated else HOME_WORLDS, Forbids=[])]
    if partial:
        variants.append(dict(Text=partial, When=PARTIAL_WORLDS, Forbids=[kt.DOG]))
    NATIVE_TEXT_EDITS[guid + "/" + field] = dict(Type=kind, Key=key, Variants=variants)


_text("901c1edd8887dfa4b9f108e106f38423", "74e73e62-e594-4200-8f0b-51c206c927d7", '"We\'ll find Elan and stop Sunhammer!"', kind="BlueprintAnswer")
_text("01a184d01ff707748b6377c38d2912e5", "b6aadd42-09ba-48cd-86fa-4f3ef5ba83bf", '"We\'ll find Sunhammer and recover the stolen jewelry!"', kind="BlueprintAnswer")
_text("22ced28b5ecb08348b35daa51ab112b1", "ef6faada-c7c6-4c63-b1d6-f19a00da9c17", '"Leave the stolen jewelry and get out of my sight. I\'ll let you go."', kind="BlueprintAnswer")
_text("5a5a533c9ce630a48b877f9a194840cb", "b46d5fa9-4ea9-4e7a-9997-b95c458bd095",
      "The wedding souls have returned to Drezen through the Commander's bargain, but their captor remains at large. Arsinoe has traced the place where Sunhammer kept them to the Worldwound. Seelah intends to confront the jeweler and his cult, and recover what he stole from the families. Her friends have suffered for this wedding. Bringing them home has not settled her doubts.", field="Description", kind="BlueprintQuest")
_text("7ac73c0b5de939b4b824a0aac54ba5f2", "ef5f2b7e-8e8c-4338-a8c1-acce1e65618f",
      "Arsinoe's search for the souls revealed a cave beneath Gravestone Rock, at the edge of the Winged Wood. The wedding guests have since been ransomed, but the cave may still shelter Sunhammer and his cult. Elan has gone ahead to keep watch. The Commander and Seelah must join him there.", field="Description", kind="BlueprintQuestObjective")
_text("83527eddea019674cb123a6a52bdf169", "8f8bb69c-77fb-4b1a-af7a-589fa79bcb17", "Find Sunhammer and recover the stolen jewelry", field="Title", kind="BlueprintQuestObjective")
_text("83527eddea019674cb123a6a52bdf169", "e07e3559-8973-46ee-8c3f-85326d63c8aa",
      "The cave is a Baphomite hideout. The wedding souls are already home, but Sunhammer and the stolen settings remain within. Retrieving them without a fight seems unlikely.", field="Description", kind="BlueprintQuestObjective")
_text("5b1e04caadc42114281d29db76c19c4f", "fe6c829a-52b3-489e-814f-b9cbe22a8cd6", "Bring the wedding jewelry back to Drezen", field="Title", kind="BlueprintQuestObjective")
_text("5b1e04caadc42114281d29db76c19c4f", "884bf99f-bd1e-42ea-ac54-996fe4e8dddb",
      "Seelah has the empty wedding settings. Arsinoe is gathering the recovered patients and their families at the Drezen infirmary. The Commander should attend and deliver what was taken from them.", field="Description", kind="BlueprintQuestObjective")
_text("ba857f1c903988f47a70a9d6a2d861fa", "247343ee-0c87-4495-9857-310cc31fa663",
      "Jannah, the convicted deserter, has asked to join her friends in finding Sunhammer and confronting his cult. The wedding guests are already home; the hunt for their captor continues.", field="Description", kind="BlueprintQuestObjective")

# Sibling sweep: pursuit, reconnaissance and separated grief.
_text('dc3a376f09759574f997995e8f07689a', '1e776184-f15d-4a8a-9e96-830c5e929e6c',
      '"We\'re finally here! The guests are home, but I keep thinking about what Sunhammer did to them. He must be stopped."', kind='BlueprintCue')
_text('5c09123a07ee1e047a292c542cce6b74', 'cb16d5c5-6f75-4238-9d9d-957abc3aa5a8',
      '{n}Kiana smiles sadly.{/n} "I knew the risks when I married a crusader. Leaving him didn\'t make me forget them. I thought he would come home, and we would have time to get used to being apart."', kind='BlueprintCue', separated=True)
_text('5d02b3f1d1f6774419ea9fd3795596e8', '12e922e5-7d4c-4e06-a130-765d91876379',
      '"What happened to the victims while we were away?"', kind='BlueprintAnswer')
_text('56f96d3f22dac0942890ebc8dafdfc56', '869d65f2-fb96-4999-9355-fd6a5c1719d1',
      '"We don\'t know what\'s down there. But think about who started all this: Darek Sunhammer and his damned trinkets! We did some digging. We believe he\'s one of Baphomet\'s cultists. Their methods, their magic, their way of infiltrating society... it fits. You bought the souls back, but he may still be hiding with his friends in the Wound."', kind='BlueprintCue')
_text('6cac7bac2baea854d9c52b1d89046cd8', '8515f2a6-a926-49a3-a566-f60b4e1dff3d',
      '{n}Elan shakes his head.{/n} "My apologies, Commander. Kiana and I have separated. That doesn\'t mean I can forget what happened to her... or let the man who did it go."', kind='BlueprintCue', separated=True)

# Authored history repair: romance closure cannot undo a rescue or a separation.
# Native dialogue itself still decides whether its speaker is present.
_scenes = {s["Id"]: s for s in SCENES}
for _guid, _edit in NATIVE_EPILOGUE_EDITS.items():
    _field = _guid + "/Text"
    _variants = [_edit, *_edit.get("Variants", [])]
    _history = []
    for _variant in _variants:
        _scene = _scenes[_variant["Replacement"]]
        _when = copy.deepcopy(_variant["When"])
        # An individual release must carry its original con receipt, never a bare return.
        for _group in _when:
            if kt.RETURNED in _group and kt.ROBBED not in _group:
                _group.append(kt.ROBBED)
        _history.append(dict(Text=_scene["Nodes"][0]["Text"], When=_when,
                             Forbids=list(dict.fromkeys([*_scene.get("Forbids", []),
                                 *([kt.DOG] if any(kt.RETURNED in g for g in _when) else [])]))))
    NATIVE_TEXT_EDITS[_field] = dict(Type="BlueprintCue", Key=_edit["Key"], Variants=_history)
for _guid, _edit in NATIVE_ANSWER_EDITS.items():
    NATIVE_TEXT_EDITS[_guid + "/Text"]["Variants"][0]["Text"] = _edit["Text"]

# The same wedding-to-widow compression is false after an early rescue without separation.
NATIVE_TEXT_EDITS["aebbc1845e827dd4da4e28014e7b4162/Text"]["Variants"].extend([
    dict(Text='{n}Kiana\'s hands are clasped to her chest. There is a dazed look in her eyes.{/n} "We survived that wedding. I heard him talk about what we would do afterwards... I thought we would have time."',
         When=HOME_WORLDS, Forbids=["kiana.separated"]),
    dict(Text='{n}Kiana\'s hands are clasped to her chest. There is a dazed look in her eyes.{/n} "You brought me back. I thought Elan would come home too... He was going after our guests. I kept their names for him."',
         When=PARTIAL_WORLDS, Forbids=["kiana.separated", kt.DOG]),
])

# The registered journal adapter and this field adapter share the current wording.
# Harmony prefix order must not select an obsolete account of the same rescue.
from storylines.native_overrides import JOURNALS as _journals
for _guid, (_description_key, _title_key, _title, _description) in _journals.items():
    for _name, _wording in (("Title", _title), ("Description", _description)):
        if _guid + "/" + _name in NATIVE_TEXT_EDITS:
            NATIVE_TEXT_EDITS[_guid + "/" + _name]["Variants"][0]["Text"] = _wording

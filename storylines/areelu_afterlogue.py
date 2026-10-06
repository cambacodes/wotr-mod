"""Areelu's afterlogue line for a continuing romance (GLOBAL E14i; Writer/handoffs/trickster/areelu-vorlesh.md).

The native afterlogue (World/Dialogs/Epilogues_afterlogues, dialog 57e18f51) is Areelu speaking to Pharasma in the
Boneyard after her death. Its first cue, Cue_0001 5b567bdd ("And what of me, the writer of these words..."), continues
(Strategy First) into one line about how her life ended, then into Cue_0007 ("I have recounted the story of my life for
you, Pharasma") and the goddess's verdict. Two of those lines contradict a route that kept her alive with the Commander:

- Cue_0004 825786e8 (not AreeluRedeemed, not AreeluDead): "...an isolated cottage far from everyone, needed by none,
  discovered by none." This is the punchline world (trickster.cheated_death with no native death etude): the half-demon
  witch spared and kept.
- Cue_0005 1b53c189 (the fallback, e.g. AreeluDead, which the Trickster sacrifice also starts): "...my life ended along with
  it." This is the rewrite on the collected stake (areelu.trickster.rewritten): the graft drawn, a mortal woman.

E14i replaces each with her own line, read only, in the same chain (the replacement keeps the native continuation into
Cue_0007, so Pharasma's verdict on her is unchanged: she is still judged for what she did). The When groups mirror the
report pages (areelu_trickster.report): the wager struck and on screen, she survives, committed or late-committed, and
nothing that closes or burns the romance. Warning-only: a drifted cue keeps its native line and nothing degrades.
"""
import copy

from storylines.native_overrides import register_legacy

from story_format import n, scene

from storylines import areelu_trickster as at

SCENES = []
PARENT = "5b567bdd747e497cb9f6984b1ca1dfc8"      # Epilogues_afterlogues/Cue_0001 (its Continue lists the life-end lines)
DIALOG = "57e18f5158904030a84a772fb361ceb4"      # Epilogues_afterlogues/Epilogues_afterlogues_dialogue (FirstCue = Cue_0001)
CUE_0004 = "825786e8c5db4511ae30950bb286f0e9"    # the cottage
CUE_0005 = "1b53c189b767412f921b8294b980a51c"    # "my life ended along with it"

# The report's romance state: committed, or late-committed without having declined (DECLINED is lifted by COMMITTED).
COMMITS = [[at.COMMITTED], [at.LATE_COMMITTED, "!" + at.DECLINED]]
CLOSES = ["!" + at.STAKE_ONLY, "!" + at.CLOSED, "!" + at.BURNED, "!" + at.INCINERATED, "!" + at.SAC_WOUND, "!" + at.SAC_BEFORE]
BASE = ["trickster.ever", at.STRUCK, at.WAGERED, at.SURVIVES, *CLOSES]
REWRITTEN = [BASE + [at.REWRITTEN] + c for c in COMMITS]
SPARED = [BASE + [at.CHEATED, "!" + at.SAC_TRICK, "!" + at.FIGHT] + c for c in COMMITS]

LINE_SPARED = "areelu.trickster.afterlogue.spared"
LINE_MORTAL = "areelu.trickster.afterlogue.mortal"


def line(id, text):
    SCENES.append(scene(id, "", "AreeluEpilogue", 6, "", [n("line", "Areelu", text, portrait="Areelu")],
                        requires=("trickster.ever", at.STRUCK, at.SURVIVES), last=99, Relationship="areelu"))


line(LINE_SPARED, '"I was defeated. The victor spared my life, and then did something I had not predicted: kept it. Not as a '
     'boon, and not as charity, but the way one keeps a wager that has not been settled. I lived out my remaining days '
     'across a hallway from {mf|him|her}, observing, in company I chose, and never relieved of my purpose."')
line(LINE_MORTAL, '"I was defeated, and the one I had tried to transform made a joke of my death and collected my power '
     'instead. I lived the rest of my days as a mortal woman under {mf|his|her} roof, without magic, still taking notes. My '
     'experiment did not end in failure. It ended in a result I had not predicted, and I never finished writing it up."')

NATIVE_EPILOGUE_EDITS = {
    CUE_0004: dict(Parent=PARENT, Dialog=DIALOG, Key="cd04e9ab-c34b-49ce-b0a7-25f064571101", Replacement=LINE_SPARED,
                   When=SPARED, KeepNativeImage=False, Variants=[]),
    CUE_0005: dict(Parent=PARENT, Dialog=DIALOG, Key="102a4671-6e9d-45b6-a801-32d1706c9698", Replacement=LINE_MORTAL,
                   When=REWRITTEN, KeepNativeImage=False, Variants=[]),
}


def integrate(payload):
    """Register the lines and the E14i edits (after areelu_trickster)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS)

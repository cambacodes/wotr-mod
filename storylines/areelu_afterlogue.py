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
report pages (areelu_trickster.report): the wager struck and on screen, she survives, accepted company, and
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

# A wager earns survival work; only her accepted raise earns company.
COMMITS = [[at.COMMITTED]]
CLOSES = ["!" + at.STAKE_ONLY, "!" + at.CLOSED, "!" + at.BURNED, "!" + at.INCINERATED, "!" + at.SAC_WOUND, "!" + at.SAC_BEFORE]
BASE = ["trickster.now", at.STRUCK, at.WAGERED, at.SURVIVES, *CLOSES]
REWRITTEN = [BASE + [at.REWRITTEN] + c for c in COMMITS]
SPARED = [BASE + [at.CHEATED, "!" + at.SAC_TRICK, "!" + at.FIGHT] + c for c in COMMITS]

LINE_SPARED = "areelu.trickster.afterlogue.spared"
LINE_MORTAL = "areelu.trickster.afterlogue.mortal"


def line(id, text, requires=None):
    SCENES.append(scene(id, "", "AreeluEpilogue", 6, "", [n("line", "Areelu", text, portrait="Areelu")],
                        requires=requires or ("trickster.now", at.STRUCK, at.SURVIVES), last=99, Relationship="areelu"))


# AUTHORED: retrospective facts remain true through kept/filed/burned report
# endings. A read-only epilogue choice cannot authorize lifelong cohabitation.
line(LINE_SPARED, '"The victor spared my life. Neither the wager nor what followed it extinguished my purpose. '
     'I chose the Commander\'s company for a time. My child\'s soul remained unresolved."')
line(LINE_MORTAL, '"The Commander collected my graft instead of my life. Without magic, I continued my work. '
     'I chose company; I did not surrender my purpose. Neither the wager nor the years that followed returned my child."')

# AUTHORED DLC-tier dependent rewrites: exact survival/return receipts, never
# a letter, an affair, or the obsolete late_committed predicate. Pharasma's
# native judgment and continuation remain unchanged in every variant.
NEUTRAL_SPARED = "areelu.trickster.afterlogue.spared_wager"
NEUTRAL_MORTAL = "areelu.trickster.afterlogue.mortal_wager"
RETURN_WITCH = "areelu.trickster.afterlogue.return_witch"
RETURN_MORTAL = "areelu.trickster.afterlogue.return_mortal"
FATE_BASE = ["trickster.now", at.STRUCK, at.WAGERED, "!" + at.CLOSED, "!" + at.STAKE_ONLY, "!" + at.DECLINED, "!" + at.INCINERATED,
             "!" + at.SAC_WOUND, "!" + at.SAC_BEFORE]
NEUTRAL_REWRITE = [FATE_BASE + [at.REWRITTEN, "!" + at.COMMITTED]]
NEUTRAL_KEEP = [FATE_BASE + [at.CHEATED, "!" + at.SAC_TRICK, "!" + at.FIGHT, "!" + at.DRAWN, "!" + at.COMMITTED]]
RETURN_BASE = ["trickster.now", at.STRUCK, at.WAGERED, "!" + at.DIED]
RETURN_RECEIPTS = [["lastcall.h2", "trickster.commander_back", "!iomedae.appointment_kept",
                    "!iomedae.trickster.rescued"], ["iomedae.appointment_kept"], ["iomedae.trickster.rescued"]]
RETURN_WORLDS = [RETURN_BASE + r for r in RETURN_RECEIPTS]
RETURN_WITCH_WORLDS = [r + ["!" + at.DRAWN] for r in RETURN_WORLDS]
RETURN_MORTAL_WORLDS = [r + [at.DRAWN] for r in RETURN_WORLDS]
line(NEUTRAL_SPARED, '"The Commander spared my life. Neither of us forfeited it in the rift. '
     'I kept my notes, my power, and the purpose for which I had opened the Wound."')
line(NEUTRAL_MORTAL, '"The rift took the essence stored in the Commander\'s crystal. I lived without the graft. '
     'The wager bought that experiment; it did not dispose of what remained of me."')
line(RETURN_WITCH, '"The Commander went into the Wound and returned. I remained alive, with the Abyss still in me. '
     'What followed did not settle my child\'s fate. I continued my work."', requires=("trickster.now", at.STRUCK))
line(RETURN_MORTAL, '"The Commander went into the Wound and returned. My graft had already been collected; '
     'I remained without magic. I continued the work I could still do, and my child\'s fate remained unresolved."',
     requires=("trickster.now", at.STRUCK))

def spared_variants():
    return [dict(Replacement=NEUTRAL_SPARED, When=NEUTRAL_KEEP, KeepNativeImage=False),
            dict(Replacement=RETURN_WITCH, When=RETURN_WITCH_WORLDS, KeepNativeImage=False),
            dict(Replacement=RETURN_MORTAL, When=RETURN_MORTAL_WORLDS, KeepNativeImage=False)]

NATIVE_EPILOGUE_EDITS = {
    CUE_0004: dict(Parent=PARENT, Dialog=DIALOG, Key="cd04e9ab-c34b-49ce-b0a7-25f064571101", Replacement=LINE_SPARED,
                   When=SPARED, KeepNativeImage=False, Variants=spared_variants()),
    CUE_0005: dict(Parent=PARENT, Dialog=DIALOG, Key="102a4671-6e9d-45b6-a801-32d1706c9698", Replacement=LINE_MORTAL,
                   When=REWRITTEN, KeepNativeImage=False,
                   Variants=[dict(Replacement=NEUTRAL_MORTAL, When=NEUTRAL_REWRITE, KeepNativeImage=False)]),
}


def integrate(payload):
    """Register the lines and the E14i edits (after areelu_trickster)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS)

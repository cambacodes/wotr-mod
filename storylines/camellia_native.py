"""Camellia's native departure slides on the Trickster (Writer/handoffs/trickster/camellia.md, Polish pass residual 1).

Her native companion page (Epilogues/BookPage_0347 503164ff, CueSequence_Companions; shown while Camelia_Companion is in
the party, dead allowed, Ex not) says she vanished, or left the Commander, or went to Varisia as Mireya. Once the route
has kept her (`epilogue.kept`) or she has named her terms (`epilogue.commit`), those slides contradict the pages that
follow them. E14d replaces or hides them, read only (CamelliaRomance and the ending etudes stay as they are):

- Kept (committed, returned, not closed): the lead slide is replaced (exactly one lead plays in every native state:
  Cue_0392 or Cue_0544 with the companions' semidivine power, Cue_28 romance, Cue_38_master romance + sacrifice, Cue_0386
  no romance, which also drops its Cue_0387 continuation, the dagger at the Commander's heart). The follow-ons Cue_16
  (Mireya in Varisia), Cue_0391 (came back, left again) and Cue_0390 (Mireya's lovers) are hidden.
- Terms named, uncommitted (`epilogue.commit`: she left, and came back in the spring to stay): the native "vanished" lead
  stays true. Only Cue_0391 ("she left again") is hidden.
- Closed, declined or never returned: every native slide plays.

Every edit and suppression is warning-only (NativeEpilogueEdit.Reviewed, DegradeOnRefusal false): a drifted cue keeps its
native text and no relationship is touched (the 252ccf6 lesson). Save names: native-edit.<cue>[.<replacement>], new.
"""
import copy

from storylines.native_overrides import register_legacy

from story_format import n, scene

from storylines import camellia_trickster as ct

SCENES = []
REL = ct.REL
PAGE = "503164ff04ac64543ba42561ea9f970f"        # World/Dialogs/Epilogues/BookPage_0347
COMPANIONS = "fec3b6f28610c8a48a239f148ed3ed60"  # World/Dialogs/Epilogues/CueSequence_Companions

CUE_0392 = "84f892d388bba01489145ecd631f23a2"    # TE + Q3_TheFinalDrop completed: euphoria passed, she disappeared
CUE_0544 = "c1b1da84c12d3ac448ec65b4342ce77f"    # TE, Q3 not completed: she refused to share the power
CUE_28 = "4ed8e9723359441dae10ad3068d3f2c7"      # CamRomDefault/CamRomTrue, no sacrifice: "Camellia simply vanished."
CUE_38 = "36a07840d25540eeac6b1c6631196bcc"      # romance + Ending_PlayerSacrifice: the ruins of Threshold
CUE_0386 = "5011dfa46fbb0464ab624d78bcfbd483"    # no romance: "on a moonless night, she vanished." (-> Cue_0387)
CUE_16 = "3617a648c06a45d1807fde65aedafb06"      # every non-TE state: "an assassin by the name of Mireya arrived in Varisia"
CUE_0391 = "430ce9767d3ede2479ff9d6aee432304"    # CamRomTrue, no sacrifice: she came back, and left again
CUE_0390 = "e9a183135b8289544a3144dcf8151920"    # romance: Mireya's lovers in the Varisian underworld (shared text)

# When groups (E14d: an OR of AND-groups; "!x" holds while x is absent). Mirrors epilogue.kept / epilogue.commit: the
# sacrifice is lifted only by the Commander's return, the kicked_out flag only when it is the kill (killed_held).
ALIVE_GROUPS = [[s, k] for s in ("!sacrifice", "trickster.commander_back") for k in ("!" + ct.KICKED, ct.P + "killed_held")]
KEPT = [["trickster.ever", ct.RET, ct.COMMITTED, "!" + ct.CLOSED, *g] for g in ALIVE_GROUPS]
TERMS = [["trickster.ever", ct.RET, ct.TERMS, "!" + ct.COMMITTED, "!" + ct.CLOSED, "!" + ct.DECLINED, *g] for g in ALIVE_GROUPS]

P = ct.P + "epilogue.native_"
NATIVE_TE_STAYED = P + "te_stayed"
NATIVE_TE_OWN_PATH = P + "te_own_path"
NATIVE_STAYED = P + "stayed"
NATIVE_THRESHOLD = P + "threshold_waited"
NATIVE_STAYED_PLAIN = P + "stayed_plain"


def slide(id, text):
    SCENES.append(scene(id, "", "CamelliaEpilogue", 6, "", [n("page", "Narrator", "{n}" + text + "{/n}", portrait="Camellia")],
                        requires=("trickster.ever", ct.RET, ct.COMMITTED), last=99, Relationship=REL))


slide(NATIVE_TE_STAYED, "Camellia's delight in semidivine power soon passed. Killing without danger bored her. She stayed beside the Commander, whose tricks she still could not predict, and watched for something that might surprise her.")
slide(NATIVE_TE_OWN_PATH, "Camellia refused to share in the Commander's semidivine power. She had her own path to follow. "
      "Where it led, she never told anyone, except that every evening it passed the Commander's door, and stopped there.")
slide(NATIVE_STAYED, "Camellia remained with the Commander after the war. She complained of dull company, made new acquaintances, and kept her own hours. When she returned to the Commander's rooms, she brought wine and a small, clean knife. She expected to be entertained.")
slide(NATIVE_THRESHOLD, "After the victory at Threshold, Camellia refused to join the crusader army retreating to Drezen. "
      "She waited among the ruins of the empty fortress, alone, listening to the wind for a familiar voice. When it came "
      "back, she went where it went.")
slide(NATIVE_STAYED_PLAIN, 'After the war, Camellia stayed with the Commander. She wore her finest dresses to dinner and watched the guests with an attention they mistook for kindness. In private she kept her knife within reach. The Commander could still make her laugh, and she stayed to see what would happen next.')

NATIVE_EPILOGUE_EDITS = {
    CUE_0392: dict(Page=PAGE, Sequence=COMPANIONS, Key="8f73fe38-c791-4d7e-9bd0-553f1f0b07aa", Replacement=NATIVE_TE_STAYED,
                   When=KEPT, KeepNativeImage=True, Variants=[]),
    CUE_0544: dict(Page=PAGE, Sequence=COMPANIONS, Key="d494dcd7-7f4f-4b8b-a8d7-7dcb41998909", Replacement=NATIVE_TE_OWN_PATH,
                   When=KEPT, KeepNativeImage=False, Variants=[]),
    CUE_28: dict(Page=PAGE, Sequence=COMPANIONS, Key="aee7c6bf-fbe1-4288-83e7-3ff3bd4545ad", Replacement=NATIVE_STAYED,
                 When=KEPT, KeepNativeImage=False, Variants=[]),
    CUE_38: dict(Page=PAGE, Sequence=COMPANIONS, Key="af56e46e-7e82-4e22-9951-8ddc37dd015f", Replacement=NATIVE_THRESHOLD,
                 When=KEPT, KeepNativeImage=False, Variants=[]),
    CUE_0386: dict(Page=PAGE, Sequence=COMPANIONS, Key="4dd21f1d-4280-4598-851d-bbc6bbf2f3e4", Replacement=NATIVE_STAYED_PLAIN,
                   When=KEPT, KeepNativeImage=False, Variants=[]),
}

NATIVE_EPILOGUE_SUPPRESSIONS = {
    CUE_16: dict(Page=PAGE, Sequence=COMPANIONS, Key="de512bb2-4d4d-4ca2-b20d-9b2d6384c802", Relationship=REL, When=KEPT),
    CUE_0390: dict(Page=PAGE, Sequence=COMPANIONS, Key="f31377a1-a78e-47f2-bc10-1721eac2f9c1", Relationship=REL, When=KEPT),
    CUE_0391: dict(Page=PAGE, Sequence=COMPANIONS, Key="4819461c-331c-4872-a077-49115a7c9ad7", Relationship=REL, When=KEPT + TERMS),
}


def integrate(payload):
    """Register the scenes and the edits (after camellia_trickster.integrate)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS, suppressions=NATIVE_EPILOGUE_SUPPRESSIONS)
    # eng8-q8e begin: final outcome parity is applied after all engine appenders.
    # Living commitments and terms are covered along with paid returns; IDs stay fixed.
    # eng8-q8e end

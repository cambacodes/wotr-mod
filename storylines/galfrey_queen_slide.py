"""Galfrey's native Queen slide on a Trickster run where she came back and took the crown again (engine-q2 item 5).

Epilogues/CueSequence_Queen (bb9d36fd) shows BookPage_0255 Cue_0259 (f5906acd) or BookPage_0258 Cue_0502 (becde706) while
GalfreyDead (a4f20ae9, the route's galfrey.dead) is Playing. Both cues share one text (e61f5ab8): "Queen Galfrey died leaving
no direct heir ... none was able to win the love of the people". On the Trickster path her return (galfrey.trickster.returned)
lifts the death but leaves the native etude Playing, so a Galfrey who reclaimed the crown (galfrey.trickster.crown_reclaimed)
was mourned by the very slide that should crown her. Each cue gets an E14d replacement, read only and warning-only on refusal
(src/NativeEpilogueEdit.cs Reviewed: ShowOnce false, no OnShow/OnStop, answers, continuation or components; the parent mod
names neither cue, their pages nor the sequence). The When reads trickster.ever: the return and the crown are Trickster acts
already done (earned_presence_lint T6a). Kept apart from the route files so it merges cleanly with claude/pol-galfrey.
"""
import copy

from storylines.native_overrides import register_legacy

from story_format import n, scene

CUE_0259 = "f5906acda82efd5468cb72aff2e68f7e"   # World/Dialogs/Epilogues/Cue_0259 on BookPage_0255
CUE_0502 = "becde70692b74ab4eba1d0cf82d2958f"   # World/Dialogs/Epilogues/Cue_0502 on BookPage_0258 (shared text)
PAGE_0255 = "6c50623b48ba8204686e2e426ac00425"
PAGE_0258 = "d9cc48a31f994c64f88c5dec322805a4"
QUEEN = "bb9d36fd37d74bf4792931d6052a7d44"       # World/Dialogs/Epilogues/CueSequence_Queen
KEY = "e61f5ab8-ec4c-439f-b035-802558deebe0"     # the shared string both cues show

RETURNED = "galfrey.trickster.returned"
CROWN = "galfrey.trickster.crown_reclaimed"
WHEN = [["trickster.ever", RETURNED, CROWN]]

# Owlcat's Queen-slide register: the realm first, the woman as her people saw her. Pending an independent prose pass.
TEXT = ('{n}Mendev had mourned Galfrey when she returned to Nerosyan. She had the royal crypt opened and named the knight buried under her name. His daughter received him for burial, and the court received an account of the deception.{/n} {n}Galfrey took the crown again. The regents returned to their offices, and the petitions that had gathered in her absence reached her table. Years later she refused another cup of the elixir and laid down the crown. This time Mendev knew its Queen was leaving alive.{/n}')

REPLACEMENTS = {CUE_0259: ("galfrey.native.queen_reclaimed", PAGE_0255), CUE_0502: ("galfrey.native.queen_reclaimed_twin", PAGE_0258)}

# Owner "Epilogue", not "GalfreyEpilogue": these replace native realm slides and are not pages of her route (Rules.IsNativeReplacement).
SCENES = [scene(rid, "", "Epilogue", 6, "", [n("page", "Narrator", TEXT)],
                requires=("trickster.ever", RETURNED, CROWN), forbids=("galfrey.closed", "sacrifice"), last=99,
                Relationship="galfrey", ForbidOverrides={"sacrifice": "trickster.commander_back"})
          for rid, _ in REPLACEMENTS.values()]

NATIVE_EPILOGUE_EDITS = {cue: dict(Page=page, Sequence=QUEEN, Key=KEY, Replacement=rid, When=WHEN, KeepNativeImage=False, Variants=[])
                         for cue, (rid, page) in REPLACEMENTS.items()}


def integrate(payload):
    """Register the two replacement slides and their edits (after the Galfrey route)."""
    if "galfrey" not in payload["Relationships"]:
        return
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS)

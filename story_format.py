"""Small authoring helpers shared by the original route and its expansion."""

# Short path names accepted by c(mythic=...); any Kingmaker Mythic enum name is accepted as-is.
MYTHIC_PATHS = {"Aeon", "Angel", "Azata", "Demon", "Devil", "Dragon", "Legend", "Lich", "Locust", "Trickster"}
MYTHIC_NAMES = {"PlayerIs" + p for p in MYTHIC_PATHS} | {p + "Unlocked" for p in MYTHIC_PATHS}
ALIGNMENT_DIRECTIONS = {"LawfulGood", "NeutralGood", "ChaoticGood", "LawfulNeutral", "TrueNeutral", "ChaoticNeutral",
                        "LawfulEvil", "NeutralEvil", "ChaoticEvil", "Good", "Evil", "Lawful", "Chaotic"}


def c(text="Continue", next=None, flags=(), requires=(), forbids=(), abort=False, revive=None, check=None,
      mythic=None, native_next=None, alignment=None):
    """One answer. Native effects (E5), each validated again by Rules.Validate:
    mythic="Trickster"          native [Trickster] answer: MythicRequirement PlayerIsTrickster + the mythic-choice achievement counter
    native_next="<cue guid>"    terminal choice of an inline (NativeReturnCue) scene continues into that native cue of the same dialog
    alignment=("Chaotic", 1)    native AlignmentShift (direction, points > 0) applied on select
    """
    choice = dict(Text=text, Next=next, Set=list(flags), Requires=list(requires), Forbids=list(forbids), Abort=abort)
    if revive is not None:
        choice["Revive"] = revive
    if check is not None:
        choice["Check"] = check
    if mythic is not None:
        name = "PlayerIs" + mythic if mythic in MYTHIC_PATHS else mythic
        if name not in MYTHIC_NAMES:
            raise ValueError("Unknown mythic requirement: %r" % (mythic,))
        choice["Mythic"] = name
    if native_next is not None:
        if next is not None or check is not None or abort:
            raise ValueError("native_next must end the RRT branch (no next, check or abort)")
        choice["NativeNext"] = native_next
    if alignment is not None:
        direction, value = alignment
        if direction not in ALIGNMENT_DIRECTIONS or not isinstance(value, int) or value <= 0:
            raise ValueError("Invalid alignment shift: %r" % (alignment,))
        choice["Alignment"] = dict(Direction=direction, Value=value)
    return choice


def n(id, speaker, text, *choices, portrait=""):
    return dict(Id=id, Speaker=speaker, Text=text.strip(), Choices=list(choices) or [c()], Portrait=portrait)


def scene(id, title, owner, chapter, entry, nodes, requires=(), forbids=(), delay=0, last=5, optional=False, **extra):
    return dict(Id=id, Title=title, Owner=owner, MinChapter=chapter, MaxChapter=last,
                Entry=entry, Nodes=nodes, Requires=list(requires), Forbids=list(forbids),
                DelayHours=delay, Optional=optional, **extra)

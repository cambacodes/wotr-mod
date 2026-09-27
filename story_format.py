"""Small authoring helpers shared by the original route and its expansion."""

# Short path names accepted by c(mythic=...); any Kingmaker Mythic enum name is accepted as-is.
MYTHIC_PATHS = {"Aeon", "Angel", "Azata", "Demon", "Devil", "Dragon", "Legend", "Lich", "Locust", "Trickster"}
MYTHIC_NAMES = {"PlayerIs" + p for p in MYTHIC_PATHS} | {p + "Unlocked" for p in MYTHIC_PATHS}
CRUSADE_RESOURCES = {"Finances", "Materials", "Favors"}
ALIGNMENT_DIRECTIONS = {"LawfulGood", "NeutralGood", "ChaoticGood", "LawfulNeutral", "TrueNeutral", "ChaoticNeutral",
                        "LawfulEvil", "NeutralEvil", "ChaoticEvil", "Good", "Evil", "Lawful", "Chaotic"}


def c(text="Continue", next=None, flags=(), requires=(), forbids=(), abort=False, revive=None, check=None,
      mythic=None, native_next=None, alignment=None, crusade=None, remove_item=None):
    """One answer. Native effects (E5), each validated again by Rules.Validate:
    mythic="Trickster"          native [Trickster] answer: MythicRequirement PlayerIsTrickster + the mythic-choice achievement counter
    native_next="<cue guid>"    terminal choice of an inline (NativeReturnCue) scene continues into that native cue of the same dialog
    alignment=("Chaotic", 1)    native AlignmentShift (direction, points > 0) applied on select
    crusade=("Finances", -500)  native crusade resource change (Finances/Materials/Favors; Chapter 3+ scenes)
    remove_item="<item guid>"   native removal of one item; the GUID must be in Story.RemovableItems and the choice or
                                scene must Require an InventoryItems key bound to it
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
    if crusade is not None:
        resource, amount = crusade
        if resource not in CRUSADE_RESOURCES or not isinstance(amount, int) or amount == 0:
            raise ValueError("Invalid crusade cost: %r" % (crusade,))
        choice["Crusade"] = dict(Resource=resource, Amount=amount)
    if remove_item is not None:
        choice["RemoveItem"] = remove_item
    return choice


def p(text, requires=(), forbids=(), any_groups=()):
    """E14c: one conditional paragraph of an epilogue page (appended after the node text, in order)."""
    return dict(Text=text.strip(), Requires=list(requires), Forbids=list(forbids), AnyGroups=[list(g) for g in any_groups])


def n(id, speaker, text, *choices, portrait="", paragraphs=(), speaker_unit=None):
    """speaker="conversant" (the native dialog's conversant) or speaker_unit="<BlueprintUnit guid>" (E14f) give an inline cue a
    native speaker; paragraphs=(p(...), ...) are E14c epilogue paragraphs."""
    node = dict(Id=id, Speaker=speaker, Text=text.strip(), Choices=list(choices) or [c()], Portrait=portrait)
    if speaker_unit is not None:
        node["SpeakerUnit"] = speaker_unit
    if paragraphs:
        node["Paragraphs"] = list(paragraphs)
    return node


def scene(id, title, owner, chapter, entry, nodes, requires=(), forbids=(), delay=0, last=5, optional=False, **extra):
    """One scene. Common **extra fields: Relationship, AnswerLists, Remote, Areas, Chapters, ContactUnit, ForbidOverrides,
    NativeReturnCue, RequiresAnyGroups, TricksterDevice / TricksterState (ER-2), EpilogueAfter (ER-3), and E13 entry effects:
    EntryMythic="PlayerIsTrickster" (a Mythic enum name) and EntryAlignment=dict(Direction="Chaotic", Value=1) put the native
    mythic requirement/icon + achievement counter and an AlignmentShift on the entry answer of a physical scene."""
    return dict(Id=id, Title=title, Owner=owner, MinChapter=chapter, MaxChapter=last,
                Entry=entry, Nodes=nodes, Requires=list(requires), Forbids=list(forbids),
                DelayHours=delay, Optional=optional, **extra)


def reaction(owner, id, requires, text, answer_list=None, remote=False, forbids=(), *, relationship=None, entry=None,
             title=None, chapter=1, last=5, delay=0, speaker=None, portrait="", flags=(), **extra):
    """E6: a one-node companion or NPC reaction to a device (TT-25, playbook P4).

    Attached to the reactor's native answer list (answer_list="<guid>") or delivered as a rest letter (remote=True).
    The scene belongs to the device's relationship (the id prefix unless relationship= is given) and is tagged
    Reaction=True: Rules.Validate keeps it to one node of terminal choices that never set a ClosedFlag, never touch
    another relationship's state and never forbid another relationship's Started/Closed/Committed flag.
    """
    if bool(answer_list) == bool(remote):
        raise ValueError("reaction %s needs exactly one of answer_list or remote=True" % id)
    if any(f == "closed" or f.endswith(".closed") for f in flags):
        raise ValueError("reaction %s may not close a relationship" % id)
    rel = relationship or id.split(".")[0]
    body = scene(id, title or "%s's word" % owner, owner, chapter,
                 "" if remote else (entry or '"What do you make of what happened?"'),
                 [n("start", speaker or owner, text, c("Continue", flags=flags), portrait=portrait)],
                 requires=requires, forbids=forbids, delay=delay, last=last, Relationship=rel, Reaction=True, **extra)
    if remote:
        body["Remote"] = True
    else:
        body["AnswerLists"] = [answer_list]
    return body

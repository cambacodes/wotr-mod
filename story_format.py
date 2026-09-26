"""Small authoring helpers shared by the original route and its expansion."""


def c(text="Continue", next=None, flags=(), requires=(), forbids=(), abort=False, revive=None, check=None):
    choice = dict(Text=text, Next=next, Set=list(flags), Requires=list(requires), Forbids=list(forbids), Abort=abort)
    if revive is not None:
        choice["Revive"] = revive
    if check is not None:
        choice["Check"] = check
    return choice


def n(id, speaker, text, *choices, portrait=""):
    return dict(Id=id, Speaker=speaker, Text=text.strip(), Choices=list(choices) or [c()], Portrait=portrait)


def scene(id, title, owner, chapter, entry, nodes, requires=(), forbids=(), delay=0, last=5, optional=False, **extra):
    return dict(Id=id, Title=title, Owner=owner, MinChapter=chapter, MaxChapter=last,
                Entry=entry, Nodes=nodes, Requires=list(requires), Forbids=list(forbids),
                DelayHours=delay, Optional=optional, **extra)

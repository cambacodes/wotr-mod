"""Authored Q7-28 native-slide corrections, not new return devices.

The Cue_0311 native checker still reads IrabethDead/AneviaGone after paid
returns. A dead Commander or a refused reconciliation cannot undo that history.
Use existing dig/raise evidence; do not grant returned, commitment or household
eligibility. Append variants so every existing native-edit save name survives.
Native book conditions, actions and continuations stay on q6b's reviewed path.
"""
from story_format import c, n, scene

CUE = "3a3e561c6b05a284d93eb3bff7b712a6"
LEFT_CUE = "ccd140dbf2603734aa323261c2445bec"
ANEVIA = "anevia.trickster.returned"
BETH = "irabeth.trickster.returned"
DUG = "irabeth.trickster.cost.dug_out"
RAISED = "irabeth.trickster.raised_on_record"
BACK = "trickster.commander_back"
PREFIX = "anevia.trickster.epilogue.native_tirabade_"
IPREFIX = "irabeth.trickster.epilogue.native_tirabade_"


def integrate(payload):
    if CUE not in payload.get("NativeEpilogueEdits", {}):
        return
    edit = payload["NativeEpilogueEdits"][CUE]
    # The widow and absent-wife variants must not win over a later true history.
    for variant in edit["Variants"]:
        if variant["Replacement"] in (PREFIX + "widow", PREFIX + "widow_committed"):
            for group in variant["When"]:
                group.extend(("!" + BETH, "!" + DUG, "!" + RAISED))
        if variant["Replacement"] == IPREFIX + "south":
            for group in variant["When"]:
                group.append("!" + ANEVIA)

    def append(target, id, relationship, text, groups, requires, forbids=(), any_groups=(), pair_image=False):
        # Consume Last Call's existing L6 contract even though its active worlds
        # also imply Commander return. These scenes join after lastcall.integrate.
        if "sacrifice" in requires:
            forbids = (*forbids, "lastcall.active")
        payload["Scenes"].append(scene(id, "", relationship.title() + "Epilogue", 6, "", [
            n("page", "Narrator", "{n}" + text + "{/n}", c())], requires=requires,
            forbids=forbids, RequiresAnyGroups=[list(g) for g in any_groups], last=99, Relationship=relationship))
        payload["NativeEpilogueEdits"][target]["Variants"].append(dict(
            Replacement=id, When=groups, KeepNativeImage=not pair_image))

    path = "trickster.ever"
    append(CUE, PREFIX + "survived_pair", "anevia",
        "Irabeth survived Iz. Anevia returned to Drezen on her own terms, but Beth never reconciled with the Commander. "
        "Anevia spoke of the rescue when she chose; she always spoke of Iz first.",
        [[path, ANEVIA, proof, "!" + BETH] for proof in (DUG, RAISED)],
        (path, ANEVIA), (BETH,), ((DUG, RAISED),), pair_image=True)
    append(CUE, IPREFIX + "survived_away", "irabeth",
        "Irabeth survived Iz, but never reconciled with the Commander. Anevia had gone south. News of Beth's survival "
        "followed her, and the Tirabades kept their distance from Drezen.",
        [[path, proof, "!" + BETH, "!" + ANEVIA] for proof in (DUG, RAISED)],
        (path,), (BETH, ANEVIA), ((DUG, RAISED),))
    append(CUE, PREFIX + "bereavement_pair", "anevia",
        "Irabeth outlived Iz, and Anevia returned to Drezen on her own terms. The Commander's death at the Worldwound "
        "changed neither fact. Anevia kept Beth's name out of the eulogies: the crusade had mourned her wife once already.",
        [[path, ANEVIA, proof, "sacrifice", "!" + BACK] for proof in (BETH, DUG, RAISED)],
        (path, ANEVIA, "sacrifice"), (BACK,), ((BETH, DUG, RAISED),), pair_image=True)
    append(CUE, PREFIX + "bereavement_widow", "anevia",
        "Anevia had returned to Drezen, but Beth had not come back from Iz. When the Commander died closing the "
        "Worldwound, she heard the news among people who knew her name. She left again when she chose, on her own terms, "
        "with another name to remember.",
        [[path, ANEVIA, "sacrifice", "!" + BACK, "!" + BETH, "!" + DUG, "!" + RAISED]],
        (path, ANEVIA, "sacrifice"), (BACK, BETH, DUG, RAISED))
    append(CUE, IPREFIX + "survived_bereavement", "irabeth",
        "Irabeth survived Iz. Anevia had gone south, and news of Beth's survival followed her. The Commander later "
        "died closing the Worldwound, with no reconciliation between them.",
        [[path, proof, "sacrifice", "!" + BACK, "!" + BETH, "!" + ANEVIA] for proof in (DUG, RAISED)],
        (path, "sacrifice"), (BACK, BETH, ANEVIA), ((DUG, RAISED),))
    append(LEFT_CUE, PREFIX + "left_bereavement", "anevia",
        "Anevia returned to Drezen after taking Irabeth away from the Commander's betrayal. The Commander died closing "
        "the Worldwound before their grievances were settled. The Tirabades kept their lives and their nightmares; "
        "Anevia never called the sacrifice a pardon.",
        [[path, ANEVIA, "sacrifice", "!" + BACK]],
        (path, ANEVIA, "sacrifice"), (BACK,))

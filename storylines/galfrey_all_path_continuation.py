"""Unintegrated Galfrey continuation prototype with path-specific voice hooks."""
from story_format import c, n, scene

PATH_ETUDES = {
    "Angel": "3a82aba4de71b89458ac82949ed957c4",
    "Azata": "d3b47e973d65c6c46af1cce815d1f6ce",
    "Aeon": "3a040afde22f4b742a2f607354ab17e7",
    "Trickster": "9f486a9c0c9abfc4a952bb22e88a7e96",
    "Demon": "9a3739370f84b0b4196d0e4d326ea3a8",
    "Lich": "11fc5662e0ce8074ea145a022282b879",
    "Devil": "a1db9daf676b36f4d99c6a788a0fe1af",
    "Dragon": "9b193d30c89a20b409fd3dda9bd109bf",
    "Legend": "c6165efcd5571c442ae38d7c0601f2df",
    "Swarm": "4da0ddbe8fb98294cb1826989ab77e4a",
}

GALFREY_ETUDE = "3230b1f42aa8f2e42ba5fef806cf43e9"
NATIVE_ROMANCE_ACTIVE = "c9358d866e0b3844b8d72536ca60e4b4"
AEON_CHANGED_DREZEN_HISTORY = "998b505008f960a4b92e679fbd588098"
DEVIL_GALFREY_AFTER_SEX = "e888c82ffc724a3b9ee041afb61408e5"
DEVIL_INCOMPATIBILITY_CUE = "b3b208e871cd49abacc81b1ea136c89d"
GALFREY_DEAD = "a4f20ae9f6a6c3d4ba204721589470a2"
GALFREY_KILLED_BY_COMMANDER = "eb30187696a04f99aa194859b13a629e"

ETUDES = {
    **{f"path.{name.lower()}": guid for name, guid in PATH_ETUDES.items()},
    "galfrey.native_active": NATIVE_ROMANCE_ACTIVE,
    "galfrey.aeon_history_changed": AEON_CHANGED_DREZEN_HISTORY,
    "galfrey.devil_after_sex": DEVIL_GALFREY_AFTER_SEX,
    "galfrey.dead": GALFREY_DEAD,
    "galfrey.killed_by_commander": GALFREY_KILLED_BY_COMMANDER,
}

# Path access audit. The final field is a concrete work item, not a claim that
# an authored fate intervention already exists or is mechanically possible.
SEEN_CUES = {
    "galfrey.devil_incompatibility_seen": [DEVIL_INCOMPATIBILITY_CUE],
}
PATH_CONTINUATION = {
    "Angel": "Native Chapter 5 duty dialogue includes Angel; the Iz attack answer explicitly excludes Angel. Verify all survival/failure outcomes and locate a post-native-romance actor before continuation.",
    "Azata": "Shared native Iz outcomes apply; no source-backed path-specific death immunity or continuation window is identified. Verify upstream quest state, Queen survival, romance history, and actor contact.",
    "Aeon": "Galfrey reacts to the changed-Drezen-history state as Aeon; the Iz attack outcome still needs tracing against the Aeon campaign state. Preserve her independent judgment of both history and intimacy.",
    "Trickster": "This file only continues an already-active native courtship. It does not meet the bespoke missed-courtship requirement. A separate Chapter 3 entry using the native council invitation is a candidate, but the exact Trickster Council/contact stage and a rejected-romance recovery remain unverified.",
    "Demon": "Shared Iz attack outcome is available to every non-Angel entering that answer; trace Demon-specific hostility, survival and rejection flags before proposing any reunion.",
    "Lich": "Blocked by native conversion: the Lich Galfrey dialogue contains a dedicated answer that breaks the romance, and her later unit is an undead companion. No source-backed restoration of her living body, free will, or voluntary romance has been found.",
    "Devil": "The native Devil aftermath records sex after Devilish Temptation, while the Chapter 5 Devil dialogue offers a try-to-coexist answer and a separate final incompatibility response. This scene is gated on the aftermath and active courtship; any new relationship needs Galfrey's explicit current choice and may still end.",
    "Dragon": "Native Chapter 5 duty dialogue includes Dragon; trace the shared Iz survival and attack states against the Dragon campaign state before attaching the authored continuation.",
    "Legend": "Native Chapter 5 duty dialogue includes Legend; trace the shared Iz survival and attack states against the Legend campaign state before attaching the authored continuation.",
    "Swarm": "Blocked by native consumption: the Swarm-specific Iz answer leads to explicit devouring and starts GalfreyDead. No source-backed soul/body recovery or freely consenting survivor is established.",
}

PATH_FATE_AUDIT = {
    "Angel": {
        "native_evidence": "Chapter 5 duty cue 7a160960668f2ef4180cb56edb8388e9 lists PlayerIsAngel; Iz Answer_0023 c383c70e3b946e24d836329436defa55 excludes Angel.",
        "access": "This Chapter 5 slice requires the native Active courtship etude, which the source describes as started and not failed. Verify the living actor and actual interaction window.",
        "gap": "Trace all Angel Iz location, companion survival, GalfreyDead, and native Active completion and actor-contact consumers.",
    },
    "Azata": {
        "native_evidence": "The audited Chapter 5 duty cue does not list Azata; the shared Iz attack answer has no Azata MythicRequirement of its own.",
        "access": "Requires a source-verified surviving Galfrey and a post-courtship actor window.",
        "gap": "Trace upstream Azata interactions into Iz and verify any path-specific Queen protection or death state.",
    },
    "Aeon": {
        "native_evidence": "The duty cue lists Aeon; native Answer_0041 is reached under MythicAeon_DrezenHistoryChanged and GalfreyWithUs with ReinforcedByAeon polarity variants.",
        "access": "This Aeon variant additionally requires the native MythicAeon_DrezenHistoryChanged state; the changed-history response is not romance consent.",
        "gap": "Trace the full Aeon-to-Iz branch and whether the changed-history decision alters Galfrey survival or later actor availability.",
    },
    "Trickster": {
        "native_evidence": "The audited duty cue does not list Trickster; the source audit identifies separate Trickster Councils but has not verified their stage/contact contract.",
        "access": "This scene is only for an already-active native courtship; the required separate missed-courtship acquisition is documented in TRICKSTER_MISSED_COURTSHIP_PLAN and is not implemented.",
        "gap": "Build a distinct missed-native-courtship entry; map Council stages, quest prerequisites, Galfrey actor presence, native rejection history and Iz survival before writing access mechanics. This chapter 5 continuation is not that acquisition route.",
    },
    "Demon": {
        "native_evidence": "The general Iz attack answer excludes only Angel, so its local condition does not protect Galfrey from Commander-initiated violence on Demon.",
        "access": "Only a living, non-hostile state can enter the draft continuation; a Demon path label cannot erase harm or rejection.",
        "gap": "Trace Demon-specific Iz answers, hostility, all kill actions, GalfreyDead, and whether an accepted native romance can persist past those actions.",
    },
    "Lich": {
        "native_evidence": "Lich answer 861d0e88764e1c249908b9ef60d55289 has PlayerIsLich and completes the native Galfrey romance root; Chapter 5 uses a zombie dialogue; the Lich companion's Nexus state uses Galfrey as an ex companion. GalfreyDead's comment explicitly counts undead as dead.",
        "access": "No romance continuation is authored. A future route first needs proof of a distinct mechanism restoring Galfrey's independent will and a body or state she can choose from; the native conversion itself is not consent.",
        "gap": "Audit the full zombie dialogue and conversion effects, then establish whether a non-coercive release/restoration can occur while the Commander remains Lich and whether Galfrey can explicitly accept or refuse afterward.",
    },
    "Devil": {
        "native_evidence": "The native Devil after-intimacy etude e888c82ffc724a3b9ee041afb61408e5 is annotated Sex with Galfrey after Devilish Temptation quest. Chapter 5 Answer 0011 606acaa9e0674d0b89022b9f60966aa3 leads to Cue_32 b3b208e871cd49abacc81b1ea136c89d, where she says their paths will never cross again. Cue_0032 5c6483b4911e4be4287d2f02260046fc is a different, conciliatory cue.",
        "access": "The current scene requires both the native active-courtship state and the Devil after-intimacy event. It offers a new authored conversation, not proof of continuing desire; Galfrey must state whether she wants another encounter or prefers the native friendship/separation outcome.",
        "gap": "The pre-separation state gate blocks this scene after Cue_32, but the authored repair/reconciliation route after that explicit ending is still missing. Verify sequencing and native dialog reservation so this scene cannot interrupt the native answer/cue chain.",
    },
    "Dragon": {
        "native_evidence": "The duty cue lists Dragon; the shared Iz attack answer does not exclude Dragon.",
        "access": "This Chapter 5 slice requires the native Active courtship state and a verified live Galfrey actor.",
        "gap": "Trace Dragon-to-Iz outcomes, direct Galfrey kill actions, and post-Iz actor availability; no path-specific immunity is inferred.",
    },
    "Legend": {
        "native_evidence": "The duty cue lists Legend; the shared Iz attack answer does not exclude Legend.",
        "access": "This Chapter 5 slice requires the native Active courtship state and a verified live Galfrey actor.",
        "gap": "Trace the Legend transition and Iz outcome against GalfreyDead, native Active courtship completion, and the active companion unit.",
    },
    "Swarm": {
        "native_evidence": "Iz Answer_0074 516217fafda9b194989bd3068289898e is Swarm-only and leads to Cue_0034 0346a8715460fce4e9413ad16af4065b, which describes Galfrey being consumed; the branch starts GalfreyDead.",
        "access": "No romance continuation is authored after this fate. A future authored fate intervention needs a verified surviving soul and a credible restoration effect, then Galfrey's independent choice; no such source support was found.",
        "gap": "Trace all Swarm coronation/Iz paths, confirm whether any non-consuming branch leaves Galfrey alive through endgame, and prove the available recovery magic or fate mechanic can restore her without merely recreating a controllable body.",
    },
}

SCENES = []
# eng7-f6d begin: reuse the living Queen at a real contact; no spawn/return.
HUB = "galfrey.continuation.presence"
PRESENCES = {HUB: dict(Unit="e46927657a79db64ea30758db3f42bb9", Area="2570015799edf594daf2f076f2f975d8",
    Mode="reuse-native", Requires=["galfrey.native_active"],
    Forbids=["galfrey.dead", "galfrey.killed_by_commander"],
    MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub")}
# eng7-f6d end


PATH_PROSE = {'Angel': {'boundary': '{n}She sets down the pen.{/n} "The men trust what they see in you. That makes the orders no '
                       'lighter. I would like one evening when we need not speak for them."',
           'stayed': '{n}She checks the last seal and turns her chair toward you.{/n} "There. Sit closer. I have spent '
                     'enough of the evening looking at a map."'},
 'Azata': {'boundary': '{n}She smooths the folded dispatch.{/n} "This is a ration order. If the seal is broken, a '
                       'hungry quartermaster will call it a forgery. Make your birds from my scrap paper."',
           'stayed': '{n}She puts a spoiled draft beside your elbow.{/n} "That one may fly. This one goes to the '
                     'supply wagons." {n}Her mouth curves.{/n} "You can amuse me after it is signed."'},
 'Aeon': {'boundary': '{n}Her hand rests on the ledger.{/n} "You altered Drezen\'s history. I must still answer for '
                      'the orders I give now. When you speak to me, do not look through me at a woman you expected to '
                      'find."',
          'stayed': '{n}She opens today\'s muster.{/n} "These men are here. Their next march is our concern." {n}She '
                    'brings her chair beside yours.{/n} "So is this conversation. Begin with what you want to say '
                    'today."'},
 'Trickster': {'boundary': '{n}She taps the impossible date.{/n} "Explain this before it reaches the garrison. They '
                           'must know which orders to obey. If you wanted to see me, you could have knocked."',
               'stayed': '{n}She corrects the date and keeps the decree.{/n} "The clerk will have my correction. You '
                         'may have the chair. Try to leave both where they belong."'},
 'Demon': {'boundary': '{n}She draws back from your wrist.{/n} "The men outside heard the anger in your voice. I will '
                       'not have it brought into my council and called strength. Tell me what happened before we speak '
                       'of anything else."',
           'stayed': '{n}She stays standing beside the dispatch table.{/n} "I shall hear the report. We are at war, '
                     'and I need to know what you intend. Do not mistake my staying for approval."'},
 'Devil': {'boundary': '{n}She leaves the contract untouched.{/n} "We chose that night. I shall not deny it. Nor shall '
                       'I sign away my judgment because of it. Speak plainly; you have no need of a contract to tell '
                       'me what you want."',
           'stayed': '{n}She returns the contract.{/n} "I have heard you. The orders still need my seal." {n}She takes '
                     'her pen.{/n} "What follows between us is not settled by what happened before."'},
 'Dragon': {'boundary': '{n}She regards you, then the map.{/n} "The men will stare. Let them. I need to know whether '
                        'the Commander who gave this order still intends to keep it."',
            'stayed': '{n}She moves the map between your chairs.{/n} "Show me how you intend to lead the column. '
                      'Afterwards you may tell me what the change feels like. I have been waiting to ask."'},
 'Legend': {'boundary': '{n}She keeps your hand, feeling your pulse.{/n} "You gave up power the army had learned to '
                        'depend on. We shall have to change its plans. I would also like to know whether you have '
                        'slept."',
            'stayed': '{n}She sets a chair beside hers.{/n} "Sit. The dispatch can wait while you tell me." {n}Her '
                      'fingers stay around yours.{/n} "Tomorrow I shall expect the Commander. Tonight I should like an '
                      'answer from you."'}}


def path_scene(path, opening, extra_requires=(), extra_forbids=()):
    key = path.lower()
    SCENES.append(scene(
        f"galfrey.{key}.the_space_between_orders",
        "The space between orders",
        "Galfrey",
        5,
        '"May I keep you company while you work?"',
        [
            n("start", "Galfrey", opening,
              c('"Say what you came to say."' if path in ('Demon', 'Devil') else '"I\'ll stay while you finish."', "boundary"),
              c('"I\'ll leave you to the orders."', "leave")),
            n("boundary", "Galfrey", PATH_PROSE[path]['boundary'],
              c('"I hear you."' if path in ('Demon', 'Devil') else '"Go on."', "stayed"),
              c('"We can speak another time."', "leave")),
            n("leave", "Galfrey", '{n}Galfrey draws the next dispatch toward her and breaks its seal.{/n} "Another time, then. I have men waiting for these orders."',
              c("Leave her to her work.", abort=True)),
            n("stayed", "Galfrey", PATH_PROSE[path]['stayed'],
              c("Return to the campaign.")),
        ],
        requires=("galfrey.native_active", f"path.{key}", *extra_requires),
        forbids=("galfrey.dead", "galfrey.killed_by_commander", *extra_forbids),
        delay=24,
        optional=True,
        Relationship="galfrey",
        Chapters=[5], Areas=[PRESENCES[HUB]["Area"]],
        ContactUnit=PRESENCES[HUB]["Unit"], InteractionHub=HUB,  # eng7-f6d
    ))


path_scene("Angel", '{n}Galfrey signs the last marching order and sets down her pen.{/n} "The forward companies leave at dawn. I hope you brought something else to discuss."')
path_scene("Azata", '{n}Galfrey takes the half-folded dispatch from your hands and smooths it beside its broken seal.{/n} "Commander. The supply wagons are waiting for this."')
path_scene("Aeon", '{n}She closes the ledger, her finger still on the line recording her authority.{/n} "Drezen has changed. The orders on this desk still need my signature."', extra_requires=("galfrey.aeon_history_changed",))
TRICKSTER_MISSED_COURTSHIP_PLAN = {
    "status": "unimplemented and required",
    "native_anchor_candidate": "GalfreyArrives/Answer_0001 invites Galfrey to the Commander's military and political council; the Trickster has separate native council stages.",
    "design": "Create a Chapter 3 acquisition independent of galfrey.native_active and galfrey.native_finished. Distinguish never-courted history from explicit rejection, and let Galfrey decline without a later hidden reset.",
    "evidence_needed": "Verify a real Trickster council stage, map/actor contact, queue reservation, chapter timing, prerequisites, and a source-grounded reason for any voluntary reconsideration after rejection.",
}


path_scene("Trickster", '{n}She turns a decree toward you. It bears her seal and an impossible date.{/n} "My seal. Your handiwork, I presume?"')
path_scene("Demon", '{n}Galfrey watches your clenched hands. When she takes your wrist, her grip is firm.{/n} "What happened, Commander?"')
path_scene("Devil", '{n}She pushes the contract away from the royal papers without touching its signature line.{/n} "A contract? I had hoped you had brought news from the front."', extra_requires=("galfrey.devil_after_sex",), extra_forbids=("galfrey.devil_incompatibility_seen",))
path_scene("Dragon", '{n}Her gaze follows the traces of your transformation, then returns to your face.{/n} "The scouts\' reports are here. Can you still use that chair?"')
path_scene("Legend", '{n}She studies you a moment, then offers her hand across the dispatches.{/n} "You have been difficult to find, Commander. Sit down."')


# eng7-f6d: draft-only binding; expansion.py does not import this module.
def integrate(payload):
    from copy import deepcopy
    payload.setdefault("Etudes", {}).update(ETUDES)
    payload.setdefault("SeenCues", {}).update(deepcopy(SEEN_CUES))
    payload.setdefault("Presences", {}).update(deepcopy(PRESENCES))

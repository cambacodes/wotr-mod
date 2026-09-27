"""Unintegrated opening for an authored Trickster-Areelu alternate route.

Canon dialogue remains the reference for the failed graft, Areelu's grief,
and her dangerous ambition. The pre-graft adult biography is an authored AU
premise; it does not change the native soul, graft, or dialogue history.
All availability flags below are contracts for future runtime producers.
"""
from story_format import c, n, scene


RELATIONSHIP = dict(
    Title="A hypothesis with teeth",
    Description="Areelu gives the Commander one chance to challenge her account of fate.",
    Objective="Decide whether rivalry with Areelu is worth the cost",
    Guidance=(
        "Experimental Trickster-only alternate continuity. This unintegrated opening "
        "requires a future producer to verify the native soul and graft revelations, "
        "the acknowledged authored pre-graft adult biography, and a living, available "
        "Areelu. Her native child identification remains grief-driven delusion, not kinship. "
        "It does not set those facts or imply romantic consent. Every scene has a "
        "hostile or nonromantic exit."
    ),
    StartedFlag="areelu.trickster_opening.started",
    ClosedFlag="areelu.trickster_opening.closed",
    CommittedFlag="areelu.trickster_opening.relationship_committed",
    UnavailableFlags=["areelu.trickster_opening.native_conflict"],
    FailureFlags=[],
)

# These names describe future registered producers. They are not live flags yet.
GATES = {
    "native_revelations_verified": "Native dialogue history confirms the original mortal soul, the grafted remnants, and Areelu's failed-restoration admission.",
    "areelu_available": "A runtime actor/state reader confirms Areelu is alive and contactable before offering an invitation. An invitation is an explicit player action; it does not presume she accepts.",
    "alternate_continuity_acknowledged": "Before the graft, the Commander's mortal soul belonged to an unrelated adult who had already lived an adult life. This is an authored AU premise, not a native script fact. The child Areelu lost, the failed restoration, her grief-driven identification of the Commander, and the grafted remnants remain as in the game. The AU does not change the native cue or claim that the child survived.",
    "active_trickster_path": "The runtime path reader confirms Trickster is the Commander's current active mythic path when contact is offered; a past path or generic mythic flag does not qualify.",
    "invitation_available": "A future reader permits the player to send one explicit contact request only when native revelations, the acknowledged authored pre-graft adult biography, current Trickster path, living/contactable Areelu, and terminal ending checks pass. The invitation itself does not start romance or imply acceptance.",
    "contact_solicitation": "A future solicitation identifies the pre-graft adult biography as an authored AU premise and explains that the native c6 cue remains real dialogue showing Areelu's grief-driven identification. It asks whether the player wants to explore an authored romance in this branch, without changing the cue or treating it as kinship fact. Declining exits without setting alternate_continuity_acknowledged. Areelu's explicit reply sets contact_accepted or contact_declined. Silence, unavailable contact, or refusal never opens the scene.",
    "entry_ready_composite": "A registered gate writer sets areelu.trickster_opening.entry_ready only after the native revelations, acknowledged AU continuity, current Trickster path, availability, terminal ending checks, and Areelu's explicit contact_accepted result are verified. The accepted reply may persist, but entry_ready is not a durable path grant: every scene independently checks the current active Trickster path, including after any delay or path change. No game reader or writer exists yet.",
    "cradle_memory_record_verified": "A separate reader confirms Cue_0010 and exactly one of Answer_0013, Answer_0014, Answer_0015, or Answer_0016 in native dialogue history. The second scene and any memory_protected result require this verified record; otherwise the memory-centered scene remains unavailable.",
    "cradle_memory_answer_available": "This derived state is true only when cradle_memory_record_verified is true and the selected answer is Answer_0013, Answer_0014, or Answer_0015. Answer_0016 is a refusal and disqualifies only the memory intervention, not all later nonromantic contact.",
    "trickster_memory_intervention": "The authored memory_test node narrates a contradictory annotation beside the Commander's verified native answer about the crib in Areelu's ruined home. It does not change the native answer or graft. The Commander may proceed only after choosing the risk that his confidence in the precise feeling he reported will become unreliable. Areelu must agree to test the copy. This is an authored Trickster-only design, not an existing game power; no game intervention producer exists.",
    "romance_interest": "The Commander may declare interest in scene three. Scene four gives Areelu a separate, authored choice to name reciprocal adult attraction without committing to a relationship; the Commander may reciprocate, pause, decline, or withdraw. No committed relationship flag is set.",
}

# Exact source-backed terminal etudes from reference/expansion/etudes.json.
# A future observer must read current activity and terminal postconditions.
# These records are not queried or changed by this manuscript.
NATIVE_ENDING_VETO_MATRIX = {
    "hard_veto": {
        "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_AreeluDead.jbp": "936af39436c74953b43a4165bfbcc9f9",
        "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_AreeluKilledByLegend.jbp": "26d8e09c942e4ec2a13c834706cbfc12",
        "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_AreeluSacrifice.jbp": "f455dbe5ddfbc454380ce27bc93795d5",
        "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_AreeluSacrificeBefore.jbp": "2667b0fda8704432bc35ace995e8022e",
        "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_AreeluSacrificeTrickster.jbp": "29c5c64462384fa3b8aae34e4c9ebce9",
        "World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/AreeluIncinerated.jbp": "23983059575fff749ae1446eba539260",
    },
    "hold_for_living_contact_proof": {
        "World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_AreeluRedeemed.jbp": "127e8a018a0840b080c276b4704e58a2",
        "World/Etudes/Common/WrathOfTheRighteous/TrueEnding/TE_AscendAreelu.jbp": "63279a971792474ba0439b9f75795a7a",
    },
    "policy": "If any hard_veto etude is active, set the mod-owned native_conflict flag and block all contact. If any hold_for_living_contact_proof etude is active, block until a runtime reader independently proves Areelu is alive and contactable; only the separate solicitation reply can establish contact_accepted. Never clear, complete, or rewrite a native ending etude. Ending_AreeluSacrificeTrickster is independently listed as a terminal veto; no causal trigger relationship to another ending is asserted here.",
    "status": "Design contract only. No etude observer, conflict writer, or post-ending contact producer exists.",
}

# The c6 child-identification line remains native dialogue and evidence of Areelu's grief.
# It is not a kinship fact or an eligibility veto for this authored adult AU branch.
NATIVE_GRIEF_CONTEXT = {
    "source_cue": {
        "World/Dialogs/c6/SecondFloor/AreeluBurnTheWitch/Cue_0069.jbp": "ec2ae0db3ba72a545b56a4fac08ecd06",
    },
    "text_key": "ccebf842-d6a0-4f67-8dab-1d00a5751fd8",
    "meaning": "Areelu says she cannot think of the Commander as anything but her child after recognizing restoration cannot return her child exactly as before. The route treats this as real, grief-driven identification that does not establish kinship or erase the Commander's adult identity.",
    "policy": "Never clear, rewrite, or veto the route because this cue was seen. The authored branch acknowledges the line, preserves its native history, and lets Areelu and the Commander confront the gap between her grief-driven identification and the AU adult biography.",
    "status": "Narrative design contract only. No native cue-history reader exists.",
}

# The native projector object was destroyed at Cue_0009. The persistent subject
# of the authored risk is the surviving dialogue-history answer, not that prop.
NATIVE_MEMORY_STATE_CONTRACT = {
    "history_key": "World/Dialogs/c5/AreeluLabAgain/AreeluCell/Cue_0010.jbp plus exactly one of Answer_0013 through Answer_0016",
    "native_state": "The selected answer remains in native dialogue history on every branch. No authored result deletes, replaces, or edits that cue history.",
    "protected_result": "memory_protected permanently marks the native answer as the sole factual record and blocks the annotation test.",
    "contested_result": "memory_contested permanently records only the Commander's reduced confidence in the interpretation of the selected Answer_0013, Answer_0014, or Answer_0015. It does not erase that answer or claim the destroyed projector survives.",
    "persistence": "The two mod-owned results are mutually exclusive, one-way, and must survive save/load. No writer or save/load test exists.",
}

# The physical native projector is already destroyed by its source scene.
# The future route may contest the Commander's remembered answer, not recover or
# claim ownership of that destroyed object.
NATIVE_CRADLE_MEMORY_SOURCE = {
    "prompt": ("World/Dialogs/c5/AreeluLabAgain/AreeluCell/Cue_0010.jbp", "7faf68a4a3ef2394397fdd22efd80ffd"),
    "answers": {
        "sadness": ("World/Dialogs/c5/AreeluLabAgain/AreeluCell/Answer_0013.jbp", "0853df779fb798c4dbf2d6e106674170"),
        "rage": ("World/Dialogs/c5/AreeluLabAgain/AreeluCell/Answer_0014.jbp", "f0d826fb7b99a1e4c9e23e46534a2993"),
        "closeness_to_mystery": ("World/Dialogs/c5/AreeluLabAgain/AreeluCell/Answer_0015.jbp", "9c9655606788f8b4cb039e48b2739c25"),
        "declined": ("World/Dialogs/c5/AreeluLabAgain/AreeluCell/Answer_0016.jbp", "84de666a567b51c46900cc799b2237b8"),
    },
    "projector_destroyed": ("World/Dialogs/c5/AreeluLabAgain/AreeluCell/Cue_0009.jbp", "591acfaf8500cc94aa7a8918db767d43"),
    "evidence_source": "reference/canon-review/candidate-inventory-dialogue.json and installed blueprints.zip",
    "rule": "A registered reader must verify Cue_0010 plus exactly one answer from Answer_0013 through Answer_0016. Answer_0016 declined means no memory intervention. Cue_0009 records the native projector and crystal shattering, so no later scene may treat that physical crystal as recoverable.",
}

MEMORY_INTERVENTION_CONTRACT = {
    "method": "The active Trickster places a second, explicitly impossible annotation beside the verified cradle-memory answer. It exposes the observer's interpretation as mutable without changing the native cue, response, soul, graft, or past event.",
    "cost": "If the Commander accepts the test, later authored scenes must remember that his confidence in the exact feeling he reported is unreliable. The native answer remains in save history and must never be deleted or presented as newly changed fact.",
    "protection_result": "A persistent mod-owned memory_protected result preserves the native answer as the only factual record and disables the intervention.",
    "loss_result": "A persistent mod-owned memory_contested result records the Commander-consented loss of certainty about that one response. It never claims the native projector crystal survives or alters native cue history.",
    "invariants": "memory_protected and memory_contested are mutually exclusive, save-safe, one-way results. The intervention requires current active Trickster, verified non-declined native answer, entry_ready, Areelu's separate agreement to test the copy, and the Commander's explicit choice to accept risk. No game writer or save/load test exists.",
    "execution_status": "Dialogue prose and local Python state contract only. No Unity dialogue choice invokes this Python function, and no native or mod save state is mutated by it.",
}


MEMORY_PROTECTED = "areelu.trickster_opening.memory_protected"
MEMORY_CONTESTED = "areelu.trickster_opening.memory_contested"
NATIVE_MEMORY_RECORD_VERIFIED = "areelu.trickster_opening.cradle_memory_record_verified"
CONTACT_ACCEPTED = "areelu.trickster_opening.contact_accepted"
CONTACT_DECLINED = "areelu.trickster_opening.contact_declined"
TRICKSTER_METHOD_FLAG = "areelu.trickster_opening.trickster_method_demonstrated"
MEMORY_CHOICE_EFFECTS = {
    "protect": {
        "Set": (MEMORY_PROTECTED,),
        "Requires": (NATIVE_MEMORY_RECORD_VERIFIED,),
        "Forbids": (MEMORY_PROTECTED, MEMORY_CONTESTED),
    },
    "accept_risk": {
        "Set": (MEMORY_CONTESTED,),
        "Requires": (
            NATIVE_MEMORY_RECORD_VERIFIED,
            "areelu.trickster_opening.active_trickster_path",
            "areelu.trickster_opening.entry_ready",
            "areelu.trickster_opening.cradle_memory_answer_available",
        ),
        "Forbids": (MEMORY_PROTECTED, MEMORY_CONTESTED),
    },
    "withdraw": {
        "Set": (MEMORY_PROTECTED,),
        "Requires": (
            NATIVE_MEMORY_RECORD_VERIFIED,
            "areelu.trickster_opening.active_trickster_path",
            "areelu.trickster_opening.entry_ready",
            "areelu.trickster_opening.cradle_memory_answer_available",
        ),
        "Forbids": (MEMORY_PROTECTED, MEMORY_CONTESTED),
    },
}


def memory_choice(text, action, next=None, flags=(), requires=(), forbids=(), abort=False):
    """Build scene choices from the same effect table used by the transition tests."""
    effect = MEMORY_CHOICE_EFFECTS[action]
    return c(
        text,
        next,
        flags=(*effect["Set"], *flags),
        requires=(*effect["Requires"], *requires),
        forbids=(*effect["Forbids"], *forbids),
        abort=abort,
    )


def apply_memory_choice(action, *, prior_state=(), current_trickster, entry_ready, areelu_agrees, native_answer_verified, answer_key):
    """Apply one authored choice to mod-owned state, preserving native answer history."""
    prior = set(prior_state)
    terminal = {MEMORY_PROTECTED, MEMORY_CONTESTED}
    if len(prior & terminal) > 1:
        return {"outcome": "rejected_contradictory_prior", "state": frozenset(prior), "native_answer": answer_key}
    if prior & terminal:
        return {"outcome": "rejected_already_final", "state": frozenset(prior), "native_answer": answer_key}
    allowed_answers = {
        value[0].rsplit("/", 1)[-1].removesuffix(".jbp")
        for value in NATIVE_CRADLE_MEMORY_SOURCE["answers"].values()
    }
    if answer_key not in allowed_answers:
        return {"outcome": "rejected_invalid_answer", "state": frozenset(prior), "native_answer": answer_key}
    if not native_answer_verified:
        return {"outcome": "rejected_unverified_answer", "state": frozenset(prior), "native_answer": answer_key}
    if action not in MEMORY_CHOICE_EFFECTS:
        return {"outcome": "rejected_invalid_action", "state": frozenset(prior), "native_answer": answer_key}
    if action in {"accept_risk", "withdraw"}:
        if not current_trickster or not entry_ready or not native_answer_verified:
            return {"outcome": "rejected_ineligible", "state": frozenset(prior), "native_answer": answer_key}
        if not areelu_agrees:
            return {"outcome": "areelu_refused", "state": frozenset(prior), "native_answer": answer_key}
        if answer_key == "Answer_0016":
            return {"outcome": "native_answer_declined", "state": frozenset(prior), "native_answer": answer_key}
    new_state = prior | set(MEMORY_CHOICE_EFFECTS[action]["Set"])
    result = {"outcome": action, "state": frozenset(new_state), "native_answer": answer_key}
    if action == "accept_risk":
        result["annotation"] = "The question authored the answer; the answer authored the question."
    return result


def resolve_contact_gate(*, native_revelations, au_acknowledged, current_trickster, areelu_alive, areelu_contactable, active_endings=(), seen_cues=()):
    """Resolve contact eligibility; a grief-identification cue supplies context, never a veto."""
    active_endings = set(active_endings)
    seen_cues = set(seen_cues)
    grief_context_seen = bool(seen_cues & set(NATIVE_GRIEF_CONTEXT["source_cue"]))
    hard_endings = set(NATIVE_ENDING_VETO_MATRIX["hard_veto"])
    hold_endings = set(NATIVE_ENDING_VETO_MATRIX["hold_for_living_contact_proof"])
    if active_endings & hard_endings:
        return {"outcome": "native_conflict", "invitation_available": False, "grief_context_seen": grief_context_seen}
    if not (native_revelations and au_acknowledged and current_trickster):
        return {"outcome": "unavailable", "invitation_available": False, "grief_context_seen": grief_context_seen}
    if active_endings & hold_endings and not (areelu_alive and areelu_contactable):
        return {"outcome": "living_contact_unproven", "invitation_available": False, "grief_context_seen": grief_context_seen}
    if not (areelu_alive and areelu_contactable):
        return {"outcome": "unavailable", "invitation_available": False, "grief_context_seen": grief_context_seen}
    return {"outcome": "invitation_available", "invitation_available": True, "grief_context_seen": grief_context_seen}


def apply_contact_reply(*, prior_state=(), invitation_available, areelu_accepts):
    """Record one explicit response to an eligible invitation; reject rewrites."""
    prior = set(prior_state)
    terminal = {CONTACT_ACCEPTED, CONTACT_DECLINED}
    if len(prior & terminal) > 1:
        return {"outcome": "rejected_contradictory_prior", "state": frozenset(prior)}
    if prior & terminal:
        return {"outcome": "rejected_already_final", "state": frozenset(prior)}
    if not invitation_available:
        return {"outcome": "rejected_unavailable", "state": frozenset(prior)}
    flag = CONTACT_ACCEPTED if areelu_accepts else CONTACT_DECLINED
    return {"outcome": "accepted" if areelu_accepts else "declined", "state": frozenset(prior | {flag})}


TRICKSTER_COPY_CHOICE = {
    "Set": (TRICKSTER_METHOD_FLAG, "areelu.trickster_opening.second_problem_solved"),
    "Requires": ("areelu.trickster_opening.active_trickster_path",),
    "Forbids": (TRICKSTER_METHOD_FLAG,),
}


def trickster_copy_choice(text, next, flags=(), requires=(), forbids=(), abort=False):
    """Build the authored contradiction choice from its checkable effect contract."""
    return c(
        text,
        next,
        flags=(*TRICKSTER_COPY_CHOICE["Set"], *flags),
        requires=(*TRICKSTER_COPY_CHOICE["Requires"], *requires),
        forbids=(*TRICKSTER_COPY_CHOICE["Forbids"], *forbids),
        abort=abort,
    )


def apply_trickster_copy_choice(*, prior_state=(), current_trickster, page_is_native):
    """Model the copy-only contradiction and refuse native-source mutation."""
    prior = set(prior_state)
    flag = TRICKSTER_METHOD_FLAG
    if flag in prior:
        return {"outcome": "rejected_already_final", "state": frozenset(prior), "native_history_changed": False}
    if not current_trickster:
        return {"outcome": "rejected_ineligible", "state": frozenset(prior), "native_history_changed": False}
    if page_is_native:
        return {"outcome": "rejected_native_source", "state": frozenset(prior), "native_history_changed": False}
    return {
        "outcome": "contradiction_demonstrated",
        "state": frozenset(prior | set(TRICKSTER_COPY_CHOICE["Set"])),
        "annotation": "The premise cites the exception as author; the exception cites the premise.",
        "native_history_changed": False,
    }

def f(*names):
    return tuple("areelu.trickster_opening." + name for name in names)


RIVALRY_FLAG = "areelu.trickster_opening.rivalry"
ENTRY_READY = "areelu.trickster_opening.entry_ready"


SCENES = [
    scene(
        "areelu.trickster_opening.the_original",
        "The original is not a footnote",
        "Areelu",
        5,
        "entry",
        [
            n("entry", "Areelu", '''The small sending crystal on your desk is cold. Areelu sent it with her reply to your invitation, wrapped in linen and an instruction to keep it away from mirrors. The projector in her ruined home is gone; its shattered crystal could never have carried this conversation.

It had been dark for six days. Tonight, a thin red line crosses its face, steady as a cut that has not decided whether to close.

Areelu's image forms without the familiar blur. She is in the laboratory, one hand resting on the edge of a table crowded with notes. The other holds a shard of crystal between two fingers. Her posture is immaculate; the ink on her thumb is not.

"You found the seam," she says. "Or you made one and hoped I would mistake it for mine. Which should I congratulate you for?"

You tell her the answer is whichever one annoys her more.

"Then I congratulate you on your timing. I was beginning to miss having someone nearby who can distinguish a question from a prayer." Her gaze shifts, measuring. "Do not confuse that with trust."

The crystal catches your reflection. For an instant the surface divides it into two overlapping faces, then returns one. The sight brings back her account of the soul she chose, the remnants she grafted, and the future she tried to force out of both.

"You have replayed the memory," Areelu says. "You know the restoration failed. You know what I wanted the graft to mean. And you know I still looked at you and saw..."

She stops. Her thumb presses into the crystal until the skin pales. The pause is not an invitation to finish the sentence for her.

"A child," she says. Her mouth pulls into something too controlled to be called a smile. "There. The ugliest fact, stated plainly. I knew the restoration had failed. I knew the soul I had chosen was yours, and the remnants were what remained of mine. I continued to look at you through the answer I wanted. Grief can be an ingenious falsifier."

She looks at your reflection. "You had lived a life before I chose your soul. An adult life, with loyalties and appetites I never bothered to discover. You were a stranger to me. That was convenient. A stranger could be reduced to a necessary component without the nuisance of learning his name." Her fingers close over the shard. "I have learned it now. I know whose voice answers when I speak to you. The graft may have altered that voice. It did not make it hers, or mine."

She sets the shard down with sufficient force to make the image tremble. "Do not congratulate yourself on curing me of an error. I can recognize it and still hate what recognition costs. You have your own history. I have the ruin I made trying to deny mine. If we speak again, we speak as the two people who are actually here."

The choice is not softened for you. Neither is her face.''',
              c('[Say plainly that the original soul was yours, and her grief does not get to rename you.]', "boundary", flags=f("started", "boundary_named")),
              c('[Tell her the distinction matters, but refuse to turn pain into a clever point.]', "careful", flags=f("started", "boundary_named", "restraint")),
              c('[Call her account another experiment in controlling the person she failed to restore.]', flags=f("closed", "hostile_exit"), abort=True),
              c('[End the contact. The old history is enough.]', flags=f("closed", "declined"), abort=True)),
            n("boundary", "Commander", '''"My soul was mine before you touched it. You can call the graft a failure. You can call what you saw a delusion. You do not get to make either one my identity."

Areelu's thumb stops moving against the crystal edge.

"A forceful claim," she says at last. "But you have not proved what the graft changed, or that your memories are untouched. I will concede the boundary; I will not pretend it answers every question."

"Disappointed?"

"I am trying to decide whether you can hold two facts in your mind without making one devour the other. The experiment happened. The remnants mattered to me, and may have changed you. Your original soul and history remained yours. I wanted a conclusion that would restore what I had lost. You were not it, and no conclusion makes that harmless."

The last sentence lands without apology. Its bluntness is more honest than kindness would have been.

"Do not turn that into an apology," she says. "I have not decided what an apology could repair."

"I didn't offer forgiveness."

"I did not ask for it." She turns the crystal a quarter turn, checking that the red line remains steady.''', c('[Ask what she wants from you now, in terms she cannot hide inside a theory.]', "question", flags=f("boundary_named"))),
            n("careful", "Commander", '''"The distinction matters. But if you are going to speak about your grief, do not dress it up as a puzzle I am supposed to solve for you."

Areelu's mouth tightens. The first response she reaches for is plainly sharp. She takes a breath and chooses another.

"You believe that was what I was doing?"

"I believe you are very good at making the person across from you responsible for the conclusion you prefer."

"And you are very good at describing that as if it were a discovery." Her gaze stays on yours. "You have not established what I was asking. I asked what you felt. I may have wanted your answer to confirm my story, but that does not tell me which part of your response came from you, which from the graft, or which from my leading question."

She draws one breath, slow and measured. "I will not ask you to make my loss easier to look at. That boundary is yours. The evidence is still unresolved."

"Do not mistake restraint for absolution," she adds. "I haven't."''', c('[Ask what she wants from you now, in terms she cannot hide inside a theory.]', "question", flags=f("boundary_named", "restraint"))),
            n("question", "Areelu", '''"What I want," Areelu says, "is to learn whether the one person who keeps finding the loose thread can tell the difference between a joke and a diagnosis."

"You called me here to assess my bedside manner?"

"No. I have no bedside manner. I called because your account leaves a premise untested, and I want to know whether you can risk being wrong about it." Her expression hardens. "Do not flatter yourself. An inconvenient question is not an intimate one."

"And if I decline to be your inconvenience?"

"Then you leave. I will dislike the wasted evening. I will survive it." She taps the red line in the crystal. "If you stay, we test one claim at a time. No bargains hidden in metaphors. No touch mistaken for trust. No future owed because you were clever once. And do not mistake the Trickster's talent for a license to edit my answer."

She has not invited you closer. She has offered a contest with terms. For Areelu, that is already a kind of risk.''',
              c('[Accept a single test, with the right to stop when either of you chooses.]', "test_prompt", flags=f("started", "terms_accepted", "rivalry")),
              c('[Refuse the test and leave the contact open only for necessary business.]', flags=f("closed", "nonromantic_exit"), abort=True),
              c('[Demand that she prove her sincerity before you give her another hour.]', "demand", flags=f("started", "demanded_proof"))),
            n("demand", "Areelu", '''"Sincerity," she repeats, as though testing whether the word has a useful edge. "You want a confession?"

"I want proof that this isn't another way to put me where you want me."

"There is no proof I can offer that you could not call another maneuver." Her eyes narrow. "If I produce a confession on command, you will be right to question it. If I refuse, you will call that proof too. You have made sincerity impossible to test, which is not the same as proving I am insincere."

She turns the crystal face down. The image vanishes.

"I will send you the record I used to reach my conclusion. You may inspect it, or throw it into a brazier. I will not ask you to come back. If you do, it will be your decision, and I will have no right to interpret it as anything else. Do not use a trick to manufacture an answer I did not give. If you want my attention, earn it while I am looking directly at you."

The line returns, but the image does not. The offered record may be evidence, bait, or both. You will decide after reading it.''',
              c('[Accept the record without promising to return.]', "record_received", flags=f("started", "record_offered")),
              c('[Refuse even the record. No further contact.]', flags=f("closed", "hard_exit"), abort=True)),
            n("record_received", "Commander", '''The record arrives folded inside plain paper. You read it once for what it says, and a second time for what it leaves out. It proves nothing about the future, and it does not ask you to forgive her.

The channel remains dark. Areelu made no demand that you answer. You can leave it that way.''',
              c('[Send one question about the record and reopen contact for her answer.]', flags=f("second_contact_open", "rivalry")),
              c('[Keep the record. Do not invite another meeting.]', flags=f("closed", "record_kept"), abort=True),
              c('[Destroy the record and close the channel.]', flags=f("closed", "record_destroyed"), abort=True)),
            n("test_prompt", "Areelu", '''"One test," she agrees. "Not one test of your loyalty, your virtue, or your capacity to endure me. One test of an idea."

She rotates the crystal. Three marks appear around the red line. They are not runes, but measurements: the points at which a closed circle fails to close.

"I will show you the record of my question at the crib. You will tell me what it can prove, and what it cannot. If your answer leaves my theory intact, say so." A pause. "You claim a Trickster can make a conclusion contradict its own evidence. Show me the difference between that and a prank with better costumes. I will not call the past changed because you made an image flicker."

"That sounds suspiciously like a moral question."

"It is a question about the cost of a method. Morality is what other people call the cost when they would rather not calculate it." Her eyes flick once toward the crystal. "You may leave before I begin."

You stay. Her satisfaction is small and quickly buried. It looks less like victory than anticipation.''', c('[Receive the proof at the next contact.]', flags=f("test_accepted", "second_contact_open", "rivalry"), abort=True),
              c('[Stop here. No test tonight.]', flags=f("closed", "test_declined"), abort=True)),
        ],
        requires=(ENTRY_READY, "areelu.trickster_opening.active_trickster_path"),
        forbids=("areelu.trickster_opening.closed",),
        delay=0,
        optional=True,
        Relationship="areelu",
        Remote=True,
    ),
    scene(
        "areelu_trickster_opening.the_test",
        "A joke with a consequence",
        "Areelu",
        5,
        "proof",
        [
            n("proof", "Areelu", '''The next contact arrives as a page of Areelu's handwriting. She has written down the question she asked about the crib in her ruined home, and beneath it your answer. You remember the projector shattering. This sheet offers no way to recover it, only her precise recollection of the words exchanged before the crystal broke.

"I know what response you made, as it stands in the record," Areelu says. "If you gave an answer, I do not know whether it belonged wholly to you, whether something in the graft answered, or whether I had already told you what I hoped to hear."

She folds the page so the question is hidden. "Do not mistake my uncertainty for an admission. The remnants may have affected you. Your adult soul may have supplied the response. My leading question may have shaped it. The recorded answer cannot separate those causes."

She places the page between you. "Show me how the Trickster tests that distinction without pretending to change what happened."''',
              c('[Knowledge: Arcana, DC 31] Separate the original question, the chosen response, and her later interpretation.', check=dict(Skill="SkillKnowledgeArcana", DC=31, Success="analysis_success", Failure="analysis_uncertain", CommanderOnly=True)),
              c('[Say directly that the answer is evidence of what you said, not proof of kinship.]', "model", flags=f("evidence_scope_named")),
              memory_choice('[Stop here. This memory is not material for another experiment.]', "protect", flags=f("closed", "ethics_exit"), abort=True)),
            n("analysis_success", "Commander", '''You trace the loop to the premise it assumes instead of measuring.

Areelu listens, then says, "You have found where my argument closes on itself. That still does not tell me what the graft changed."

"Correct."

"A gap is not an answer," she says. "I dislike gaps."''', c('[Ask what test could distinguish a remembered answer from an imposed interpretation.]', "model", flags=f("evidence_scope_named")),
              memory_choice('[Protect the memory and end the experiment.]', "protect", flags=f("rivalry", "closed"), abort=True)),
            n("analysis_uncertain", "Commander", '''You cannot separate the remembered feeling from the words Areelu placed around it.

Areelu leaves the page folded. "Then you have no finding. Don't dress uncertainty up as a victory."

"I won't."

"Then we can examine the method, if you still want to."''', c('[Ask what test could distinguish a remembered answer from an imposed interpretation.]', "model", flags=f("evidence_scope_named")),
              memory_choice('[Protect the memory and end the experiment.]', "protect", flags=f("rivalry", "closed"), abort=True)),
            n("model", "Areelu", '''"You have found a weakness in my argument, not in the graft." She taps the page. "An adult soul can remain itself and still carry an echo of what I bound to it."

Areelu's eyes narrow. "And do not simplify my attachment into a delusion. My claim about your identity was false; my grief was not. I know you had a life before I interfered. I do not yet know how much of it survived that interference, or what echoes I left behind."

The distinction stings because it leaves no clean victory. She has denied the family claim without letting you simplify what happened.

"Your Trickster test would hold the answer still and make its margin lie about who wrote it. If the question and answer both claim authorship, the footnote contradicts itself. It might expose the certainty I borrowed from that moment. It cannot tell us where your feeling began."

You answer that this is enough for a first test. Not proof of innocence. Proof that a conclusion can be made to expose its own assumptions.''',
                c('[Ask her to permit one Trickster contradiction beside the recorded answer, with your own certainty at risk.]', "intervention_offer", flags=f("test_scoped"), requires=f("active_trickster_path", "entry_ready", "cradle_memory_answer_available")),
              c('[Keep the dispute theoretical. The original answer was declined or is unavailable.]', "cost", flags=f("test_scoped", "rivalry"), forbids=f("cradle_memory_answer_available")),
              memory_choice('[Protect the original answer and continue only as an intellectual rivalry.]', "protect", "cost", flags=f("rivalry", "test_refused")),
              memory_choice('[End the exchange. Neither of you will use this memory again.]', "protect", flags=f("closed", "ethics_exit"), abort=True)),
            n("intervention_offer", "Areelu", '''Areelu keeps one hand on the page. "No. Not on those terms. You keep calling uncertainty a price, but I won't help you damage your memory to win an argument with me."

"The original record stays untouched. I would add one impossible footnote to a copy, and I accept that I may lose confidence in what I felt. You would be testing my limit, not changing the past."

She studies you, still unconvinced. "You are very practiced at making a risk sound like proof of courage. Give me a safeguard, or accept my refusal."''',
              memory_choice('[Accept her refusal. Preserve the original answer and keep this theoretical.]', "protect", "cost", flags=f("rivalry", "test_refused")),
            c('[Offer a single copy-only test: no changes to what happened, and either of you can stop before the annotation is made.]', "consent_offer", flags=f("test_scoped"), requires=f("active_trickster_path", "entry_ready")),
              memory_choice('[End the exchange. Neither of you will use this memory again.]', "protect", flags=f("closed", "ethics_exit"), abort=True)),
            n("consent_offer", "Areelu", '''"A copy only. What happened stays as it happened. One annotation, and either of us can stop before it appears." Areelu considers the terms. "That is narrow enough to test. I agree to this reconstruction, not to your theory."

She watches your face for a sign of triumph. "If you proceed, the annotation will make your account of the feeling less certain. I will not call that sacrifice noble, and I will not let you call it proof."''',
              memory_choice('[Proceed, knowing your confidence in the remembered feeling may be permanently weakened.]', "accept_risk", "memory_test", flags=f("rivalry", "areelu_test_agreed")),
              memory_choice('[Do not proceed. Preserve your original answer as the only factual record.]', "protect", "cost", flags=f("rivalry", "areelu_test_agreed")),
              memory_choice('[Withdraw before the test. Close contact.]', "withdraw", flags=f("closed", "test_withdrawn", "areelu_test_agreed"), abort=True)),
            n("memory_test", "Commander", '''You do not reach for the shattered projector. You do not touch the original answer that remains in the record.

Instead, your Trickster's contradiction appears beside the specific answer recorded to the question about the crib. The new footnote cites the question as its author and the answer as its author, each citation indisputably true and impossible together. Your original answer remains legible on the untouched sheet beside it. The footnote insists that the feeling was both yours and supplied to you, a claim that cannot be true in the same way at once. You have not altered the answer; you have made the margin confess that it cannot tell you what the answer means.

The page stays still. Your certainty does not. You remember what you selected, but you can no longer use the memory's emotional precision as unquestioned proof of where the feeling began.

Areelu reads both lines. "You have made your certainty about the answer's meaning less reliable. The answer itself is untouched. That does not make my interpretation more reliable."

"No. It makes the uncertainty visible."

"And it leaves the past exactly where it was." Her hand lifts from the page. "Do not call this a victory. You have shown that an observer can be tricked. You have not shown that the original observation was false."''',
              c('[Accept the limit of the test and ask what the failure cost her.]', "cost", flags=f("model_completed", "trickster_test_observed")),
              c('[End here. Keep the contradiction, but do not pursue Areelu.]', flags=f("closed", "trickster_test_observed"), abort=True)),
            n("cost", "Areelu", '''"The failed restoration cost me the only future I had been willing to imagine," she says. "That is not the same as saying it cost me the right to do whatever I wanted afterward."

She folds the page. The movement is exact; the paper still creases at the corner.

"I wanted the child I lost. I wanted the world to admit that death had taken something it could not keep. I made a theory out of that want and forced other lives to bear its weight. Then I looked at you and demanded that reality agree with the story I needed."

For an instant her voice thins. She recovers before the feeling can become an appeal.

"You are not the child I lost. You are not a substitute. The remnants were not you, and you were not them. Those facts do not acquit me." Her eyes fix on yours. "I am telling you because you asked what it cost. Do not mistake this for permission to comfort me."

You do not. The quiet between you is not forgiveness. It is room for the truth to stay ugly.''', c('[Tell her the truth is hers to carry, then ask why she chose to share it.]', "why", flags=f("model_completed", "grief_named")),
              c('[End the conversation while the experiment remains inconclusive.]', flags=f("closed", "rivalry_only"), abort=True)),
            n("why", "Areelu", '''"Why did you tell me?"

"Because you would have noticed the omission." She speaks without hesitation. Then, more quietly: "And because you have earned an answer that is not a disguise."

You hold her gaze. "That is not the same as trust."

"I know. I would not insult us both by pretending otherwise."

The word hangs between you. Us. She seems to notice it at the same moment you do.

"A convenient pronoun," she says. "It can mean two people arguing over a diagram."

"Or two people who haven't finished arguing."

"Do not write the ending before we have tested the next premise." She folds the page once and leaves it on the table. "I will send you a second problem. You may answer it, refuse it, or tell me that the first was enough. I am not owed another meeting."

The signal fades. This time she waits until you choose to end it.''', c('[Keep the channel open for a second question, with no promise beyond that.]', flags=f("model_completed", "second_question_open")),
              c('[Close the channel. The rivalry ends here.]', flags=f("closed", "rivalry_only"), abort=True)),
        ],
        requires=(
            "areelu.trickster_opening.second_contact_open",
            RIVALRY_FLAG,
            NATIVE_MEMORY_RECORD_VERIFIED,
            "areelu.trickster_opening.active_trickster_path",
            ENTRY_READY,
        ),
        forbids=("areelu.trickster_opening.closed",),
        delay=24,
        optional=True,
        Relationship="areelu",
        Remote=True,
    ),
    scene(
        "areelu_trickster_opening.the_second_problem",
        "A flaw in the margin",
        "Areelu",
        5,
        "challenge",
        [
            n("challenge", "Areelu", '''The next page is freshly made. Areelu has drawn a fresh working copy of a Worldwound calculation, leaving its provenance and every value on it deliberately unclaimed.

"Your first trick made a conclusion contradict its evidence," she says. "That is a useful nuisance. Now tell me whether you can find a flaw without making the page lie for you."

The diagram is a loop with one line that treats the rift's stability as both an observed result and a required premise. Areelu asks which claim depends on the other. She watches your face instead of the symbols.

"You asked for a test of an idea," you say. "This is one."

"It is. If you find a real flaw, the copy changes. If you only make a clever noise, I discard the page and you have learned nothing about my work."''',
              c('[Knowledge: Arcana, DC 33] Separate the measured closure from the assumption that the seam must remain stable.', check=dict(Skill="SkillKnowledgeArcana", DC=33, Success="second_analysis_success", Failure="second_analysis_uncertain", CommanderOnly=True)),
              trickster_copy_choice('[Trickster: Make the copied premise cite its own exception, so the loop must expose the contradiction it hides.]', "trickster_inversion", flags=f("second_problem_attempted")),
              c('[Decline the exercise and end the contact.]', flags=f("closed", "second_problem_declined"), abort=True)),
            n("second_analysis_success", "Commander", '''You point to the line where the calculation assumes the seam is stable in order to prove that it is stable. The page has not measured its own conclusion; it has repeated it.

Areelu checks the sequence twice. "That is a flaw in this copy. Do not congratulate yourself for finding a flaw in the Worldwound itself. I chose the premise to see whether you would distinguish a circular argument from a failed experiment."

"You expected me to mistake one for the other?"

"I expected you to want the larger victory." She sets the page aside, still unconvinced of your motives.''', c('[Ask what result she would accept as evidence against her own theory.]', "reply", flags=f("second_problem_solved")),
              c('[Tell her you came to be right, not to help her improve the exercise.]', "reply", flags=f("second_problem_solved", "ambition_admitted"))),
            n("second_analysis_uncertain", "Commander", '''You can name the two claims, but not which one the calculation actually measures. Areelu waits. You hear the pause as a chance to guess; she is giving you time to stop guessing.

"I do not know," you say.

"A useful answer," she replies, "provided it remains an answer and does not become an excuse to let me do your thinking." She turns the page toward you. "Try again, or leave the gap open."''', c('[Ask her which observation the copy is meant to represent.]', "reply", flags=f("second_problem_unresolved")),
              c('[Admit you cannot solve it yet and keep the disagreement open.]', "reply", flags=f("second_problem_unresolved"))),
            n("trickster_inversion", "Commander", '''You write one new sentence in the margin: the premise cites the exception as its author, and the exception cites the premise. Both citations fit the copy. Together they make its claim impossible to close.

The loop has to show its missing measurement instead of disguising it as a result. The paradox belongs to your new line; the copy opens at the fold where its claim failed.

Areelu scans the line. "You have made the argument fail in a way that shows me where it was already weak. That is more useful than making the diagram dance." Her finger stops short of the ink. "Do not assume I like being surprised."

"You did ask."

"I did." She does not smile, but she no longer looks at the page.''', c('[Ask what result she would accept as evidence against her own theory.]', "reply", flags=f("second_problem_solved", "trickster_method_demonstrated")),
              c('[End the exercise before she can mistake the trick for permission to inspect your mind.]', flags=f("closed", "second_problem_declined"), abort=True)),
            n("reply", "Areelu", '''"What result would change my mind?" She repeats the question. "One that survives my attempts to explain it away. You have shown me a flaw in a copy and a limit in my story about the crib. Neither repairs what I did, and neither makes the Worldwound an innocent mistake."

She folds the diagram once. The paper catches at the crease.

"I wanted to know whether you could challenge my work without using my grief as a handle. You did. I am not sure yet whether that makes me trust you, or only gives me a better reason to watch you."

She looks down at the line she crossed out. "I keep treating the failed restoration as a problem I haven't finished solving. Saying it failed does not make the loss feel finished. I do not know what I would do with my hands if I stopped working on it."

For the first time, the pause is not shaped like a question. You notice the ink along her thumb, the strain she has been hiding in her hand, and the composure she has to choose again. Wanting her is not the same as knowing her, and she gives no sign that she has mistaken one for the other.''',
              c('[Tell her you are attracted to her and would like to know her, without asking for an answer tonight.]', "interest", flags=f("commander_interest_stated")),
              c('[Keep this between the work and the argument. No personal claim.]', "goodbye", flags=f("second_question_open", "rivalry_only")),
              c('[Close the channel. You have both said enough for now.]', flags=f("closed", "second_problem_declined"), abort=True)),
            n("interest", "Commander", '''"I am attracted to you," you say. "I would like to know you outside the argument. I am not asking you to answer tonight, or to treat the trick as a reason to say yes."

Areelu's expression stills. The silence lasts long enough to be an answer to the urgency you did not put into the question.

"I heard you," she says. "I have not decided whether I want the same thing. Your restraint earns no reward, and my curiosity is not consent. If this continues, I will tell you what I choose."

"Understood."

"Do not make me repeat it as a test." Her gaze returns to the folded diagram, though not with the same concentration as before.''',
              c('[Accept her uncertainty and leave the next step to her.]', "goodbye", flags=f("second_question_open", "interest_unresolved")),
              c('[Withdraw the personal question and keep the contact strictly intellectual.]', "goodbye", flags=f("second_question_open", "interest_withdrawn")),
              c('[Push for an answer now. End contact when she refuses to give one.]', flags=f("closed", "interest_refused"), abort=True)),
            n("goodbye", "Areelu", '''"Next time," she says, "bring a question you are willing to have answered against you."

"And if I bring the wrong question?"

"Then I will tell you." She leaves the folded calculation where it is, a test neither of you needs to pretend was a victory. "That is all I am offering tonight."

The connection ends without a promise of another meeting. The disagreement remains. So does the possibility that, given time, neither of you will want it to be the only reason you return.''',
              c('[Keep the channel open for another question, with no expectation attached.]', flags=f("second_question_open", "rivalry")),
              c('[Close the channel until Areelu chooses to contact you.]', flags=f("closed", "rivalry_only"), abort=True)),
        ],
        requires=(
            "areelu.trickster_opening.second_question_open",
            RIVALRY_FLAG,
            "areelu.trickster_opening.active_trickster_path",
        ),
        forbids=("areelu.trickster_opening.closed",),
        delay=24,
        optional=True,
        Relationship="areelu",
        Remote=True,
    ),
    scene(
        "areelu.trickster_opening.the_live_fold",
        "A fold with teeth",
        "Areelu",
        5,
        "field_entry",
        [
            n("field_entry", "Areelu", '''The next invitation gives a place and a time. No signal, no painted image. The coordinates lead to a sealed chamber built into a shelf of black stone. The outer door bears a surveyor's mark under a thick layer of soot. Areelu has cut a second mark below it, an angular instruction to those who know her hand: approach alone.

Areelu waits beside a waist-high ring of copper. Beyond it, the air bends around a seam no wider than a knife. The red light caught in the seam is not the shattered projector crystal. It is the edge of a small planar fold she has deliberately held open for measurement.

"Before you ask: no, this is not the Worldwound," she says. "It is a bounded residue from a probe I should have shut down sooner. If the outer ring slips, the fold will eat the instruments and the notes on this table. The chamber is shielded. We have time to stop it."

"And you asked me here because?"

"You found a circular premise in my copy. I want to see whether it was an error in ink or a habit in my work." Her eyes move over you. "You may leave. I will close it myself."

The seam gives a low, almost musical hum. The copper ring answers half a beat late. You see the pattern now: one side records the fold's pull, while the other assumes the pull has already ended. Areelu watches your face, not your hands.

"Tell me what you see," she says. "Then tell me what you intend to do. Do not touch anything until I agree."''',
              c('[Knowledge: Arcana, DC 35] Identify which measurement the outer ring is treating as a conclusion.', check=dict(Skill="SkillKnowledgeArcana", DC=35, Success="field_arcana_success", Failure="field_arcana_failure", CommanderOnly=True)),
              c('[Trickster: Make the fold cite its own boundary as the cause of its opening, then let the contradiction force it to choose a limit.]', "field_trickster", flags=f("field_paradox_attempted"), requires=f("active_trickster_path", "entry_ready")),
              c('[Tell her to close it herself. You will not turn a private test into a wager with live magic.]', "field_close_alone", flags=f("field_declined"))),
            n("field_arcana_success", "Commander", '''The outer ring reads a measurement as proof that the pull has ended. It has confused the boundary it needs with the result it was meant to observe.

Areelu follows your finger along the copper. "So the instrument is begging the answer out of the question." She glances at you. "Do not look pleased. I asked you here to find the defect, not to congratulate the defect for existing."

"I can do both."

The corner of her mouth shifts, then stills. "That is what worries me."''', c('[Ask her to name the cost before either of you acts.]', "field_decision", flags=f("field_fault_found")),
              c('[Recommend closing the fold now and leaving the instrument unfinished.]', "field_close_alone", flags=f("field_fault_found", "field_declined"))),
            n("field_arcana_failure", "Commander", '''You can trace the two readings but cannot prove which one is circular. The seam pulses again. Areelu turns a copper dial and steadies it without looking away from you.

"You could pretend certainty," she says. "Most people do when an answer is expected."

"Would you prefer that?"

"I would prefer the truth, even when it is inconvenient and badly timed." She takes her hand off the dial. "The ring is still stable. We can close it, try your Trickster method, or stop here."''', c('[Ask her to close it now. You will not bluff your way through a live fold.]', "field_close_alone", flags=f("field_uncertain", "field_declined")),
              c('[Name your uncertainty and ask what reading she trusts least.]', "field_decision", flags=f("field_uncertain"))),
            n("field_trickster", "Commander", '''You give the fold one cause, then make the boundary cite that cause as the reason it has opened. The contradiction does not overpower the magic. It gives the working a limit it had failed to name.

The red edge contracts. The copper ring finds a single pitch and holds it.

Areelu's hand closes around the dial. She looks first at the seam, then at you. "You did not force it shut. You made the false premise unable to pretend it was a measurement."

"You keep asking whether the trick is only a joke."

"I keep finding uses for the answer." Her voice remains cool, but she lets the dial go. "Do not turn that into admiration. I have not decided what I think of you."''', c('[Ask whether the instrument is safe, then give her the choice to continue.]', "field_aftermath", flags=f("field_fault_found", "field_stabilized", "field_paradox_used")),
              c('[Step away and let her close the ring. The contradiction has done enough.]', "field_close_alone", flags=f("field_paradox_used"))),
            n("field_decision", "Areelu", '''"If we change the ring, we save the instruments and lose the measurement. If we hold it for another minute, I can record the pulse, but one of us will have to keep the outer boundary from slipping." She says it like a list of ingredients. Her fingers flex once at her side. "I am not asking you to take the risk. I am telling you what it is."

You could leave her the choice she has claimed. You could offer to hold the boundary while she records the result. Or you could tell her that this experiment has reached its limit.''',
              c('[Hold the outer boundary while she records one pulse. Stop at the first sign of strain.]', "field_aftermath", flags=f("field_stabilized", "field_shared_risk")),
              c('[Tell her to close it. The measurement can be repeated; the risk cannot be recalled.]', "field_close_alone", flags=f("field_closed_early")),
              c('[Leave the chamber. She chose the experiment, and you will not make the choice for her.]', flags=f("closed", "field_exit"), abort=True)),
            n("field_close_alone", "Areelu", '''Areelu turns the ring inward. The seam narrows to a red thread, then vanishes. It takes the instrument's last reading with it. The notes remain, though the newest page is blank where the measurement should have been.

"You were right to stop me," she says. The words are not warm, and she does not offer them as a debt. "I know how to close a fold. I was trying to make the result worth the risk. That is not the same as needing you to take it for me."

She removes one copper pin and sets it on the table. "The loss is mine. I will not make you repair it by staying."''',
              c('[Tell her the lost measurement is not a verdict on her work, then ask whether she wants company while she records what remains.]', "field_aftermath", flags=f("field_stabilized", "field_measurement_lost")),
              c('[Leave the chamber and keep the relationship professional.]', flags=f("closed", "field_exit", "rivalry_only"), abort=True)),
            n("field_aftermath", "Areelu", '''The fold is closed. The chamber settles, and the metal ring cools beneath your hand. If you held the boundary, the pulse leaves a pale line across your palm; it fades while Areelu checks that your fingers still move. If you asked her to close it, the newest reading is gone. Neither result is a triumph. Something was risked, and something was chosen.

"You could have made the decision for me," she says. "You did not."

"You told me the cost."

"Most people hear a cost as a request to prove their courage." She turns the copper pin between two fingers. "You heard it as information. I dislike how much that matters."

For a moment neither of you moves. Her composure returns by degrees. She looks at the red trace on your palm, then at your face. The chamber has gone quiet enough for an answer, if either of you wants one.''',
              c('[Ask whether your earlier declaration changed what she wants from you.]', "field_interest_offer", requires=f("commander_interest_stated"), forbids=f("interest_withdrawn")),
              c('[Keep the exchange focused on the work. Do not ask her for a personal answer.]', "field_professional", forbids=f("commander_interest_stated", "interest_withdrawn"))),
            n("field_interest_offer", "Areelu", '''"You want to know whether your declaration changed anything." She tests the phrasing, then looks directly at you. "I did not answer because I could not tell whether I wanted the man, the contest, or simply the chance to want something that was not the child I lost."

She puts the copper pin down. "I can tell you one thing now. I am attracted to you. Your mind is part of it. So is your body. That desire is mine, and it does not make the graft a romance, the child a substitute, or my grief your responsibility. It may also make me selfish. I will not sell you a promise of gentleness I cannot guarantee."

The admission is not a surrender. It costs her something to say it without dressing it as a test. She waits for your answer without moving closer.''',
              c('[Say you want her too, but will not be a remedy for her grief or a prize for winning.]', "field_mutual_interest", flags=f("areelu_desire_admitted")),
              c('[Tell her you need time to decide what you want now that she has answered.]', "field_interest_paused", flags=f("areelu_desire_admitted", "field_interest_paused")),
              c('[Tell her the attraction is not mutual, and ask to keep future contact about the work.]', "field_interest_declined", flags=f("areelu_desire_admitted", "field_interest_declined"))),
            n("field_mutual_interest", "Commander", '''"I want you too," you say. "But I will not be the answer to your grief, and I will not mistake being wanted for being owed anything."

Areelu exhales, almost a laugh and not quite. "Good. I would have distrusted you if you had offered to fix me. I am not a broken instrument. I am a person who has done unforgivable things and may do unforgivable things again. You should remember both facts when you decide what you want."

Her hand rests on the table between you, palm turned upward. She does not reach for you. "If you want to touch me, ask. If you do not, I will not make the silence mean you were afraid."''',
              c('[Ask if you may hold her hand. Take no further liberty.]', "field_hand", flags=f("touch_requested")),
              c('[Do not touch her. Let this answer stand without turning it into a promise.]', "field_professional"),
              c('[Tell her you have changed your mind and close contact.]', flags=f("closed", "field_interest_withdrawn"), abort=True)),
            n("field_hand", "Areelu", '''She studies you for a breath. Then she turns her palm fully toward yours. "Yes. My hand. For as long as we both want it."

Her skin is warm, her grip controlled. The contact is brief enough to end before either of you can pretend it settled anything. She keeps her gaze on you.

"I wanted that," she says. "I still do not know what comes after it. Do not confuse my uncertainty with regret, and do not ask it to become certainty before I have earned the right to give you an honest answer."''',
              c('[Let go when she does, and ask whether she wants another meeting on personal terms.]', "field_next_step", flags=f("areelu_desire_admitted", "hand_held")),
              c('[Release her hand and return to the work. The contact was enough for tonight.]', "field_professional", flags=f("areelu_desire_admitted", "hand_held"))),
            n("field_interest_paused", "Areelu", '''"Then take the time," she says. "I will not turn my answer into a deadline."

She takes the copper pin and begins sorting the notes. Her hands are steady again, but she does not hide that the admission has changed the room. "We can continue the work if you want. If you decide you want no more than that, say so plainly. I will be disappointed. I will survive it."''', c('[Stay to help her record the surviving measurements, without promising a romance.]', "field_professional", flags=f("field_work_continues")),
              c('[Leave the chamber and decide in private.]', flags=f("closed", "field_interest_paused"), abort=True)),
            n("field_professional", "Areelu", '''Areelu nods once. She does not turn your answer into a debt.

"Then we keep the terms clear," she says. "You may challenge the next calculation. You may also refuse. Neither choice buys access to my grief, and I will not use it to purchase your attention."

She writes the lost measurement in the margin as a loss, not a blank she can pretend to fill later. The distinction is small. She makes it anyway.''', c('[Keep the channel open for another work session.]', flags=f("field_work_continues", "second_question_open")),
              c('[End the meeting. Let the next invitation come from her.]', flags=f("closed", "field_exit"), abort=True)),
            n("field_interest_declined", "Areelu", '''Areelu holds your gaze for a moment. "I am disappointed. I am not owed a different answer, and you are not responsible for making that disappointment smaller."

She gathers the surviving notes. The attraction has been named, and you have refused it. She does not recast that refusal as fear or ask you to reconsider.''',
              c('[Keep future contact about the work only.]', "field_professional", flags=f("field_work_continues", "second_question_open")),
              c('[End contact here.]', flags=f("closed", "field_exit"), abort=True)),
            n("field_next_step", "Areelu", '''"I want another meeting," she says. "I am not promising what I will want when it comes. You have permission to ask again, and I have the right to answer no."

"That is more than you offered before."

"It is more than I knew before." She retrieves her notes. "Do not turn progress into a contract. I am choosing the next question, not the rest of my life."''',
              c('[Accept the next meeting without setting terms for her answer.]', flags=f("field_work_continues", "second_question_open")),
              c('[Tell her to contact you only when she wants the conversation, not the contest.]', flags=f("field_work_continues", "second_question_open")),
              c('[End contact here. You have both said enough.]', flags=f("closed", "field_exit"), abort=True)),
        ],
        requires=("areelu.trickster_opening.second_question_open", RIVALRY_FLAG, "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=48,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_inventory",
        "What the work made possible",
        "Areelu",
        5,
        "inventory_entry",
        [
            n("inventory_entry", "Areelu", '''The invitation says "not an experiment." It brings you to a records room beneath the laboratory, where a ledger and a dozen witness statements lie in separate stacks. The ledger turns people into logistics: supplies redirected, prisoners moved, a village abandoned after a ward shifted. Names are missing; numbers have been corrected; one total ends with "at least."

"You asked what the failed restoration cost me," Areelu says. "I answered with the loss I can bear to describe. This is what I avoid. The work did not fail in isolation. I made other people expendable, then called the result necessary." She opens the ledger. "I want to know whether the calculation was wrong, or whether calculation was only what I could bear to look at. Do not offer absolution. Examine the record with me, and tell me what you require first." Her attraction has not made this an invitation to trust her. The names remain absent, and the choice remains yours.''',
              c('[Restore every recoverable name before reviewing a calculation.]', "inventory_terms", flags=f("inventory_names_required")),
              c('[Create a counterledger that keeps each person beside the figures.]', "inventory_terms", flags=f("inventory_counterledger")),
              c('[Refuse to make the Worldwound legible as another puzzle.]', "inventory_exit", flags=f("inventory_refused"))),
            n('inventory_terms', 'Commander', '''You name the conditions: recovered identities beside totals, uncertainty written plainly, and independent witnesses allowed to correct the record. Context may explain a decision; it does not turn a choice into necessity. You will not edit the result for her or sign it as her advocate.

Areelu reads the terms twice. "Inconvenient." She pulls the ledger to the center of the table. "Proceed." The first entry concerns a caravan diverted from a ward station. The official account says the detour preserved the ritual's timing. A margin note says it carried civilians from a village struck by a planar surge. The number is crossed out and replaced with "at least twenty-seven."

You ask how many names she can recover, who made the decision, what she knew about the surge, and whether another road existed. She answers the first three. "There was another road. It would have cost two days and weakened the ward. I decided the timing mattered more. I can tell you why. I cannot prove I was forced." The answer is not absolution. It is a fact she had previously left outside the ledger.

The review takes hours. Some records are incomplete; some are coded. Once, Areelu closes the book and turns away. She returns without asking you to make the silence easier. By the end there are nine names, three uncertain identifications, and a blank where the missing remain uncounted. Areelu writes the uncertainty beside the figure. It is a small act next to the harm, and she does not pretend it balances anything.''',
              c('[Send the names and her account to an independent archivist under Areelu’s own signature.]', next='inventory_consequence', flags=['areelu.trickster_opening.inventory_independent_record']),
              c('[Keep a private counterledger while she verifies the names herself.]', next='inventory_private_consequence', flags=['areelu.trickster_opening.inventory_private_record']),
              c('[Stop here. Do not supervise what she does with the record.]', next='inventory_exit', flags=['areelu.trickster_opening.inventory_stopped'])),
            n('inventory_private_consequence', 'Areelu', '''Areelu separates the names from the calculations and folds the counterledger into a leather case.
"No courier," she says. "No audience. If you want an accusation made public, make it openly. Do not smuggle one out in my handwriting."
She sets six disputed names beside the case. She will compare them against the caravan rolls herself.
"Return when I have checked these. You may find my explanation wanting. You may even be right."
Her fingers remain on the lid until you step away.''',
              c('[Return to hear her findings.]', next='inventory_end', flags=['areelu.trickster_opening.inventory_witnessed']),
              c('[Leave the comparison to her. Keep contact professional.]', next='inventory_end', flags=['areelu.trickster_opening.inventory_professional', 'areelu.trickster_opening.rivalry_only'])),
            n('inventory_consequence', 'Areelu', '''"An archivist may call my choices monstrous," she says. "They will be right about the choices. They may misunderstand the forces around them." She gathers the witness statements but leaves the names visible. "I do not control the account simply because I understand the machinery better. Send it." She refuses your offer to submit it for her. The letter will bear her name; the answer will come to her.

When she seals it, you notice her fingers shaking. She presses them flat against the table until they stop. You do not reach for her. She does not ask you to.

"There is a temptation to pretend the next choice will be cleaner because this one was honest. It will not. I want you here when I open the reply. I am not sure whether that is trust, attraction, or a desire for a witness. You may decline without explaining which."''',
              c('[Agree to witness it, without promising forgiveness.]', next='inventory_end', flags=['areelu.trickster_opening.inventory_witnessed']),
              c('[Agree only if you can leave at any point.]', next='inventory_end', flags=['areelu.trickster_opening.inventory_witnessed', 'areelu.trickster_opening.exit_right_explicit']),
              c('[Decline personally; keep only a professional channel.]', next='inventory_end', flags=['areelu.trickster_opening.inventory_professional', 'areelu.trickster_opening.rivalry_only'])),
            n("inventory_exit", "Areelu", '''Areelu closes the ledger. "Then we stop. I dislike the result. It does not make the record yours to repair." She puts the statements in a locked case. "I will decide what to do. You are not my keeper, and I will not pretend this work has no value because you chose not to participate." Her gaze searches your face, but she does not ask you to soften your answer. "If there is another invitation, it will concern the calculation. Nothing else."''',
              c('[Keep the channel strictly professional.]', flags=f("closed", "inventory_exit_final"), abort=True),
              c('[Close contact entirely.]', flags=f("closed", "inventory_exit_final"), abort=True)),
            n('inventory_end', 'Commander', '''You leave the ledger in Areelu's keeping. The disputed names still lack answers.
She has agreed to check them, although she rejects your explanation of the decision that put them in danger.
"Bring a better argument next time," she says as you reach the door. "I have heard this one."
Whether her findings leave the room depends on the arrangement you made. Your presence has not made the account yours to distribute.''',
              c('[Agree to meet after the reply, without setting its terms.]', flags=['areelu.trickster_opening.inventory_complete', 'areelu.trickster_opening.second_question_open']),
              c('[Leave the next contact to her.]', flags=['areelu.trickster_opening.inventory_complete', 'areelu.trickster_opening.second_question_open'])),
        ],
        requires=("areelu.trickster_opening.field_work_continues", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=72,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_reply",
        "The witness who does not forgive",
        "Areelu",
        5,
        "reply_entry",
        [
            n('reply_entry', 'Commander', '''Areelu has finished comparing the caravan rolls. A folder waits under her hand.
"Six names and two dates," she says. "You may examine the sources. You may also spare me your expression of satisfaction until you have read them."''',
              c('[Read the findings together.]', next='reply_findings_choice', forbids=['areelu.trickster_opening.rivalry_only']),
              c('[Receive only the written findings.]', next='reply_professional', requires=['areelu.trickster_opening.rivalry_only'])),
            n('reply_public_findings', 'Commander', '''The archivist's reply arrives sealed. Areelu asks you to meet in the records room. "I wanted you here. I will not tell you I need you. If you leave before I open this, I will still open it." She has been practicing asking without turning an answer into an obligation.

The archivist identifies six names, corrects two dates, and finds that the caravan route changed after Areelu's order. That weakens one of her explanations. The letter also records the cost of the weakened ward: a second settlement lost its outer district. The writer asks whether Areelu would make the decision again, knowing both outcomes.

Areelu reads the question twice. Her face stays composed; one hand closes on the table. "They are not wrong to ask. I am not obliged to like it." She looks up. "You can answer first, or say nothing. This is my account."''',
              c('[Name that the changed route weakens her defense; the answer remains hers.]', next='reply_answer', flags=['areelu.trickster_opening.reply_evidence_named']),
              c('[Ask whether she can accept an answer more complicated than yes or no.]', next='reply_answer', flags=['areelu.trickster_opening.reply_complexity_requested']),
              c('[Stay silent and let her face the letter without your interpretation.]', next='reply_answer', flags=['areelu.trickster_opening.reply_silence_respected'])),
            n('reply_private_findings', 'Areelu', '''Areelu opens the leather case herself. No seal has been added, no copy sent away.
Her notes identify six names, correct two dates, and show that the caravan changed course after her order. A settlement beyond its intended route lost its outer district when the ward weakened.
She has crossed out one of her own explanations with a single heavy stroke.
"That defense no longer holds. The others do."
You ask whether she would make the decision again.
She looks up sharply. "You have read one page. At least read the second before deciding you understand the choice."''',
              c('[Read the second page, then hear her answer.]', next='reply_answer', flags=['areelu.trickster_opening.reply_evidence_named'])),
            n('reply_findings_choice', 'Areelu', '''The folder contains the comparison you arranged.''',
              c("[Open the archivist's account.]", next='reply_public_findings', requires=['areelu.trickster_opening.inventory_independent_record']),
              c('[Read the private counterledger.]', next='reply_private_findings', requires=['areelu.trickster_opening.inventory_private_record'])),
            n('reply_professional', 'Areelu', '''Areelu supplies the six recovered names and two corrected dates through the agreed channel. No personal question accompanies them. The document remains private unless you separately agree to release it.''',
              c('[Keep the research channel open.]', flags=['areelu.trickster_opening.reply_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.rivalry_only'])),
            n('reply_answer', 'Areelu', '''"I would make the choice again if the ritual were still the only chance to close the Worldwound. I would not call the caravan expendable. I would record the names first, and try the second road before deciding two days were impossible. I cannot tell you whether I would succeed." Her answer has no neat conclusion. It does not erase the dead or pretend every cost was unavoidable.

"If that question is asked again, I will answer the same unless the evidence changes. I will not edit the account to make it sound merciful." She rests her fingertips on the table, avoiding yours. "Tell me what you heard. Do not tell me what I should feel."''',
              c('[A choice acknowledged, not a debt settled.]', next='reply_relationship_question', flags=['areelu.trickster_opening.choice_acknowledged']),
              c('[A necessity preserved; you cannot decide if it is enough.]', next='reply_relationship_question', flags=['areelu.trickster_opening.necessity_preserved']),
              c('[An answer you are not entitled to approve or reject for those harmed.]', next='reply_relationship_question', flags=['areelu.trickster_opening.judgment_refused'])),
            n('reply_relationship_question', 'Areelu', '''"Good. Do not decide for them, and do not decide for me." She folds the account, stops halfway, and opens it again. "I wanted desire to make this easier. It does not. It makes me want to choose the witness who understands me, which is why I should not choose the witness who approves my account."

She looks at you. "You can want me and disagree with what I did. If you cannot, I would rather know now. I am attracted to you. I am considering whether to let that become a relationship. I will not offer a cure for grief or a share in my work as payment. I want to know what desire looks like when neither of us gets to claim the other as an answer."''',
              c('[Explore a relationship, with separate lives and an open right to leave.]', next='reply_terms', flags=['areelu.trickster_opening.relationship_exploration_accepted']),
              c('[Keep meeting, but do not name it a relationship yet.]', next='reply_terms', flags=['areelu.trickster_opening.relationship_exploration_slow']),
              c('[Decline. Attraction alone is not enough for the life you want.]', next='reply_declined', flags=['areelu.trickster_opening.relationship_exploration_declined'])),
            n('reply_terms', 'Commander', '''You name your terms: no access to your mind without permission; no Trickster intervention that manufactures affection; no touch or sex as proof; no demand that private intimacy endorse her public choices. You will not promise exclusive attention just because you choose to explore her. Other relationships are possible only with informed consent from everyone affected. No one will be used to provoke jealousy, and no hidden experiment will replace a spoken yes.

Areelu listens without interrupting. "Inconvenient," she says. "Which is one reason I believe you mean them. I can agree. I will be poor at some of this. If I make my failure your responsibility, tell me. If I refuse to hear you, leave." She offers her hand but does not close the space.''',
              c('[Ask if she wants you to take her hand now, and wait for her answer.]', next='reply_touch', flags=['areelu.trickster_opening.relationship_terms_agreed']),
              c('[Say you want to wait before touching. The agreement stands on its words.]', next='reply_no_touch', flags=['areelu.trickster_opening.relationship_terms_agreed', 'areelu.trickster_opening.touch_deferred']),
              c('[Ask to revisit these terms after you have both considered them.]', next='reply_pause', flags=['areelu.trickster_opening.relationship_terms_pending'])),
            n('reply_no_touch', 'Areelu', '''Areelu lowers her offered hand.
"Words, then. We have never lacked those."
She leans against the table, leaving the distance between you open.
"I am interested in finding out whether we can bear each other without an experiment to blame. That may be the less reasonable undertaking."
You remain where you are. Neither of you reaches across the space.''',
              c('[Begin the relationship at this distance.]', next='reply_end', flags=['areelu.trickster_opening.relationship_started']),
              c('[End personal contact.]', flags=['areelu.trickster_opening.closed', 'areelu.trickster_opening.relationship_ended'], abort=True)),
            n('reply_touch', 'Areelu', '''You ask. She says yes. You take her hand only after the answer is clear. Her fingers close around yours with more force than the gesture requires; when she notices, she loosens them without letting go.

"I do not know how to do this without trying to control the variables," she says. "I will likely try anyway." The admission has no polished edge. You tell her you will name it when she does, and expect her to listen rather than promise never to fail. Her thumb moves once over your knuckles, then stills. The touch is chosen and brief. It settles nothing about the dead, the graft, or the next time she will have to face a choice that cannot be solved by either of you.''',
              c('[Agree to begin, knowing this will require correction and may end.]', next='reply_end', flags=['areelu.trickster_opening.relationship_started']),
              c('[End the contact now. The terms were not enough.]', flags=['areelu.trickster_opening.closed', 'areelu.trickster_opening.relationship_ended'], abort=True)),
            n("reply_pause", "Areelu", '''"Then we wait," she says. "A pause is not rejection, but it is not consent either." She puts the letter away. "When you decide, tell me. Until then, we keep the channel on the terms we already established."''',
              c('[Remain rivals while the relationship stays undecided.]', "reply_end", flags=f("relationship_paused")),
              c('[End personal contact.]', flags=f("closed", "relationship_paused"), abort=True)),
            n("reply_declined", "Areelu", '''Areelu closes her hand. "Then I will not turn no into a negotiation." Her disappointment is plain, and she does not make it your problem. "You may still challenge my work. You may also end contact."''',
              c('[Keep the research channel open without romantic expectation.]', "reply_end", flags=f("relationship_declined_final", "rivalry_only")),
              c('[End contact entirely.]', flags=f("closed", "relationship_declined_final"), abort=True)),
            n('reply_end', 'Commander', '''Areelu closes the folder and puts it with the rest of her work. Its destination remains the one you agreed upon.
"I could send you something without a calculation attached," she says. "Assuming you would recognize it."
There is enough mockery in her voice to make the offer easy to refuse, and enough attention to make clear that she is waiting for the answer.''',
              c('[Invite her to write, and agree that either of you may ask for a pause.]', flags=['areelu.trickster_opening.reply_complete', 'areelu.trickster_opening.second_question_open']),
              c('[Keep contact to scheduled meetings for now.]', flags=['areelu.trickster_opening.reply_complete', 'areelu.trickster_opening.second_question_open'])),
        ],
        requires=("areelu.trickster_opening.inventory_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=96,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_second_graft",
        "A future that is not a replacement",
        "Areelu",
        5,
        "graft_entry",
        [
            n('graft_entry', 'Areelu', '''A week passes before Areelu asks you to return to the laboratory. The invitation does not mention romance. It says that she has found a discrepancy in the failed restoration record and wants you present before she decides what it means.

The workbench holds no crystal and no living subject. There is a diagram of the original ritual, annotated in two hands: Areelu's, and the archivist's corrections. A third page is blank except for one sentence: "If restoration is possible, what exactly would it restore?"

"I have not started anything," she says. "I will not. I wanted to know whether the question can be made precise before I let my desire for an answer become an excuse." She points to the diagram. "The old attempt was intended to return my child. It did not. Your soul was not a continuation of theirs, and you are not a substitute. The remnants may have changed you. I do not know how much. I have wanted to turn that uncertainty into a second attempt because I cannot bear that the first one ended with nothing I could call success."

She does not ask you to reassure her. The line between her and the work is visible, not safe. "There is a theoretical path that might produce a new life carrying some echo of the remnants. It would not bring my child back. It could produce a person with no consent to be a vessel for my grief. I could destroy the draft and never return to it. I could study it only as an abstract historical question, without a subject, without a procedure, and with independent review. Or I could admit I still want it. I will not call that want a plan."

This is the first time she has brought desire to you as a danger she intends to govern, rather than as evidence that the danger is worth taking. Your answer cannot decide for her, but it can define what place you will accept beside her.''',
              c('[Tell her to destroy the draft. No possible child should inherit this experiment.]', next='graft_destroy', flags=['areelu.trickster_opening.graft_draft_destroyed']),
              c('[Allow historical study only: no procedure, no subject, independent review, and no revival of the dead child claim.]', next='graft_study', flags=['areelu.trickster_opening.graft_study_limited']),
              c('[Tell her honestly you understand why she wants it, but will not help her make that want into a new life.]', next='graft_refusal', flags=['areelu.trickster_opening.graft_desire_named'])),
            n("graft_destroy", "Commander", '''"Destroy it. Not because I think your grief is foolish, but because the person you hope to recover cannot consent to be recovered through someone else. No living person should be asked to become the proof that your first ritual meant something."''',
              c('[Stay while she destroys the draft, without making the act a test of her love for you.]', "graft_aftermath", flags=f("graft_draft_destroyed", "graft_witnessed")),
              c('[Leave her to make the choice alone. The decision is hers.]', "graft_aftermath", flags=f("graft_draft_destroyed", "graft_private"))),
            n("graft_study", "Commander", '''"Study what happened, not how to repeat it. No subject, no procedure, and no claim that another child could restore the one you lost. An outside scholar gets the unedited record. If the question turns back into a plan, I leave."''',
              c('[Ask her to sign the limits and send the draft for independent review.]', "graft_aftermath", flags=f("graft_study_limited", "graft_external_review")),
              c('[Ask her to stop here. You do not trust the research to remain abstract.]', "graft_aftermath", flags=f("graft_draft_destroyed", "graft_study_refused"))),
            n("graft_refusal", "Areelu", '''"You understand the want," Areelu says, "and refuse to help me obey it." Her mouth tightens. "I do not like that answer. I believe it is the answer I needed to hear." She rests her hand on the blank page without writing. "I will not ask you to stand beside me while I turn grief into another person's obligation."''',
              c('[Tell her she must decide what to do without using your affection as permission.]', "graft_aftermath", flags=f("graft_desire_named", "graft_boundary_set")),
              c('[End the relationship. This is the line you cannot trust her not to cross.]', flags=f("closed", "graft_relationship_ended"), abort=True)),
            n('graft_aftermath', 'Areelu', '''The draft goes into the brazier, or the sealed archive, according to the limits you chose. Areelu watches until the last line is no longer legible. She does not make the choice look easy. The grief stays; nothing in the room returns what she lost.

"I thought that if I could formulate the question correctly, the answer might excuse my wanting it," she says. "It cannot. A sound method would still have to answer for the person it creates. I do not know whether destroying the draft is wisdom or another attempt to control the result. But tonight I chose not to produce someone who would owe me an explanation for being alive."

You tell her that you cannot grant her absolution. She answers that she did not ask for it. If she chose limited study, she says the archivist will receive the complete record and the right to publish it. If she destroyed the draft, she says she will not rebuild it in secret. The promise is specific enough to be tested later.

She looks at you. "I want to be with you. I also want the thing I just gave up. Both are true. If I pretend one cancels the other, you should distrust me." The room is quiet. Her hand remains on the table, close to yours but not touching.''',
              c('[Stay in the relationship while she grieves, with accountability beyond your private bond.]', next='graft_close', flags=['areelu.trickster_opening.graft_consequence_faced']),
              c('[Pause the relationship until independent review confirms the boundary held.]', next='graft_no_touch', flags=['areelu.trickster_opening.graft_consequence_faced', 'areelu.trickster_opening.relationship_paused']),
              c('[Leave. You cannot build intimacy around a promise you do not trust.]', flags=['areelu.trickster_opening.closed', 'areelu.trickster_opening.graft_relationship_ended'], abort=True)),
            n('graft_no_touch', 'Areelu', '''Areelu leaves her hand on the table. You take your cloak.
"Send word when you want another conversation," she says. "I have work that can survive without your approval."
You leave the laboratory alone.''',
              c('[Keep the pause.]', flags=['areelu.trickster_opening.graft_scene_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.relationship_paused'])),
            n('graft_close', 'Commander', '''You do not touch her until you ask. She says yes to your hand and no to being held. You honor both answers. Her fingers close around yours for a moment, then release.

"That was not a cure," she says.

"It was a choice."''',
              c('[Continue, knowing there will be future reviews of the promise and no guaranteed forgiveness.]', flags=['areelu.trickster_opening.graft_scene_complete', 'areelu.trickster_opening.second_question_open']),
              c('[End the personal part here and keep only the research channel.]', flags=['areelu.trickster_opening.graft_scene_complete', 'areelu.trickster_opening.rivalry_only', 'areelu.trickster_opening.second_question_open'])),
        ],
        requires=("areelu.trickster_opening.relationship_started", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=168,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_private_hour",
        "What she asks for",
        "Areelu",
        5,
        "private_entry",
        [
            n("private_entry", "Commander", '''Areelu sends an invitation without a diagram attached. It gives you a private evening in the rooms she has chosen for herself, away from the laboratory and the people who still call her Lady. When you arrive, the wine is unopened, the door is unlocked, and she is standing at the window in a dark red robe over the black clothes she wears when she expects to work.

"I have been told this is where one is supposed to make a gesture," she says. "I have prepared three possible openings, and each sounds like a threat when I say it aloud." She looks back at you. "So I will ask plainly. I want you here. I want to touch you. I want to know whether you want the same, and I will accept any answer without turning it into a diagnosis."''',
              c('[Tell her you want her, but ask to talk first about what each of you expects from tonight.]', "private_terms", flags=f("private_desire_mutual")),
              c('[Say you want her too. Ask her to tell you what she wants, one thing at a time.]', "private_terms", flags=f("private_desire_mutual")),
              c('[Tell her you are not ready for touch tonight.]', "private_pause", flags=f("private_touch_declined"))),
            n("private_terms", "Areelu", '''She asks what you expect. You say you want desire without turning it into a reward for surviving her history. You want to be allowed to stop. You want her to be allowed to stop. You will not make her body a confession or your own a reassurance. You do not want to be treated as a second chance to restore someone else. If she wants to speak about the graft, she must ask first; if either of you changes your mind, the evening ends without argument.

Areelu hears each term and gives her own: do not call her a monster to make her feel more exciting; do not ask her to perform cruelty for your pleasure; do not promise to save her from herself. She wants to be touched as herself, not as a symbol of the Worldwound or its opposite. She wants the freedom to say what she wants without that answer being used to predict what she will want later.

"I want your hands on my waist," she says. "I want your mouth on mine. I may want more. I do not promise that I will, and I do not want you to decide that for me." She steps close enough for you to feel her warmth but does not touch you. "May I kiss you?"''',
              c('[Say yes, and keep the kiss slow enough for either of you to stop.]', "private_kiss", flags=f("private_touch_consented")),
              c('[Ask for one kiss, then a pause to check in.]', "private_kiss", flags=f("private_touch_consented", "checkin_requested")),
              c('[Change your mind. No kiss tonight.]', "private_pause", flags=f("private_touch_declined"))),
            n('private_kiss', 'Commander', '''You say yes. Areelu watches your face for one last beat, then kisses you. The first touch is controlled, almost formal. You feel the pause in it: the place where she could turn back and chooses not to. You keep your hands visible until she guides one to her waist. The fabric is warm beneath your palm. She draws a breath against your mouth and makes a small sound she would dismiss as irrelevant if you teased her about it.

The kiss deepens by degrees, not because either of you has won an argument, but because each answer creates room for the next question. When she pulls away, she stays close. Her gaze moves over your face, searching for regret rather than permission to continue.

"I want more," she says. "I also want to stop here and remember that I asked." She waits.''',
              c('[Tell her you want more too, and ask before you loosen the robe at her shoulder.]', next='private_after', flags=['areelu.trickster_opening.private_desire_confirmed']),
              c('[Say the kiss is enough for tonight. Stay close without escalating.]', next='private_kiss_only', flags=['areelu.trickster_opening.private_desire_confirmed', 'areelu.trickster_opening.intimacy_stopped_by_choice']),
              c('[Stop and leave. You do not want to continue.]', next='private_departure', flags=['areelu.trickster_opening.private_desire_withdrawn'])),
            n('private_kiss_only', 'Areelu', '''"Enough," you say, keeping your hand still at her waist.
Areelu draws back. For a moment her impatience shows; then she straightens the robe at her shoulder herself.
"You choose inconvenient stopping places."
"I learned from you."
That earns a brief smile. You sit beside the unopened wine and talk until the lamp begins to smoke. The kiss remains the last touch of the evening.''',
              c('[Say good night.]', next='private_close', flags=['areelu.trickster_opening.private_evening_shared', 'areelu.trickster_opening.intimacy_stopped_by_choice'])),
            n('private_departure', 'Areelu', '''You step back and take your hand from her waist.
"I want to leave."
Areelu releases you immediately. She stays beside the table while you fasten your cloak.
"Then go. I will not chase an explanation down the stairs."
The door closes behind you. You return to your own room alone.''',
              c('[Leave the evening there.]', next='private_close', flags=['areelu.trickster_opening.private_desire_withdrawn', 'areelu.trickster_opening.intimacy_stopped_by_choice'])),
            n('private_after', 'Areelu', '''She answers the next question with a deliberate yes. You draw the robe from one shoulder and stop when her hand covers yours. She says, "Wait," and you do. Her breathing steadies. She checks the clasp at your collar, asks whether she may open it, and waits for your answer. No one rushes to make the moment mean more than it does.

If you both choose to continue, the room grows warmer and the door stays unlocked. Areelu's confidence returns in flashes, alongside uncertainty she cannot discipline away. She guides your hands; you ask before each new touch. She asks what you want and listens to the answer. When she draws you toward the bed, the choice is mutual, unhurried, and private. The lamp burns low while the city quiets beyond the window.

Later, she lies on her side with one arm beneath the pillow. She does not ask whether you have forgiven her. You do not ask whether this has changed what she did. Her hand finds your wrist and rests there, light enough that you could move away without waking her.

"I wanted this," she says. "I want it again. That does not tell me what I will be capable of tomorrow." She turns toward you. "Can you let tonight be real without calling it a cure?"''',
              c('[Yes. Stay with her, and agree to talk again in the morning.]', next='private_close', flags=['areelu.trickster_opening.private_evening_shared']),
              c('[Yes, but go back to your own room. Desire does not erase the need for space.]', next='private_close', flags=['areelu.trickster_opening.private_evening_shared', 'areelu.trickster_opening.space_after_intimacy']),
              c('[No. This crossed a boundary you did not know you had. Leave and pause the relationship.]', next='private_close', flags=['areelu.trickster_opening.private_evening_unsettled', 'areelu.trickster_opening.relationship_paused'])),
            n("private_pause", "Areelu", '''Areelu nods. The disappointment comes and goes across her face before she can conceal it. "Thank you for telling me before I had to guess." She asks whether you would like her to sit with you, speak about something else, or let you go alone. When you choose, she follows that choice without bargaining for another answer.''',
              c('[Stay and talk. You want closeness without touch.]', "private_close", flags=f("private_evening_paused")),
              c('[Leave for tonight and keep the next meeting undecided.]', "private_close", flags=f("private_evening_paused"))),
            n('private_close', 'Commander', '''Areelu's note arrives through the courier before the next invitation. It asks whether you want to meet again, without claiming how you spent the night. You answer from your own rooms.''',
              c('[Keep the relationship, and keep talking about boundaries as they change.]', flags=['areelu.trickster_opening.private_scene_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.delivered.private_close']),
              c('[Pause and return to the relationship only after both choose it again.]', flags=['areelu.trickster_opening.private_scene_complete', 'areelu.trickster_opening.relationship_paused', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.delivered.private_close']),
              c('[End the romance, but keep the professional channel open.]', flags=['areelu.trickster_opening.private_scene_complete', 'areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.rivalry_only', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.delivered.private_close'])),
        ],
        requires=("areelu.trickster_opening.relationship_started", "areelu.trickster_opening.active_trickster_path", ENTRY_READY, "areelu.trickster_opening.graft_scene_complete"),
        forbids=("areelu.trickster_opening.closed", "areelu.trickster_opening.relationship_paused"),
        delay=96,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_open_record",
        "The answer belongs to more than you",
        "Areelu",
        5,
        "record_entry",
        [
            n('record_entry', 'Areelu', '''The archivist has been examining independently acquired records and finds an old field ledger that was absent from the surviving public accounts: a record of the ward failures that preceded the caravan order. It shows that one of Areelu's assistants warned her about the second road, and that Areelu sent the assistant away before making the choice.

Areelu asks you to meet at the archive. The report sits open between you. Beside it is a sealed invitation from the archivist to present the findings before a panel of survivors and scholars. The meeting would identify Areelu as the decision-maker. It would also expose the assistant, whose warning was treated as insubordination and who now lives under another name.

"I knew there had been an objection," Areelu says. "I did not know the warning was this specific. I remembered the assistant as someone who could not accept the risk. That is how I made the order easier to give." She looks at the letter. "The panel wants a public account. If I attend, they will ask why I ignored the warning. If I do not, the archivist can publish the record without my testimony. The assistant may be identified regardless."

She turns the page to you. "I want to go. I want to control what is said. I want to keep the assistant safe. I cannot guarantee all three. You have been clear that you are not my advocate. I am asking you to help me choose what not to control."

The archivist obtained this ledger separately. Any counterledger you kept private remains in Areelu's case; this invitation gives nobody permission to open it.''',
              c('[Insist the assistant’s identity stays sealed unless they choose otherwise, even if that weakens Areelu’s public defense.]', next='record_protection', flags=['areelu.trickster_opening.assistant_identity_protected']),
              c('[Ask Areelu to testify publicly and accept that the panel may reject her explanation.]', next='record_testimony', flags=['areelu.trickster_opening.areelu_testimony_chosen']),
              c('[Recommend delaying the hearing until the assistant can be contacted through the archivist.]', next='record_delay', flags=['areelu.trickster_opening.hearing_delayed']),
              c('[Knowledge: World, DC 34] The field ledger proves a warning was ignored, but does not prove the assistant’s identity or consent to be named.', check={'Skill': 'SkillKnowledgeWorld', 'DC': 34, 'Success': 'record_world_success', 'Failure': 'record_world_failure', 'CommanderOnly': True})),
            n("record_world_success", "Commander", '''You point to the dates. The assistant's warning precedes the order, but the signature has been copied into a later summary. It is not enough to identify the writer with certainty. The letter from the archivist already offers a private channel to confirm the name without putting it in the public record.

Areelu reads the passage, then the offer. "You have found a way to ask without pretending the answer is ours." Her voice tightens. "Do not look pleased. I am grateful, and I dislike owing anyone a better question."''',
              c('[Use the private channel and let the assistant decide whether to be named.]', "record_protection", flags=f("assistant_contact_offered")),
              c('[Leave the question to the archivist. Areelu should not reach out to someone she once overruled.]', "record_delay", flags=f("assistant_contact_withheld"))),
            n("record_world_failure", "Commander", '''You cannot establish whether the signature belongs to the assistant or to someone who copied the report. Areelu catches the uncertainty in your answer.

"Then do not make it certainty," she says. "The hearing can wait while the archivist verifies it. Or I can testify to the decision I know I made, without attaching a name I cannot prove."''',
              c('[Delay the hearing and ask the archivist to contact the assistant privately.]', "record_delay", flags=f("hearing_delayed", "assistant_contact_offered")),
              c('[Testify to the decision without claiming to know who warned her.]', "record_testimony", flags=f("areelu_testimony_chosen"))),
            n("record_protection", "Areelu", '''Areelu looks at the invitation for a long moment. "If the assistant remains unnamed, the panel will ask why I am asking them to trust an account that cannot be checked." She does not look at you. "That will be a fair question. I can testify to the order, the warnings I received, and the fact that I sent the person away. I do not need to say who it was."

The choice costs her the most useful piece of context. It also refuses to make the assistant pay for Areelu's honesty. She asks the archivist to preserve the original ledger and mark the identity uncertain. The instruction is in writing, signed by the person who could have controlled the record and chose not to.''',
              c('[Attend the hearing as a witness to the process, not as her defender.]', "record_outcome", flags=f("record_terms_preserved")),
              c('[Stay away. She should answer without relying on your presence.]', "record_outcome", flags=f("record_terms_preserved", "commander_absent"))),
            n("record_testimony", "Areelu", '''"I will attend," Areelu says. "I will state what I did and what the ledger proves. I will not claim the assistant's warning was vague. I will not name them without consent. If the panel decides that this makes my account incomplete, they can say so in the record."

The day of the hearing, she speaks without asking you to stand behind her. The panel interrupts twice. One member asks whether a different order would have saved everyone. Areelu answers that she does not know. When the archivist asks why she sent the assistant away, she says she wanted fewer objections, not better evidence. The admission changes the room. It does not make the room forgive her.''',
              c('[Attend without signaling agreement with her answer.]', "record_outcome", flags=f("record_terms_preserved")),
              c('[Do not attend. Her testimony should stand on its own.]', "record_outcome", flags=f("record_terms_preserved", "commander_absent"))),
            n("record_delay", "Areelu", '''Areelu signs a request to delay the hearing. The archivist will contact the assistant through the private channel, share only the relevant entry, and ask whether they wish to confirm or remain unnamed. The panel may refuse the delay; no one promises the identity will stay secret forever. Still, the first question now belongs to the person whose choice it concerns.

"You could have made the delay sound like cowardice," she says. "It would have been easier for me to reject it. You made me see the difference between hiding a fact and refusing to expose someone who has not agreed to be part of my confession."''',
              c('[Attend only if the assistant chooses to participate.]', "record_outcome", flags=f("record_terms_preserved")),
              c('[Leave the hearing to Areelu and the archivist.]', "record_outcome", flags=f("record_terms_preserved", "commander_absent"))),
            n("record_outcome", "Areelu", '''The hearing does not decide whether Areelu is forgiven. It records the order, the warning, the delay she imposed, and the lives lost when she chose the ritual's timing. The panel asks for the unedited materials to remain available. Areelu signs the release. The assistant's name stays sealed unless they later choose to speak.

Outside, Areelu's composure slips. She presses her fingertips against the stone wall, not to steady herself but to feel that it is there. "I thought an honest account would make the next choice obvious," she says. "It did not. It only made the people affected visible again."''',
              c('[Tell her you are proud of the choice, while making clear that pride is not absolution.]', "record_private", flags=f("record_public_consequence")),
              c('[Tell her you cannot praise her for admitting what she did, but you can stay while she faces the response.]', "record_private", flags=f("record_public_consequence")),
              c('[Say you need distance after seeing how much harm her choices reached.]', "record_pause", flags=f("record_relationship_distance"))),
            n("record_private", "Commander", '''She asks whether you still want the relationship. There is no wager in the question. She will continue the public record whether you stay or leave. You are not being asked to reward her for telling the truth, and your answer cannot take the hearing back.''',
              c('[Stay. You want her, and you will continue to challenge the choices that need challenging.]', "record_end", flags=f("record_relationship_continues")),
              c('[Stay, but pause physical intimacy until you both have lived with the hearing’s consequences.]', "record_end", flags=f("record_relationship_continues", "relationship_paused")),
              c('[End the romance. You can recognize her effort and still decide this relationship is not for you.]', "record_end", flags=f("relationship_ended", "rivalry_only"))),
            n("record_pause", "Areelu", '''Areelu accepts the distance. She does not pursue you down the corridor or recast your answer as fear. "Take it," she says. "I will not promise that the record ends here. I will not ask you to stay close while I learn how to live with it."''',
              c('[Pause the relationship and keep contact limited to the research.]', "record_end", flags=f("relationship_paused", "rivalry_only")),
              c('[End the relationship and close personal contact.]', "record_end", flags=f("relationship_ended", "rivalry_only"))),
            n('record_end', 'Commander', '''The record remains open. Areelu has not become good because she made one difficult choice, and she has not become incapable of change because she made the earlier ones. Your future is not a reward she earns by suffering in public. It is a decision both of you keep making, with room for disagreement and for an ending neither can control alone.''',
              c('[Keep the agreed channel and the completed record.]', flags=['areelu.trickster_opening.record_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.delivered.record_entry']),
              c('[Close the personal relationship while leaving her public account untouched.]', flags=['areelu.trickster_opening.closed', 'areelu.trickster_opening.record_arc_complete', 'areelu.trickster_opening.delivered.record_entry'], abort=True)),
        ],
        requires=("areelu.trickster_opening.private_scene_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=120,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_returned_names",
        "The account leaves the archive",
        "Areelu",
        5,
        "returned_entry",
        [
            n('returned_entry_active', 'Areelu', '''Since the public hearing, the archivist has received three letters from families who recognize the recovered names. One asks for copies of every record connected to a missing daughter. One requests funds to rebuild a water ward that the old ledger lists as an acceptable loss. The third contains no request at all. It says only that the writer knows who signed the order and does not want Areelu to come to their door.

Areelu lays the letters on a table in the records room. She has marked no reply. A fourth sheet lists what she can offer: copies, compensation, the names of the officials who carried out each order, and a public correction to the original report. The list is extensive. Every item is also a way to remain at the center of the account.

"The easiest answer is to give them what I can give," she says. "The harder question is whether giving it becomes another way to dictate what they are allowed to ask from me." Her gaze moves to the letter refusing a visit. "I want to answer all three. I want the writer to meet me and say what they think of me. That would satisfy my curiosity. It would not serve them."

She looks at you, not asking for a moral verdict. "I need to decide what the record owes them, and what I owe the person who wants no contact. The archivist can transmit material without my presence. I can also keep the letters private and tell myself I am protecting them. Which choice can I live with when no one thanks me for it?"''',
              c('[Send the requested copies and water-ward funds through the archivist; honor the no-contact request without a personal reply.]', next='returned_materials', flags=['areelu.trickster_opening.letters_private_boundary']),
              c('[Ask the archivist to offer each writer the same complete record and let each decide whether they want compensation or contact.]', next='returned_choice', flags=['areelu.trickster_opening.letters_recipient_choice']),
              c('[Publish the correction and funding offer at once, even if the families would rather not be named publicly.]', next='returned_confrontation', flags=['areelu.trickster_opening.letters_public_offer'])),
            n('returned_entry_professional', 'Narrator', '''The papers arrive through the appointed channel. Areelu adds no invitation to her rooms and no request to reconsider your decision. You answer the research notice in writing, and the personal meeting does not take place.''',
              c('[File the exchange.]', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open'])),
            n('returned_entry', 'Areelu', '''A notice arrives about the next piece of unfinished work. The personal terms you last chose still stand.''',
              c('[Attend the meeting.]', next='returned_entry_active', forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused', 'areelu.trickster_opening.rivalry_only']),
              c('[Keep this contact professional.]', next='returned_entry_professional', requires=['areelu.trickster_opening.relationship_ended']),
              c('[Remain apart while the work proceeds.]', next='returned_entry_professional', requires=['areelu.trickster_opening.relationship_paused'], forbids=['areelu.trickster_opening.relationship_ended']),
              c('[Use only the research channel.]', next='returned_entry_professional', requires=['areelu.trickster_opening.rivalry_only'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused'])),
            n("returned_materials", "Commander", '''You ask Areelu to list only what each letter actually requested. The family asking for copies receives the copies without a condition. The damaged ward receives the sum needed for a repair, with no image, speech, or acknowledgment attached. The person refusing contact receives no letter from Areelu. The archivist keeps a private note that an offer can be reconsidered only if the writer asks.

Areelu reads the draft response and crosses out the sentence that says the payment is an act of remorse. She replaces it with the source of the funds and the account number from which they came. She does not thank you for catching the difference. She sees it herself and leaves the correction visible.

"I wanted the words to mean more than the action," she says. "That would have made me feel better about both."''',
              c('[Tell her the correction matters, but it repairs no part of the original decision.]', "returned_response", flags=f("letters_material_response")),
              c('[Ask her to keep the reply impersonal and let the recipients define what the act means.]', "returned_response", flags=f("letters_material_response", "meaning_left_open"))),
            n("returned_choice", "Commander", '''The archivist drafts a neutral letter to each family. It offers the complete file, the opportunity to request material support, and a private route to speak with Areelu if they choose. The language makes clear that refusing contact will not change the offer or cause the record to disappear.

Areelu stares at the word choose. "I dislike asking people to make another decision because of what I did." She takes up the pen. "But deciding for them that they do not want to hear from me would be the same arrogance in a more flattering coat." She signs the letters, then gives them back to the archivist unopened.

Her restraint is not acceptance of the replies. It is a decision to let the replies belong to the people who send them.''',
              c('[Tell her that the open offer is right only if she accepts a refusal without following up.]', "returned_response", flags=f("letters_recipient_response")),
              c('[Ask her to put a fixed end date on the offer so it cannot become a permanent demand for attention.]', "returned_response", flags=f("letters_recipient_response", "offer_time_limited"))),
            n("returned_confrontation", "Areelu", '''Areelu looks at the public draft. "You think I want to hide behind privacy." She does not sound offended; she sounds certain, and the certainty itself is familiar. "Perhaps I do. But publishing names without permission would turn their losses into a demonstration of my honesty. I would be choosing their exposure because I want my correction to be seen." She closes the draft.

"I will publish the corrected total and the sources of error. The families' names remain with the archivist unless they authorize release." She turns toward you. "You may tell me that I am retreating. I will not use that accusation to justify something they did not ask for."''',
              c('[Accept the boundary. Correct the public record without exposing the families.]', "returned_response", flags=f("letters_public_correction")),
              c('[Tell her to consult the affected writers first. You will not decide for them either.]', "returned_response", flags=f("letters_public_correction", "recipients_consulted"))),
            n("returned_response", "Areelu", '''The archivist sends the replies without commentary. Two families accept the files. One accepts the repair funding but refuses to meet. The person who requested no contact does not answer. No one thanks Areelu. One writer says the material is useful and the apology is not wanted. Another asks that the record name the decision she made, without calling it a sacrifice.

Areelu reads the words twice. "I wanted an answer that would tell me what to do next. These answers tell me only what they chose to tell me." She places the letter asking for no apology on top of the stack. "It is difficult to be told that my remorse is not needed. I had mistaken the chance to show it for something I was owed."

You do not comfort her by saying the families will understand. You do not know that. She does not ask you to say it. She files each reply beside the corresponding order and leaves the unanswered letter unanswered.''',
              c('[Ask whether she can accept that the repair may be the only relationship she has with those families.]', "returned_ledger", flags=f("letters_no_reward")),
              c('[Tell her that you will not turn private remorse into a substitute for restitution.]', "returned_ledger", flags=f("letters_no_reward", "restitution_boundary")),
              c('[Pause the personal conversation. You need time before being close to her again.]', "returned_pause", flags=f("letters_no_reward", "relationship_paused"))),
            n("returned_ledger", "Commander", '''You ask her to read the public correction beside the original order. Not as a punishment and not as a private exercise in shame: the original page stays visible because every later description should be checked against what she knew when she signed it.

The first version says, "The caravan was redirected to preserve the ritual schedule." The corrected version says, "I redirected the caravan after being warned that the alternate road would leave the ward weaker. I chose the ritual schedule over the time needed to protect the settlement. I did not know how many residents would die. I knew the order placed them at risk." She studies the phrasing. "It is less elegant," she says. "It is harder to misunderstand."

You ask whether she wants to add remorse. She says remorse is true, but the correction is not a letter to herself. She can tell the families she is sorry if they ask. She will not put the word where it might imply that they are expected to receive it.

The archivist asks Areelu to initial each alteration. She signs beside the original record, not over it. The paper now shows the order, the correction, and the time at which she accepted the record should be changed. It does not make the changed account the only account.''',
              c('[Keep both versions together in the archive, with the correction dated and attributed.]', "returned_archivist_conference", flags=f("public_record_corrected")),
              c('[Ask the archivist to distribute the correction only to the families who requested it.]', "returned_archivist_conference", flags=f("public_record_corrected", "distribution_limited"))),
            n("returned_archivist_conference", "Commander", '''The archivist reads the correction back, then places a second letter beside it. The writer has reviewed the public wording and says it accurately describes the order. They want the warning included as a separate document, not folded into Areelu's account as an explanation. They also ask that the report state that they refused a meeting and that the refusal changed nothing about their access to the record.

Areelu starts to ask whether the writer believes she understood the risk. The archivist stops her. The writer did not invite a conversation about Areelu's understanding. They asked the record to carry a clear boundary. Areelu closes her mouth and looks down at the request.

You ask her what she thinks the boundary is protecting. "Their right to have the account without having to manage my reaction to it," she says. She sounds irritated, but not at the writer. "I keep trying to turn a document into a conversation I can steer." She hands the letter to the archivist. "Put it in the public file exactly as written. I will not send a response."''',
              c('[Let the refusal stand without a reply and add the request to the record.]', "returned_counsel", flags=f("family_boundary_published")),
              c('[Ask the archivist to confirm the writer approved public inclusion before releasing their letter.]', "returned_counsel", flags=f("family_boundary_published", "publication_confirmed"))),
            n("returned_counsel", "Areelu", '''The runner waits until the archivist seals the family letter before speaking. Areelu says she wants to write another message, one sentence only: that she understands the warning was ignored and will not contact the family again unless they ask. The archivist says the family has already made the boundary clear. A second message, however brief, is still contact.

Areelu argues that the sentence would confirm she heard them. The archivist replies that the correction is public, the record is available, and the family asked not to meet. They can see what she chose to write. They did not ask her to tell them that she saw it. Areelu turns to you, perhaps expecting a way to make both wishes fit without changing either.

You tell her that the desire to be seen acknowledging the boundary is still a desire for their attention. It may be understandable. It does not override what they chose. She can let the unreturned message exist as something she wanted and did not send.

She puts the draft away. "I wanted to be the person who did not repeat the intrusion," she says. "I wanted the family to know it. That is not the same thing as respecting the refusal." The distinction irritates her, and she leaves the irritation visible rather than turning it into an argument. She asks the archivist to retain the draft in the private file, marked unsent. It will not become part of the family's correspondence.''',
              c('[Let the unsent draft remain private and continue with the archive review.]', "returned_intimacy", flags=f("unsent_contact_respected")),
              c('[Ask her to destroy the draft so that it cannot become a future justification for contact.]', "returned_intimacy", flags=f("unsent_contact_destroyed"))),
            n('returned_intimacy', 'Areelu', '''"I can accept it as a fact," she says. "I cannot promise that I will feel no resentment toward the silence. That resentment is mine to carry. It does not give me leave to break the boundary." She considers the top letter. "You could have called this growth and made it sound finished. I would have preferred the praise. I am glad you did not offer it."

The observation is close to a compliment, but she does not make it a payment. She asks whether you want to walk back together. She stops at the door and waits for your answer.''',
              c('[Keep walking together, without promising that the old closeness has returned.]', next='returned_reflection', flags=['areelu.trickster_opening.walked_together']),
              c('[Ask her to walk alone. You will meet after the next record arrives.]', next='returned_nonromantic', flags=['areelu.trickster_opening.walked_alone'])),
            n('returned_reflection', 'Commander', '''The walk follows the old city's upper wall, where the stones have been repaired in patches from different centuries. Areelu does not try to turn the silence into a second hearing. She asks what you think of the archivist's changes, then waits while you decide whether to answer.

You tell her that a public correction is useful because it lets another reader see what changed and who accepted the change. You do not tell her that this makes the original account acceptable. She says she understands the distinction. You point out that understanding a distinction in a conversation is easier than keeping it when the next criticism arrives. She admits that she may be tempted to close the file or to answer anger with a more precise argument than the person speaking can follow.

"Then I will ask the archivist to keep the public copy," she says. "If I try to alter it, the prior version remains available." She is making the rule for herself, not asking you to enforce it. The archivist will receive a duplicate and a dated instruction. If the next review finds that she ignored the condition, the report will say so.

She turns toward you. "I would like to keep walking beside you. I would also like to know whether you want that, or are staying because you think leaving now would look cruel."''',
              c('[Stay because you choose to. Tell her you may still ask for space again.]', next='returned_receipt', flags=['areelu.trickster_opening.walk_chosen']),
              c('[End the walk. You need solitude, and she can contact you after the next review.]', next='returned_nonromantic', flags=['areelu.trickster_opening.relationship_distance_requested'])),
            n('returned_receipt', 'Areelu', '''At the top of the wall, the archivist's runner catches up with a receipt for the funds sent to repair the water ward. There is no letter attached. The repair has been accepted; the family did not add a message.

Areelu turns the receipt over once. "I want to write that I am glad they accepted it," she says. "That would make the acceptance about my relief." She passes the receipt to the archivist to file. The silence remains the family's answer.

She looks at you. The public record has a correction; the families have the copies they requested; the repair has gone through. There is no shared embrace at the end of the process. "I want you to walk beside me," she says, "but I will not make this work a reason you must." You answer that the two choices remain separate. She nods, and the next step is not assumed.''',
              c('[Agree to continue the relationship and review the remaining work together.]', next='returned_after_walk', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open']),
              c('[Keep the personal relationship paused while the archive work continues.]', next='returned_nonromantic', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.relationship_paused', 'areelu.trickster_opening.second_question_open']),
              c('[Close the personal relationship after the archive has been corrected.]', next='returned_nonromantic', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.second_question_open'])),
            n('returned_after_walk', 'Commander', '''A week later, the archivist sends you both a copy of the sealed record. The correction is now indexed beside the original order. The family that refused contact has not replied. No new letter has arrived. Areelu keeps the copy in her office but does not add a private annotation to it.

When you visit, she is at the window with the file closed. She has not forgotten the family or stopped wanting an answer. She says the desire to know whether they have read the correction is still there. She has not asked the archivist to check. She is waiting because the answer is not hers to demand.

The next conversation turns toward your own relationship. You tell her that you can want her and still dislike how her attention narrows around a question she cannot answer. She says she does not want you to become an audience for her restraint. You answer that you are not praising her for each time she refrains from crossing a line. Restraint is the minimum that lets the other person remain free; it is not a gift you owe her for performing it.

Areelu lets the words sit between you. "I want to be desired even when I am being difficult," she says. "I do not want that desire to become a verdict that I am good." You tell her it is not. She asks if you still desire her. You say yes, but you will not make the answer a shield against what she did. The attraction survives the disagreement without solving it.''',
              c('[Keep the relationship open and agree to revisit the archive after the next scheduled review.]', next='returned_aftercare', flags=['areelu.trickster_opening.desire_after_disagreement']),
              c('[Tell her you want her, but remain paused while the family’s no-contact request is still difficult for her to bear.]', next='returned_nonromantic', flags=['areelu.trickster_opening.relationship_paused']),
              c('[End the romance. You do not want desire to become another way of managing her choices.]', next='returned_nonromantic', flags=['areelu.trickster_opening.relationship_ended'])),
            n('returned_aftercare', 'Areelu', '''Areelu writes the next archive review on the calendar, six days away. You ask whether she will keep the same public record available until then. She says she will, even if the family never responds and even if the archivist finds another correction. You ask what she will do if the review finds that the current version still minimizes what she chose.

She says she will amend the record and preserve each version. You ask what she will do if the archivist says no amendment is supported. She says she will leave the record in place and accept the refusal. She pauses before adding that she may continue to disagree privately. You tell her disagreement is allowed; covertly changing the file is not.

The conversation is not a promise of moral transformation. It is a concrete procedure that can be observed: the archive keeps dated versions, the archivist controls distribution, and Areelu gives up the ability to revise the past account in secret. You are not given access to the archive as proof of her trust. You are not asked to patrol it. The independent reader remains the one who checks the work.

Areelu asks what you want from her in the six days before the review. You tell her not to turn the interval into a test of your loyalty. If you meet, meet because both of you want to. If you need space, say so without making your absence a coded message. She admits she prefers a puzzle to a silence she cannot interpret. You tell her not every silence is written for her.''',
              c('[Agree to meet once before the review, on a day chosen by both of you.]', next='returned_future', flags=['areelu.trickster_opening.review_meeting_planned']),
              c('[Keep the interval quiet. Let the next contact come from the archivist’s scheduled review.]', next='returned_future', flags=['areelu.trickster_opening.review_meeting_deferred']),
              c('[End the romance. The archive can proceed without making the relationship its witness.]', next='returned_nonromantic', flags=['areelu.trickster_opening.relationship_ended'])),
            n('returned_future', 'Commander', '''Six days later, the archive sends its scheduled notice. The public correction remains unchanged; the archivist has confirmed the sources and has not found evidence to alter the account. That result does not mean the families accept it. The family that asked for no contact has not written again.

Areelu reads the notice, folds it once, and puts it in the archive file. She does not ask whether you think this counts as success. You tell her it counts as completion of the review, not as a verdict on the people who remain silent. She accepts that distinction without asking you to improve the phrasing.

She asks if you want to come to dinner. It is not a reward for the record, and she does not say that you have proved your patience. You ask what she wants. She says she wants your attention, your desire, and the chance to argue about something that is not a dead person or a failed experiment. She leaves the invitation unanswered between you.''',
              c('[Go to dinner. Keep the relationship alive without claiming that the archive is closed forever.]', next='returned_final_meeting', flags=['areelu.trickster_opening.dinner_chosen']),
              c('[Decline tonight and let the scheduled record review stand as the end of this arc.]', next='returned_declined_dinner', flags=['areelu.trickster_opening.dinner_declined'])),
            n('returned_final_meeting', 'Areelu', '''At dinner, you ask Areelu why she wants your company after a day spent reviewing records. She says she wants to be desired by someone who can see the parts of her that she would prefer to hide. She admits the desire is selfish. She does not ask you to call it healthy.

You tell her that attraction is not a medal you give her for doing the minimum. It is something you feel in spite of what she has done, and sometimes in conflict with it. She says that sounds less comforting than she had hoped. You answer that comfort is not the condition you offered when you first agreed to meet.

She talks about the future she used to imagine for the dead child, then stops herself. She tells you that she had plans she cannot transfer onto you: a name, a home, the shape of an ordinary life that she believed she could restore. You are not the continuation of that imagined future. Your desire for her can be adult and real without becoming a replacement for the person she lost.

She says that hearing the distinction hurts. You say it is not a rejection of her grief, but you will not live inside the role grief invented. Areelu accepts the correction without agreeing that every echo of the graft is irrelevant. The question remains unresolved, as it should. She can wonder what the remnants changed without treating that uncertainty as a claim on your identity.

The evening has no dramatic reconciliation. You eat, disagree about whether the archivist's phrasing was too cautious, and let the conversation wander toward music and the city. When Areelu asks to kiss you, she waits through the pause. She waits for your answer.''',
              c('[Kiss her and agree to the next ordinary evening together.]', next='returned_after_review', flags=['areelu.trickster_opening.desire_after_disagreement']),
              c('[End the evening without touching. Keep the relationship open and the boundary intact.]', next='returned_no_touch', flags=['areelu.trickster_opening.touch_deferred']),
              c('[Tell her you want no further personal meetings.]', next='returned_nonromantic', flags=['areelu.trickster_opening.relationship_ended'])),
            n('returned_no_touch', 'Areelu', '''You finish the evening without touching.
Areelu sets her cup down and accompanies you as far as the door.
"I will write when the next notice arrives."
You agree. She lets you leave without turning the answer into another invitation.''',
              c('[Go to your own rooms.]', next='returned_close', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.touch_deferred'])),
            n('returned_after_review', 'Areelu', '''When the dinner ends, Areelu does not ask you to come back to her rooms. She asks whether you want to see her next week, then adds that she can accept a no without needing you to make it sound kind. You ask whether she wants the answer now. She says yes, but not if you are answering only to keep her calm.

You tell her that you want to see her again. The desire is real, and so is the limit: you will not become the person who checks whether she has written to the family that asked for no contact. That remains a duty she owes them and a boundary the archivist helps preserve. Your relationship can include conversations about her choices, but it cannot make you the mechanism that stops her from making them.

She says that she has sometimes imagined you as a witness whose presence would make her better. She says the fantasy is comforting and false. You are not a restraint she gets to wear when she fears what she might do. If she wants to act differently, the choice must remain hers even if you are not there to see it.

You answer that she can want you and still have to govern herself. She replies that she wants your body, your attention, and the sharpness with which you refuse to let her turn intimacy into a pardon. She does not describe that as a virtue. She says it is what she wants. You tell her that desire makes the relationship possible, not invulnerable.

Areelu asks if she may touch your face. You say yes. Her hand is warm; the contact is not an apology. When she lowers it, she asks if you want to walk out together or leave separately. You choose the exit you want, and neither answer changes the terms already spoken.''',
              c('[Walk out together and keep the relationship open to future disagreement.]', next='returned_long_term', flags=['areelu.trickster_opening.second_question_open']),
              c('[Leave separately and meet after the next scheduled archive review.]', next='returned_long_term', flags=['areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.relationship_distance_requested'])),
            n('returned_long_term', 'Areelu', '''A week later, the family that asked for no contact sends the archivist a final note. They have received the copies and the repair funds. They do not want further correspondence. They ask that the archive keep the record available for future historians but that the family not be mentioned in public summaries beyond the names already recovered.

Areelu reads the note and puts it in the file. She does not ask to reply. She tells you that she still wishes the family would say something that made the silence less absolute. She also says she understands that the wish is not theirs to meet. The note closes one form of contact. It does not say what the family thinks of her, and she may never know.

You ask if she can leave the unknown alone without turning it into another question for you to answer. She says she can try. You remind her that the work of leaving it alone is hers, not a proof she needs to perform for your approval. She says she knows, then admits that being seen trying still matters to her. You tell her that you see it without making the family responsible for the fact.

Areelu looks at you for a long moment. "I still want you," she says. "I want to be touched. I want to hear you argue with me and stay long enough to tell me when I am making an excuse." She does not dress the desire as repentance. She asks whether you want to spend the evening with her. If you say yes, she will ask before touching. If you say no, she will not interpret the refusal as a judgment on the family's letter or a rejection of every earlier moment.

You make the choice for tonight. The archive remains closed to personal interpretation, the relationship remains open to change, and neither silence becomes a hidden invitation.''',
              c('[Say yes and spend an ordinary evening together.]', next='returned_close', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.ordinary_evening_chosen']),
              c('[Decline tonight and ask to meet after the next public review.]', next='returned_close', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.relationship_distance_requested'])),
            n("returned_pause", "Areelu", '''Areelu inclines her head. "Then take the time. I will not treat your need for distance as an attempt to punish me." She gathers the letters. "I have other work to do before the archivist writes again. You need not attend to prove that you care."''',
              c('[Pause the romance and leave contact open for the next public record.]', "returned_close", flags=f("returned_arc_complete", "relationship_paused", "second_question_open")),
              c('[End personal contact. Do not ask her to wait for you.]', flags=f("closed", "returned_arc_complete"), abort=True)),
            n('returned_nonromantic', 'Narrator', '''The archivist handles the remaining correction and repair receipt through the official channel. Areelu sends no personal invitation with the papers. You file the exchange and return to your own work.''',
              c('[File the notice.]', next='returned_close', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open'])),
            n('returned_declined_dinner', 'Areelu', '''You decline the invitation.
"Another time, perhaps," Areelu says, and gathers the papers instead of setting the table.
You leave before dinner. No kiss follows you to the door.
The next communication will concern the scheduled review; tonight belongs to you.''',
              c('[Leave.]', next='returned_close', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open'])),
            n('returned_close', 'Commander', '''The names leave the archive as copies and corrections, not as a story about Areelu becoming worthy of forgiveness. The replies stay with their writers. The next question comes from a different direction: whether the surviving work can be examined without repeating the conditions that made people expendable in the first place.''',
              c('[Agree to review the remaining work with the archivist present.]', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open']),
              c('[Let Areelu continue the review without you, then decide whether to return.]', flags=['areelu.trickster_opening.returned_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.commander_review_absent'])),
        ],
        requires=("areelu.trickster_opening.record_arc_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=168,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_private_copy",
        "The line on the page",
        "Areelu",
        5,
        "copy_entry",
        [
            n('copy_entry_active', 'Commander', '''A fresh page lies on Areelu's desk, face down. The red ink has marked the blotting paper beneath it: the old question about the crib.
"You have seen enough to ask," she says. "So ask."
She does not cover the impression.''',
              c('[Ask why she repeated a test you limited to one attempt.]', next='copy_contested_entry', requires=['areelu.trickster_opening.memory_contested']),
              c('[Remind her that you protected the original answer from experimentation.]', next='copy_protected_entry', forbids=['areelu.trickster_opening.memory_contested'])),
            n('copy_entry_professional', 'Narrator', '''The papers arrive through the appointed channel. Areelu adds no invitation to her rooms and no request to reconsider your decision. You answer the research notice in writing, and the personal meeting does not take place.''',
              c('[File the exchange.]', flags=['areelu.trickster_opening.copy_arc_complete', 'areelu.trickster_opening.second_question_open'])),
            n('copy_entry', 'Commander', '''A notice arrives about the next piece of unfinished work. The personal terms you last chose still stand.''',
              c('[Attend the meeting.]', next='copy_entry_active', forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused', 'areelu.trickster_opening.rivalry_only']),
              c('[Keep this contact professional.]', next='copy_entry_professional', requires=['areelu.trickster_opening.relationship_ended']),
              c('[Remain apart while the work proceeds.]', next='copy_entry_professional', requires=['areelu.trickster_opening.relationship_paused'], forbids=['areelu.trickster_opening.relationship_ended']),
              c('[Use only the research channel.]', next='copy_entry_professional', requires=['areelu.trickster_opening.rivalry_only'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused'])),
            n('copy_contested_entry', 'Commander', '''The missing page is a new copy of the old exchange. Areelu has removed the copied exchange from the ruined laboratory from the archive table, but a red mark remains in the paper beneath it. You see the impression before she covers it. The line reads: "What did you feel by the crib?" The words are from the old prompt. The copy itself is new.

You ask whether she has reconstructed the memory again. Areelu does not answer at once. Her gaze drops to the red ink. "I copied the prompt and your response onto a clean page. I wanted to see whether the contradiction you made would still hold without the diagram beside it." She pauses. "I did not alter the past. I did not reach into your mind. I should have asked before recreating the question in front of you."

The distinction matters, but it does not make the choice harmless. You had agreed to one copy-only test under conditions either of you could stop. You had not agreed to repeated private use of the answer. She has not changed the record or the graft; she has crossed a boundary around your participation and assumed that technical safety made further consent unnecessary.

"I wanted to know whether I could trust the method," she says. "I did not ask whether you wanted to be part of another test. That was my decision, not an accident." Her expression hardens as she waits. You can hear the old defense forming: the copy is inert, the original answer untouched, no actual harm done. She has not spoken it yet. She is watching to see whether you will ask her to.''',
              c('[Tell her that no alteration is not the same as consent. Ask her to account for why she repeated the test.]', next='copy_confront', flags=['areelu.trickster_opening.copy_boundary_named']),
              c('[Ask to inspect the copy and verify that neither the original record nor your mind was altered.]', next='copy_inspect', flags=['areelu.trickster_opening.copy_investigation_requested']),
              c('[Leave now. You will not decide whether the breach matters while standing inside it.]', next='copy_pause', flags=['areelu.trickster_opening.copy_contact_paused'])),
            n('copy_protected_entry', 'Areelu', '''"You refused the experiment," Areelu says. "I remember."
She turns the page over. It holds a transcript, without a magical annotation or the impossible footnote you declined to create.
"I thought I might examine the question without asking it again. Apparently I was not content to leave your answer where you put it."
Your recollection is intact. Nothing in the room has weakened it.
What troubles you is the fresh space she has left beneath the transcript, ready for another answer.
"The memory was never yours to spend," you say.
"No. The question was mine. I have been behaving as though that gave me the rest."
She does not destroy the page while you watch. She waits for you to say what you want done with it.''',
              c('[Ask her to account for reopening the question.]', next='copy_confront', flags=['areelu.trickster_opening.copy_boundary_named']),
              c('[Inspect the inert transcript.]', next='copy_inspect', flags=['areelu.trickster_opening.copy_investigation_requested']),
              c('[Leave the meeting.]', next='copy_pause', flags=['areelu.trickster_opening.copy_contact_paused'])),
            n('copy_inspect', 'Commander', '''Areelu lets you examine the page. The paper carries no spell residue, no divination mark, and no sign of an effect aimed at your mind. The past remains as it was. The copy is a copy: ink, pressure, and the question she wanted to ask again.

The check answers what happened to the artifact and what did not happen to you. It cannot answer why she treated an available record as an invitation to reopen a personal question. You have given no permission for this new use.

Areelu watches you finish. "You have confirmed the narrowest fact," she says. "Do not let me use that to answer the larger one."''',
              c('[Put the copy down and confront the choice she made.]', next='copy_confront', flags=['areelu.trickster_opening.copy_boundary_verified']),
              c('[End the meeting. The technical finding changes nothing about your need for distance.]', next='copy_pause', flags=['areelu.trickster_opening.copy_boundary_verified', 'areelu.trickster_opening.copy_contact_paused'])),
            n('copy_confront', 'Commander', '''"The paper is inert. My answer is not yours to put to work whenever it interests you. I told you the limits before today. You cannot reopen the question simply because you dislike where I left it."''',
              c('[Ask her to state what she did without explaining it away.]', next='copy_response', flags=['areelu.trickster_opening.copy_confrontation_direct']),
              c('[Tell her the next step is hers: she can accept the boundary or lose your trust.]', next='copy_response', flags=['areelu.trickster_opening.copy_confrontation_consequence']),
              c('[Say the relationship is over. You do not want to negotiate basic consent.]', flags=['areelu.trickster_opening.closed', 'areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.copy_contact_ended', 'areelu.trickster_opening.delivered.copy_entry'], abort=True)),
            n('copy_response', 'Areelu', '''The silence stretches. Areelu does not apologize immediately. She turns the page face down, then back again, as if the order might change the content.

"I repeated the prompt without asking whether you agreed to revisit it," she says. "I told myself the page could not hurt you because the original answer was untouched. That was not the condition you gave me. I wanted the argument reopened, and I used your answer because it was available." She stops there. Her face remains controlled, but her fingers have pressed a crease into the paper.

"That is not a defense. It is the decision." She does not ask if that is enough. "I will destroy the copy. I will not ask you to forgive me because the original record is safe. I will not make another copy without your separate permission. You can require no more use of that answer, or no further personal contact. I will follow either boundary."''',
              c('[Require her to destroy the copy and never reuse your answer. Continue only if this becomes a permanent rule.]', next='copy_repair_terms', flags=['areelu.trickster_opening.copy_answer_barred']),
              c('[Require her to send the copy and the full record of the unauthorized reuse to the archivist.]', next='copy_repair_terms', flags=['areelu.trickster_opening.copy_archive_disclosure']),
              c('[End the relationship but leave the research channel open.]', next='copy_end', flags=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.copy_contact_ended'])),
            n('copy_repair_terms', 'Commander', '''You ask her to repeat the boundary in her own words. Areelu does not look away from the envelope.

"I will not use your answer again, in a private copy or in a public argument, unless you separately give permission. The fact that the answer exists in past does not make every later use consented. I will not treat access to the record as access to you." She pauses. "That is the rule you asked for. I can follow it. I do not ask you to believe I have followed it until you have time to see what I do."

You tell her that this is not a ritual where the right sentence earns absolution. If she uses the answer again, the breach will happen again. If she keeps the boundary, the past breach will remain part of the relationship. No future good choice erases it.

"I understand," she says. Then, after another pause: "I am angry that you are right to ask for proof. That anger does not change the rule." She places the pen beside the envelope, making no attempt to sign over your objection.''',
              c('[Let her document the rule and proceed with the remedy you chose.]', next='copy_archive_log', flags=['areelu.trickster_opening.copy_rule_restated']),
              c('[Keep the meeting paused. You need to see her accept the boundary without an immediate repair.]', next='copy_pause', flags=['areelu.trickster_opening.copy_rule_restated', 'areelu.trickster_opening.copy_contact_paused'])),
            n('copy_archive_log', 'Areelu', '''Areelu dictates a short account for the archive while the observer writes. She states that she created a fresh copy of the original question and response without obtaining separate permission. She states that the past was not modified and that she has no evidence of a magical effect on the Commander. She also states that those technical facts do not establish consent.

The observer asks whether the report should say that the Commander had previously permitted a test. Areelu says yes, but distinguishes that permission: it covered one test, with the stated cost and an explicit chance to stop. It did not grant indefinite use of the answer. You correct the observer once when the phrasing makes it sound as if your old consent made the second test reasonable. Areelu does not object to the correction.

You ask why she wanted to reopen the argument. She says the first test showed that her inference was not secure, but the truth that followed was harder to bear: she had built a life around a conclusion she could not prove. She wanted to test the method again because she preferred a question that stayed open to an answer she could not command. "I knew the difference," she says. "I chose the convenient version anyway." She does not ask you to feel sorry for her.

The archive entry will be available to the same reviewers who hold the public record. It will not be published as a scandal or hidden as a private misunderstanding. It records the boundary, the breach, and the remedy without declaring the relationship repaired.''',
              c('[Approve the factual account and leave the assessment of repair open.]', next='copy_archive_review', flags=['areelu.trickster_opening.copy_archive_accounted']),
              c('[Ask the observer to note that the relationship remains paused until you decide otherwise.]', next='copy_pause', flags=['areelu.trickster_opening.copy_archive_accounted', 'areelu.trickster_opening.relationship_paused'])),
            n('copy_archive_review', 'Commander', '''The observer reads the archive account aloud, including the sentence that the new copy was not consented to. Areelu says the record is accurate. You ask whether she wants the line softened because the phrase sounds harsher than her intention. She says no. Her intention was not the only relevant fact; the permission she assumed was the decision she made.

The archivist asks whether the Commander should be named in the account. You say yes, because you were the person whose answer she reused, but you want the context and your response included. You do not want the report to imply that the copy changed your memory or that you approved it by being present. The archivist writes the clarification exactly as you state it.

Areelu watches the exchange. She says she would rather the record name the violation without naming the person affected, because exposure is not necessary to establish what she did. You tell her that you decide what your name means in your account. She says, "Yes. That is yours." She does not attempt to choose for you.

The report leaves the archive with one more correction: Areelu does not control the record of her breach, and you do not have to disappear from it in order to protect her. You both know the document is not a replacement for the boundary itself. It makes the boundary legible to anyone who might later try to make the same mistake.''',
              c('[Approve the copy record with your own account included.]', next='copy_repair', flags=['areelu.trickster_opening.copy_account_included']),
              c('[Approve the breach record but omit your name. The decision to be identified is yours.]', next='copy_repair', flags=['areelu.trickster_opening.copy_account_omitted'])),
            n('copy_repair', 'Commander', '''Areelu tears the copy across the middle, then again through the question. She seals every piece in a paper envelope and writes what she destroyed and why on the front. If you chose external disclosure, she sends the sealed copy with an unedited account of how she reused the answer. If you chose a private prohibition, she locks the envelope with the original records and marks it not to be reopened.

You do not praise the act. She has stopped one repetition; she has not restored the boundary by acting correctly after crossing it. Trust is what happens after the next choice, and she knows you will see whether she follows the rule when the conversation becomes inconvenient.

"I can accept that you may not trust me," she says. "I cannot ask you to speed it up."''',
              c('[Continue the relationship, but pause intimate contact until the new boundary has held over time.]', next='copy_pause', flags=['areelu.trickster_opening.copy_breach_addressed', 'areelu.trickster_opening.relationship_paused']),
              c('[Continue with no new intimacy. You will decide later whether trust returns.]', next='copy_future', flags=['areelu.trickster_opening.copy_breach_addressed', 'areelu.trickster_opening.copy_closeness_withheld']),
              c('[End the romance. Keep the research channel under the archivist’s oversight.]', next='copy_end', flags=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.copy_breach_addressed'])),
            n("copy_future", "Areelu", '''Areelu puts the envelope in the archive's locked drawer and gives the key to the archivist. It is a practical safeguard; it does not make the archivist responsible for policing every conversation between you.

You ask whether she understands what it will mean if she wants the answer again later. She says she will have to ask you at that time, with no assumption that your previous consent carries forward. You ask what happens if you decline. "Then the question remains unanswered," she says. "I do not get to turn your no into an invitation to design another method." The answer is exact. You tell her that exactness is only useful if she remembers it when the answer disappoints her.

"I might fail at remembering," she says. "If I do, the consequences belong to me. I will not use my work, my grief, or the fact that I desire you as reasons you should remain." She does not take your hand. She does not ask you to promise you will remain anyway.

The archivist will review the copy log at the next scheduled record audit. You are not appointed to watch Areelu. The audit exists because the public record and the archive need a reliable chain of custody, not because a romance can supervise her into goodness.''',
              c('[Let the archivist hold the key and leave the next contact undecided.]', "copy_followup", flags=f("copy_audit_scheduled")),
              c('[Ask for a written audit date before agreeing to return.]', "copy_followup", flags=f("copy_audit_scheduled", "return_condition_named"))),
            n('copy_followup', 'Commander', '''The audit occurs a week later. It verifies that the envelope remains sealed, that no new copy was made, and that Areelu's report still matches the archive. The archivist asks whether you want to attend. Areelu has already stated that your attendance is optional; she does not know which answer you will choose.

You attend. The envelope is intact. The key remains with the archivist. The paper account includes the part where Areelu wanted another test and the part where she chose not to make one without permission. This does not prove the boundary will never be crossed again. It proves that, this time, she kept it when there was no immediate reward for doing so.

Areelu looks at you only after the archivist closes the file. "I am relieved," she says. "I also know relief is not evidence that I deserve your trust." You tell her that the audit answers a narrow question: whether the copy was preserved or used again. It does not decide the rest of your relationship. She says that is fair, though she still dislikes how many things remain undecided.''',
              c('[Keep working with her, but let trust return at its own pace.]', next='copy_followup_conversation', flags=['areelu.trickster_opening.copy_audit_passed']),
              c('[Remain apart. A passed audit does not change your decision to end the romance.]', next='copy_end', flags=['areelu.trickster_opening.copy_audit_passed', 'areelu.trickster_opening.relationship_ended'])),
            n('copy_followup_conversation', 'Areelu', '''The audit is finished, but Areelu does not treat it as a verdict on either of you. She asks whether you are willing to speak somewhere without the archivist. If you say no, the conversation can remain on the official channel. If you agree, she chooses a room with two doors and leaves the one behind you open.

She says the new copy happened because she wanted to ask whether the memory could be separated from the grief she had attached to it. She knew it was your answer. She wanted the answer because she wanted to understand you, and she let that desire become permission in her own mind. Her desire for you did not make the boundary less important; it made her more responsible for noticing when she was using access to the record as a substitute for asking you.

You ask whether she can want to know you without treating every unknown as an invitation to test. She says she does not know how to do that perfectly. She can promise to ask; she cannot promise never to feel the impulse to reach for a method instead. You tell her you do not expect perfection. You do expect the choice to stop once you say no, and a willingness to hear why without forcing you to make the refusal easier for her.

She reaches toward you, then withdraws the movement before touching. "May I hold your hand?" You may say yes or no. Either answer becomes the answer for this moment, not a prediction of the next.''',
              c('[Let her hold your hand. The boundary is still there, and so is desire.]', next='copy_closeness', flags=['areelu.trickster_opening.copy_conversation_resumed'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused']),
              c('[Keep your hands to yourself. Continue the conversation without touch.]', next='copy_closeness', flags=['areelu.trickster_opening.copy_conversation_no_touch'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused']),
              c('[End the personal meeting and let the research channel stay with the archivist.]', next='copy_end', flags=['areelu.trickster_opening.copy_conversation_ended', 'areelu.trickster_opening.relationship_ended'])),
            n('copy_closeness', 'Commander', '''Areelu does not confuse the audit's result with regained trust. You ask her to describe what she will do if she wants to reuse a record and you are not present. She says she will treat the answer as unavailable for new personal experiments unless you explicitly agree to that particular use. If the matter is necessary to the public research, she will ask the archivist whether the record can be used without involving you. She will not ask the archivist to obtain your private permission on her behalf.

You ask how she will tell the difference between a factual source and a private memory. She answers that the information can be identical while the relationship to it differs. The source may be public; the decision to invite you into another experiment remains yours. The first mistake was treating access as permission. The second would be pretending that a better procedure makes it impossible to repeat.

She asks whether you believe her. You say you believe she understands the rule in this room. Trust beyond it will require time. She does not protest that you should trust her because she gave you an accurate account. She says she wanted a faster answer and is trying not to demand one.

The affection is still there, although it has become less convenient to express. Areelu says she wants to be close to you and wants to be able to ask without making your response a referendum on whether she has changed. You tell her that she can ask. You can refuse. The answer is still the answer.''',
              c('[Agree to another meeting and let the next touch be asked for separately.]', next='copy_revisit', flags=['areelu.trickster_opening.copy_closeness_rebuilt']),
              c('[Stay in contact but hold intimacy until the next archive review confirms the rule has lasted.]', next='copy_pause', flags=['areelu.trickster_opening.copy_closeness_rebuilt', 'areelu.trickster_opening.relationship_paused'])),
            n('copy_revisit', 'Areelu', '''At the next meeting, the archivist reports that the sealed copy has not been reopened and no duplicate was made. The process is boring by design: a date, a signature, an intact envelope. Areelu listens to the report without trying to make it say more than it does.

You ask if she still wants the answer to the question she copied. She says yes. She wants to know whether the Commander felt sadness, anger, or something she has not named. She also knows that you have already answered once and that the answer does not belong to her as a continuing resource. She can want to know and choose not to ask again. The desire itself is not the violation; acting on it without your consent would be.

You tell her this distinction makes her want more difficult, not less. She says she would rather have difficult desire than a quiet agreement whose terms she invented. She wants your mouth, your attention, and the chance to be wanted without pretending that intimacy puts her beyond criticism. She waits for your response, not because she expects a particular one, but because that is what asking requires.''',
              c('[Tell her you want her and ask to kiss her, without reopening the memory question.]', next='copy_second_contact', flags=['areelu.trickster_opening.copy_desire_reaffirmed'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused']),
              c('[Keep the evening nonphysical. You are willing to continue, but not to resume intimacy yet.]', next='copy_nonphysical', flags=['areelu.trickster_opening.copy_intimacy_still_paused']),
              c('[Close the personal relationship. The unresolved memory question is too close to the breach.]', next='copy_end', flags=['areelu.trickster_opening.relationship_ended'])),
            n('copy_second_contact', 'Commander', '''You ask Areelu to imagine the next time she learns something private about you: not a quotation from a conversation, but a fact that changes how she understands what you want. You ask whether she can keep the fact without immediately testing it, interpreting it, or building a theory around it.

She says that she cannot promise not to interpret. Her mind does that before she chooses it. What she can promise is to ask before she acts on an interpretation, and to let you tell her that she is wrong without demanding that you prove the correction. She says the answer must remain yours even if she believes she has recognized a pattern.

You ask whether that will be different with your desire for her. Areelu says she wants to believe that your attraction means she has a place in your life. She also knows that desire can change. If it does, she will not call the earlier yes a contract that binds the later no. You say you will hold her to that when it becomes painful, not only when it is easy to say.

Areelu leaves her hand on her side of the table. She says she wants to kiss you and wants you to answer freely. You tell her that the memory question remains closed tonight. She agrees. This time she leaves the copy in the archive without asking to bring the answer into the room. The silence around it is not a cure. It is a boundary both of you can feel.''',
              c('[Kiss her, then stop wherever either of you wants to stop.]', next='copy_second_review', flags=['areelu.trickster_opening.copy_second_contact_chosen'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused']),
              c('[Hold her hand and keep the evening quiet.]', next='copy_second_review', flags=['areelu.trickster_opening.copy_second_contact_chosen', 'areelu.trickster_opening.intimacy_deferred'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused']),
              c('[Leave. The boundary is understood, but you are not ready to be close.]', next='copy_nonphysical', flags=['areelu.trickster_opening.copy_second_contact_declined'])),
            n('copy_nonphysical', 'Areelu', '''You leave your hands at your sides.
"I am willing to keep speaking. That is all I am offering tonight."
Areelu closes the folder.
"Then we will speak another time. I have no interest in extracting an evening from you one concession at a time."
She remains in the room while you leave. The envelope stays sealed, and the next report will come through the archivist.''',
              c('[End the meeting without physical contact.]', next='copy_close', flags=['areelu.trickster_opening.copy_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.copy_intimacy_still_paused'])),
            n('copy_second_review', 'Areelu', '''A week later, the archivist checks the envelope and the public account again. Nothing has been reopened. The procedure is not proof that Areelu will never cross a boundary; it is evidence that she kept this one through a period when she still wanted the answer. The archivist adds the date and closes the file.

Areelu reads the entry. "I wanted the process to tell me that I had changed," she says. "It tells me only what I did during the process." You tell her that this is the right scope. She nods. The answer disappoints her, but she does not try to enlarge it.

She asks whether you want the relationship to continue. If you do, it remains one you will keep choosing, with room for disagreement and for future correction. If you do not, the audit does not become a debt. Areelu waits for your answer without moving closer.''',
              c('[Continue, keeping the copy boundary and the audit in the shared history.]', next='copy_audit_future', flags=['areelu.trickster_opening.copy_arc_complete', 'areelu.trickster_opening.second_question_open']),
              c('[End the romance, but leave the completed record with the archivist.]', next='copy_end', flags=['areelu.trickster_opening.copy_arc_complete', 'areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.second_question_open'])),
            n('copy_audit_future', 'Commander', '''The audit closes the formal question. It cannot close the private one: whether Areelu will reach for a test when a question matters to her more than your comfort. She says she wants to believe that asking will become habit, but she does not promise that habit will come without effort.

You say you will not accept an arrangement where she gets to decide when the topic is safe because the page is only a copy. She agrees that the decision to involve you remains yours. If she wants to use public records for independent work, she can do so through the archivist. If she wants your experience or your interpretation, she asks you directly and leaves the answer with you.

She admits that the boundary feels unfair when she is curious. You ask whether she expects you to help her tolerate that feeling. She says no. You can offer closeness, but you are not required to soothe her whenever a limit frustrates her. She has to find other ways to live with uncertainty: work that does not involve you, the archivist's review, or simply leaving the question unanswered.

You tell her that you still desire her. The admission does not restore the lost ease. She says she wants you too, and she will not interpret your yes tonight as permission next week. You both know desire can outlast anger and also coexist with it. Neither one cancels the other.''',
              c('[Keep meeting, and let future touch be asked for separately.]', next='copy_long_term', flags=['areelu.trickster_opening.desire_after_breach']),
              c('[Keep the romance ended. Let the archive remain the only shared work.]', next='copy_end', flags=['areelu.trickster_opening.relationship_ended'])),
            n("copy_long_term", "Areelu", '''At a later meeting, Areelu tells you that the question about the crib has returned to her. The archive has not been reopened. She has not made a private copy. She did not contact you the moment the question came back; she waited until you had both agreed to meet and then asked whether you wanted to hear it.

You ask why it matters to her now. She says that in the beginning she wanted the answer to resolve who you were. After she accepted the life you had before her interference, she wanted it to establish what the graft had done. Now she sees that even a truthful answer might not distinguish your own feeling from the echo of the remnants, her leading question, or her grief. She still wants to know. The desire has not become wise merely because it has survived an audit.

You tell her the memory is not available for another test. She says she understands, and asks if that means you do not want to talk about it at all. You say you can discuss your own experience when you choose. She cannot turn that into a new experiment, and she cannot use your willingness to speak as permission to recreate the prompt.

She says she wants to know you in ways that do not require a laboratory. She wants to learn what makes you laugh when you are tired, what you hate being called, whether you like her hands on your back, and when you want her to stop. The questions are intimate because they are current and answerable. You tell her which ones you want to answer tonight. She listens and asks before touching you.''',
              c('[Share what you choose and let her kiss you if you both still want it.]', "copy_close", flags=f("copy_arc_complete", "second_question_open", "present_desire_chosen")),
              c('[Keep the topic for another day. Continue the relationship without making disclosure a test.]', "copy_close", flags=f("copy_arc_complete", "second_question_open", "disclosure_deferred"))),
            n("copy_pause", "Areelu", '''Areelu does not follow you when you leave. The page stays on the table until the archivist arrives to collect the materials. You receive no message asking you to return.

You leave the building without waiting to see what she does with the page.''',
              c('[Leave the next report to the archivist.]', "copy_pause_notice", flags=f("copy_notice_awaited"))),
            n("copy_pause_notice", "Areelu", '''Three days after your departure, a note arrives through the official channel.
"I destroyed the copy. The answer and the boundary remain yours."
There is no request attached.
The archivist has countersigned the account of what was destroyed. Areelu has added nothing below it.''',
              c('[Return to the research, with the archivist present and personal contact paused.]', "copy_close", flags=f("copy_breach_addressed", "relationship_paused")),
              c('[End personal contact. She can continue the research without you.]', "copy_end", flags=f("relationship_ended", "copy_breach_addressed"))),
            n("copy_end", "Areelu", '''Areelu accepts the ending without trying to convert it into a test. She does not say that you are punishing her, or that the method is harmless. She destroys the copy and records why. The research can continue under the archivist's care, but you will not be the person expected to keep her honest.

"You were right to draw the line," she says. "That does not entitle me to your company afterward."''',
              c('[Close the personal relationship and continue only with the public record.]', flags=f("copy_arc_complete", "second_question_open")),
              c('[Close the contact entirely.]', flags=f("closed", "copy_arc_complete"), abort=True)),
            n('copy_close', 'Commander', '''The page is gone. The copy has not changed the original answer, and the original answer does not excuse what happened. Areelu has a clearer boundary now because you had to defend it. That cost belongs in the relationship's history; neither of you gets to erase it by moving on quickly.''',
              c('[Keep the agreed channel and the completed record.]', flags=['areelu.trickster_opening.copy_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.delivered.copy_entry']),
              c('[Stop the personal relationship here, even though she accepted the boundary.]', flags=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.copy_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.delivered.copy_entry'])),
        ],
        requires=("areelu.trickster_opening.returned_arc_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=120,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_residual_gate",
        "A limit chosen in public",
        "Areelu",
        5,
        "gate_entry",
        [
            n('gate_entry_active', 'Areelu', '''The archivist finds a sealed survey from the old ward network. One line in it describes a residual gate beneath a ruined watch post, still keyed to the same sequence Areelu used before the Worldwound opened fully. The site is not an active Worldwound and the survey does not prove that the gate will breach. It does say that two families now live within the outer boundary, and that the old instrument continues to read a pressure it cannot explain.

Areelu asks the archivist to send the families a warning and let them decide whether to leave before the inspection. She does not plan to go alone. The panel appoints an independent observer; the families choose one representative to attend. You are invited because the seam's behavior may call for the Trickster's contradiction, but no one asks you to use it.

At the site, the gate is a narrow red seam in a stone arch, no wider than the fold you stabilized together. The instrument makes one reading from the past and one from the present. The error between them is stable, but the old mechanism treats the difference as a command to open further.

Areelu stands outside the chalk boundary. "This was built from the logic I trusted then. I want to close it. I also want to know why it still obeys that logic." She looks toward the observer, then the families' representative. "They have the right to stop the inspection. You do not have to help just because you can. If we proceed, the residents will be outside the marked radius, and we will record every choice before making it."''',
              c('[Ask the residents’ representative whether they want the inspection to continue, then accept the answer.]', next='gate_permission', flags=['areelu.trickster_opening.gate_residents_consulted']),
              c('[Knowledge: Arcana, DC 37] The two readings can be separated by grounding the outer ring, but the instrument will be destroyed.', check={'Skill': 'SkillKnowledgeArcana', 'DC': 37, 'Success': 'gate_arcana_success', 'Failure': 'gate_arcana_failure', 'CommanderOnly': True}),
              c('[Trickster: Make the old command cite its own continuation as proof that it has already ended. The contradiction may close the gate, but could consume Areelu’s working archive as its anchor.]', next='gate_trickster_offer', flags=['areelu.trickster_opening.gate_trickster_proposed'], requires=['areelu.trickster_opening.active_trickster_path', 'areelu.trickster_opening.entry_ready']),
              c('[End the inspection. Evacuate the nearby families and let the archivist decide whether to seal the whole site.]', next='gate_withdraw', flags=['areelu.trickster_opening.gate_inspection_withdrawn'])),
            n('gate_entry_professional', 'Narrator', '''The papers arrive through the appointed channel. Areelu adds no invitation to her rooms and no request to reconsider your decision. You answer the research notice in writing, and the personal meeting does not take place.''',
              c('[File the exchange.]', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open'])),
            n('gate_entry', 'Areelu', '''A notice arrives about the next piece of unfinished work. The personal terms you last chose still stand.''',
              c('[Attend the meeting.]', next='gate_entry_active', forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused', 'areelu.trickster_opening.rivalry_only']),
              c('[Keep this contact professional.]', next='gate_entry_professional', requires=['areelu.trickster_opening.relationship_ended']),
              c('[Remain apart while the work proceeds.]', next='gate_entry_professional', requires=['areelu.trickster_opening.relationship_paused'], forbids=['areelu.trickster_opening.relationship_ended']),
              c('[Use only the research channel.]', next='gate_entry_professional', requires=['areelu.trickster_opening.rivalry_only'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused'])),
            n("gate_permission", "Areelu", '''The representative asks what the inspection can change for the people living nearby. Areelu explains that closing the gate will reduce the risk of a further pressure surge, but that the current readings do not prove the arch is about to open. The instrument may be lost. The site may remain inaccessible until a new survey is completed. No one is promised that the work will make their homes safer today.

The representative wants the inspection to continue, with the family's own observer inside the outer marker and a clear evacuation signal. Areelu accepts the conditions without bargaining for trust. She marks the boundary and gives the observer the signal flag. The representative can still call the test off once it begins.''',
              c('[Proceed under the residents’ stated conditions.]', "gate_briefing", flags=f("gate_permission_granted")),
              c('[Recommend evacuation anyway. Consent to inspection is not an obligation to accept risk.]', "gate_withdraw", flags=f("gate_residents_consulted", "gate_inspection_withdrawn"))),
            n("gate_briefing", "Commander", '''Before anyone touches the ring, the observer asks each person to say what will end the test. The representative says the signal flag ends it. The observer says any change in the seam's rhythm ends it. Areelu says a request to stop ends it even if the readings remain stable. You say the Trickster intervention ends with the page; it will not be used to force a second attempt if the first fails.

The observer repeats the evacuation route and checks that no one will be left inside the marked boundary. The representative confirms that two households have already left and the others know where to wait. Areelu places her working archive in a separate case. If it becomes the anchor, only the observer can make the copy of the measurements public; neither Areelu nor you can quietly replace the original later.

No one signs a waiver pretending to make the risk disappear. The field record lists what remains uncertain, how each person may stop, and what they will lose if the gate is closed. The representative reads the list before approving the next step.''',
              c('[Confirm the briefing and let the chosen procedure begin.]', "gate_prediction", flags=f("gate_safeguards_confirmed")),
              c('[Notice a missing resident from the attendance list. Stop until their evacuation is verified.]', "gate_withdraw", flags=f("gate_safeguards_checked", "gate_inspection_withdrawn"))),
            n("gate_prediction", "Commander", '''The observer asks for predictions before any intervention: which reading should change first, how quickly the seam should respond, and what would count as evidence that the procedure failed. Areelu answers that a successful closure should remove the false pressure signal without changing the stone around it. If the arch shifts, if the rhythm accelerates, or if the reading begins to cite a new source, everyone leaves.

You make the same prediction about the Trickster method. The contradiction may close the command's loop, but it cannot promise the stone will remain inert. It cannot erase whatever history the gate records. It cannot be used twice if the first attempt fails, because the anchor will already be spent.

The representative asks Areelu whether she would continue if the gate remained open after the archive was consumed. She says no. The site would be evacuated; they would wait for a new survey, even if she never got the answer she wanted. The observer writes that commitment into the plan. A prediction is not a guarantee, but it gives everyone a reason to recognize the moment to stop.''',
              c('[Proceed only with the listed stop conditions in force.]', "gate_decision", flags=f("gate_stop_conditions_recorded")),
              c('[Stop the inspection and order evacuation. The remaining uncertainty is enough reason to wait.]', "gate_withdraw", flags=f("gate_inspection_withdrawn", "gate_uncertainty_accepted"))),
            n("gate_decision", "Areelu", '''The representative's conditions are clear: the observer stays inside the outer marker, the evacuation signal remains visible, and the first sign of instability ends the test. Areelu repeats each term and waits for the representative to confirm them. Only then does she step to the copper ring.

The seam continues to pulse at the same interval. The inspection can still end with the instrument lost and the gate sealed, with the Trickster intervention and the archive consumed, or with an evacuation while the question remains open. Permission to inspect has not become permission to continue at any cost.''',
              c('[Ask Areelu to close the ring herself and accept the loss of this measurement.]', "gate_close_areelu", flags=f("gate_operator_closes")),
              c('[Offer the Trickster contradiction with its archive cost, and let Areelu decide whether to authorize it.]', "gate_trickster_offer", flags=f("gate_trickster_proposed"), requires=f("active_trickster_path", "entry_ready")),
              c('[End the inspection at the agreed boundary. Evacuate and wait for a new survey.]', "gate_withdraw", flags=f("gate_inspection_withdrawn"))),
            n("gate_close_areelu", "Commander", '''Areelu does not reach for the ring until the representative repeats the evacuation signal. She grounds the outer circuit with a copper pin. The seam contracts, and the instrument's central plate cracks. The reading is gone. She does not call the site solved; the old gate is sealed and the archivist will have to inspect it again before anyone returns.

The representative checks the outer boundary, then gives the signal to go home. No one is injured. The panel receives a report that names Areelu as the person who closed the mechanism, records the destroyed instrument, and marks the site's final safety status unknown pending survey.''',
              c('[Sign the record as a witness to the procedure, not as a guarantor of safety.]', "gate_consequence", flags=f("gate_closed_by_areelu")),
              c('[Let the independent observer file the report without your signature.]', "gate_consequence", flags=f("gate_closed_by_areelu", "intervention_private"))),
            n("gate_arcana_success", "Commander", '''You isolate the old reading from the new. If you ground the outer ring at the point where the copper has begun to darken, the seam should lose the false signal. The instrument will be destroyed; the archive's measurements will end at the moment of closure. The gate itself may remain as a sealed ruin, but the nearby families will no longer be inside an active reading boundary.

Areelu watches the copper. "That is a result I can accept. The question is whether the residents accept losing the instrument that might explain why it happened." The observer asks for the measurement sheets to be copied before any action. Areelu agrees. The representative has heard enough to ask a sharper question: who decides whether the loss is worth it?''',
              c('[Ground the ring after the observer copies every readable measurement.]', "gate_ground", flags=f("gate_instrument_lost")),
              c('[Ask the representative whether they accept losing the instrument in exchange for closing the gate now.]', "gate_tradeoff", flags=f("gate_measurement_tradeoff"))),
            n("gate_tradeoff", "Commander", '''You explain the trade: the outer ring can be grounded, which is likely to close the gate but will destroy the instrument. The archivist has copied what is readable. The families will still need a later survey before returning to the site.

The representative considers the loss and asks the observer to confirm the copied pages are legible. Only after the observer confirms do they agree to close the gate. They do not call the trade fair; they call it preferable to leaving the old mechanism active. Their consent covers this action alone.''',
              c('[Ground the ring under the stated conditions.]', "gate_ground", flags=f("gate_instrument_lost", "gate_tradeoff_accepted")),
              c('[Respect their hesitation and withdraw for evacuation.]', "gate_withdraw", flags=f("gate_tradeoff_declined", "gate_inspection_withdrawn"))),
            n("gate_arcana_failure", "Commander", '''You can read the two patterns but cannot establish where to ground the ring. Areelu says nothing while you revisit the lines. The observer asks whether the families should evacuate now. The seam remains stable, but no one has proved how long it will remain so.

"Do not bluff because we are waiting," Areelu says. "A delay is a choice too, but it is not the same as certainty." The residents' representative asks for the options to be stated without a guarantee. You can propose the Trickster intervention with its named cost, recommend evacuation and site closure, or ask Areelu to continue only after another survey.''',
              c('[Tell the representative the risk is unresolved and recommend immediate evacuation.]', "gate_withdraw", flags=f("gate_uncertain", "gate_inspection_withdrawn")),
              c('[Propose the copy-only Trickster contradiction, with the archive cost stated in advance.]', "gate_trickster_offer", flags=f("gate_uncertain", "gate_trickster_proposed"), requires=f("active_trickster_path", "entry_ready")),
              c('[Pause. No intervention until an independent survey establishes a safe boundary.]', "gate_withdraw", flags=f("gate_uncertain", "gate_inspection_withdrawn"))),
            n("gate_trickster_offer", "Commander", '''You explain what the Trickster method can do and what it cannot. It can make the old command contradict its own claim that the reading continues. It cannot restore whatever the instrument records or prove that the arch is harmless. The contradiction needs an anchor; Areelu's working archive is the only object at the site carrying the full original sequence. If you use it, those papers will be consumed. The residents may lose the best historical account of the gate.

Areelu's face tightens. "That archive is mine. The choice to spend it is also mine." She looks to the observer. "If the Commander offers the intervention, I may accept or refuse it. Do not let my presence make refusal look cowardly." The observer records the proposed cost. The representative can withdraw before the contradiction is made.''',
              c('[Ask Areelu to authorize the archive as the anchor, knowing the record will be destroyed.]', "gate_trickster_authorized", flags=f("gate_anchor_requested")),
              c('[Withdraw the intervention. The archive should survive, even if the gate remains sealed by evacuation.]', "gate_withdraw", flags=f("gate_anchor_refused", "gate_inspection_withdrawn")),
              c('[Let the residents’ representative decide whether the local risk is worth the archive cost.]', "gate_residents_decide", flags=f("gate_residents_decide"))),
            n("gate_residents_decide", "Commander", '''The representative asks whether the archive can be copied. The observer confirms that every readable measurement is already preserved, though the original sequence would be lost. The representative asks whether the Trickster intervention itself is guaranteed to close the gate. You answer no: it may expose the contradiction, but no one should call the result certain until it happens.

The representative agrees to the proposed cost on behalf of the residents who chose to attend. They also state that if Areelu refuses to spend the archive, or if you refuse to make the intervention, they will evacuate and wait. Their consent is not permission for anyone to proceed against the others' will.''',
              c('[Tell Areelu the residents accept the stated risk. She must still choose whether to authorize her archive as the anchor.]', "gate_trickster_authorized", flags=f("gate_resident_consent_recorded")),
              c('[Withdraw. The representative’s consent does not obligate you or Areelu to continue.]', "gate_withdraw", flags=f("gate_resident_consent_recorded", "gate_inspection_withdrawn"))),
            n("gate_trickster_authorized", "Areelu", '''Areelu closes her eyes once, then opens them. "I authorize it. Not because I think the archive is disposable, and not because you asked. I authorize it because the residents are here, the cost is recorded, the observer has copied what can be copied, and I choose to spend my work to limit the risk I helped create." She looks directly at you. "You do not owe me the trick. If you proceed, it is your choice too."''',
              c('[Proceed. Let the contradiction consume the working archive and close the gate.]', "gate_closed_trickster", flags=f("gate_anchor_spent"), requires=f("active_trickster_path", "entry_ready")),
              c('[Stop. Areelu’s permission does not obligate you to use the Trickster power.]', "gate_withdraw", flags=f("gate_anchor_refused", "gate_inspection_withdrawn"))),
            n("gate_ground", "Commander", '''You place the copied measurements outside the ring and set the copper ground against the dark point. Areelu holds the far marker while the observer watches the seam. The gate contracts in two pulses. The instrument's center cracks and the false reading vanishes with it. Nothing explodes. No one is hurt. The measurements end, and so does the chance to learn more from that particular device.

The residents' representative checks the boundary before approaching. Their houses are outside the reading now. They do not thank Areelu; they thank the observer for telling them what the instrument could and could not promise. Areelu accepts the distinction without asking to be included.''',
              c('[Record the loss of the instrument and leave the remaining survey to the archivist.]', "gate_consequence", flags=f("gate_closed_by_ground")),
              c('[Stay until the families confirm the route back to their homes is clear.]', "gate_consequence", flags=f("gate_closed_by_ground", "residents_accompanied"))),
            n("gate_closed_trickster", "Commander", '''The contradiction takes hold only after Areelu's authorization and the residents' approval. The old command declares that the gate must continue because its opening has not finished. The margin answers that the command's continued existence proves the opening is already complete. Both lines appear on Areelu's archive page; neither can hold the other as a premise. The red seam contracts until the stone arch is only stone.

The working archive goes blank. The copied measurements remain outside the ring, but the sequence that tied the instrument to the old ritual is gone. The families leave safely. The observer records that no injury occurred and that the archive was deliberately spent, not secretly destroyed.

Areelu looks at the empty page. "You did not undo the old ritual. You made its command unable to pretend it was still happening." She turns to the representative. "That was the cost I authorized. The decision to close the site is yours now." The representative chooses a full survey before anyone returns. Areelu accepts the delay.''',
              c('[Let the independent observer record your intervention and Areelu’s authorization in full.]', "gate_consequence", flags=f("gate_closed_by_trickster", "intervention_recorded")),
              c('[Give the residents the public account, but keep your role out of the report.]', "gate_consequence", flags=f("gate_closed_by_trickster", "intervention_private"))),
            n("gate_withdraw", "Areelu", '''The inspection ends. The residents' representative orders an evacuation while the archivist arranges a full survey. The gate stays under observation; it is neither declared safe nor described as an imminent catastrophe. Areelu gives the observer every measurement she has and leaves the working archive intact.

"I wanted to know what the gate would do," she says. "That was not enough reason to put people beside it." She does not hide her frustration at losing the chance to study it. The frustration does not change the evacuation order. You leave with an unresolved site and no claim that the danger has passed.''',
              c('[Stay to help the families relocate until the survey is complete.]', "gate_consequence", flags=f("gate_left_unresolved", "residents_accompanied")),
              c('[Let the observer manage the relocation. Do not turn care into another experiment.]', "gate_consequence", flags=f("gate_left_unresolved"))),
            n('gate_consequence', 'Commander', '''The observer reads back the decisions and the measurements actually taken. Gaps remain where you chose to stop.
Areelu corrects the position of one marker, then signs beneath the account of her own part in the work.
The residents receive copies of the pages concerning their homes. A survey must precede any return to a closed-off area.
The observer keeps the identifying witness copy under seal when you requested privacy. The public account cannot turn an unnamed participant into an absent one.''',
              c('[Seal the field record and carry one copy to the families’ representative.]', next='gate_review', flags=['areelu.trickster_opening.gate_report_complete']),
              c('[Ask the observer to read the report once more before anyone signs.]', next='gate_review', flags=['areelu.trickster_opening.gate_report_complete', 'areelu.trickster_opening.report_crosschecked'])),
            n('gate_review', 'Observer', '''The archivist asks each participant to confirm their own part in the record.
Areelu identifies the material she brought to the site. You confirm what you chose to do with it. The representative checks the marked boundary and the evacuation arrangements.
Nobody signs for anyone else.
The last paragraph says the work ended without injury and leaves the remaining uncertainties attached to the site.
Areelu taps that paragraph. "Keep it. A competent enemy will ask those questions before an incompetent ally does."''',
              c('[Approve the report and leave the technical review open until the site survey.]', next='gate_aftermath', flags=['areelu.trickster_opening.gate_independent_review_complete']),
              c('[Ask the observer to preserve the report exactly as read, including the uncertainty.]', next='gate_aftermath', flags=['areelu.trickster_opening.gate_independent_review_complete', 'areelu.trickster_opening.uncertainty_preserved'])),
            n('gate_aftermath', 'Areelu', '''The report records the cost in the same language the panel required: what happened, what was lost, what remains uncertain, and who chose each step. Areelu signs her name below the intervention or the withdrawal. She does not write that the gate is solved unless it was actually closed, and she does not claim that a harmless outcome proves the risk had been imaginary.

Outside the marked site, she asks whether you want to talk about the work, the relationship, or neither. She does not choose for you. The result has changed the future of the old archive and the residents' immediate plans. It has not proved that she is safe to love or that your choices make her less responsible for her own.''',
              c('[The gate is closed. Now let us decide who gets to learn how we did it.]', next='gate_power_bargain', flags=['areelu.trickster_opening.gate_arc_complete'], requires=['areelu.trickster_opening.gate_closed_by_trickster']),
              c('[Talk about the consequences before discussing the relationship.]', next='gate_relationship', flags=['areelu.trickster_opening.gate_arc_complete']),
              c('[Ask to walk together in silence. Do not turn the outcome into a verdict.]', next='gate_relationship', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.gate_silence_chosen']),
              c('[Leave. You need distance before the next private conversation.]', next='gate_next', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.relationship_paused'])),
            n("gate_power_bargain", "Areelu", '''"The measurements belong to the residents," Areelu says. "We settled that."

"Measurements are harmless without the missing sequence. Your archive is gone, and my trick has no diagram. The next person who wants to close such a gate will have to come to us."

For the first time since the observer began reading, she gives you her whole attention.

"Us?" she asks. "You have advanced remarkably far in the division of my work."

You point out that she cannot reproduce the contradiction without you. She answers that you could not have found its anchor without her. Neither statement needs embellishment. Beneath the ruined arch, the surveyor hammers a numbered peg into the earth. Each blow gives the two of you a little time to imagine what a monopoly might be worth.

"A ruler could demand a fortress, an oath, a life," she says. "For the privilege of being rescued from a danger he did not create. You understand that this is the same bargain a demon would offer?"

"A demon would leave a clause that lets the gate open again."

"And you would congratulate yourself for leaving it closed while you counted the payment." Her smile is cold, interested. "At least you have stopped pretending every appetite you possess is a public service."

You can hear temptation in her contempt. She does not conceal it. She has spent the only complete sequence and hates being left with scraps, while the power that consumed it remains yours to use. A bargain would give her something she wants: a place in the next discovery that you could not quietly take away.

"I will not become your court magician," she says. "If I agree, I choose my work. You choose whether to offer your talent. Neither of us promises the other a subject for an experiment. The families keep the readings we promised them."

She looks back at the arch. "But I see no reason to hand every ambitious fool the means to repeat this. The difference between prudence and a private empire is often the price written on the invitation. What price did you have in mind?"''',
              c('[Protection has a price. We choose our patrons and divide what they pay us.]', "gate_monopoly", flags=f("private_research_pact", "ambition_admitted")),
              c('[No price for people in danger. I want the technique protected from imitation, not sold.]', "gate_public_method", flags=f("method_restricted_for_safety")),
              c('[I wanted to hear you consider it. Publish what can safely be taught.]', "gate_public_method", flags=f("method_public_intent"))),
            n("gate_monopoly", "Commander", '''"Half," Areelu says.

"Of the gold?"

"Of whatever you decide is worth asking for. If you obtain a library, I use it. If you obtain a fortress, I hold a key. If someone swears an oath to purchase your help, you tell me its words before accepting. I will not lend my mind to an empire whose terms I discover afterward."

You ask what she offers in exchange. She names the surveys she still possesses, then stops before identifying their locations. Those will come after you agree. Her caution is almost refreshing after an afternoon of public declarations.

"And if I keep the price secret?"

"Then you keep the next gate." She glances toward the blank archive. "Find someone else who can tell you which page to burn."

There is no spell in the threat. She is describing something she can do without your permission, and both of you know it. You agree to disclose the price. She agrees to share the surviving surveys. No names or promises are purchased from the families here; their danger is already ended, and nothing more is owed for it. The bargain concerns the next petitioner, who may arrive with fewer alternatives than either of you would care to admit.

Before you leave, Areelu returns to the observer. She confirms that the settlement will receive the measurements and refuses a request for a general account of the method. The observer writes the refusal beside her name. It will be public. Areelu watches the ink dry without asking that it be softened.

On the road she walks close enough that her sleeve brushes yours. "I prefer knowing when you are dangerous," she says. "It saves me the trouble of admiring your charity."

You ask if admiration was ever a possibility.

"Do not spend it before you have earned it."''',
              c('[Agree to the division. Keep the method between you.]', "gate_next", flags=f("research_price_shared", "method_withheld"))),
            n("gate_public_method", "Areelu", '''Areelu's expression cools. "Then decide what can safely be taught before promising it. I will not see another fool scratch an approximation into a wall and discover the error by opening it."

You agree that the published measurements should carry no ritual sequence. The archivist can collect requests from scholars willing to submit their reconstruction for examination. Areelu insists on the right to reject a dangerous proposal, then catches your look.

"You may examine it too," she says. "I am not afraid of disagreement. I am afraid of mediocrity with access to a chisel."

The arrangement gives you neither a private price nor an obedient research partner. It gives future petitioners somewhere to bring their questions. She is visibly less pleased by this than by the prospect of a bargain. When you ask whether she will still attend the first examination, she answers that she would hardly trust you to conduct it alone.''',
              c('[Tell the archivist how scholars can request an examination.]', "gate_next", flags=f("research_requests_open"))),
            n("gate_relationship", "Commander", '''You walk outside the evacuation markers. The archivist and the observer remain with the residents. Areelu does not ask you to tell her whether she did the right thing. Instead she asks what you will remember about it when she later tries to use the outcome as proof that she can be trusted.

You tell her the choice can be judged only in its context: she offered a warning, accepted independent limits, named the archive as a cost, and let the residents stop the test. A safe result cannot prove that the risk was necessary. An unresolved result cannot prove that her caution was cowardice. The future should be allowed to judge what she does next, not be forced to vindicate this one decision.

Areelu thinks about that. "I wanted the gate to give me an answer about myself," she says. "I wanted to know whether I could make a choice that did not repeat the old one. The result cannot tell me that. Only the next choice can." She turns toward you. "I would like to make those choices where you can see them. I do not want you to become responsible for watching me make them."''',
              c('[Tell her you will stay in the relationship, but you will not become her monitor.]', "gate_next", flags=f("gate_arc_complete", "relationship_boundary_reaffirmed")),
              c('[Tell her you need distance before the next private conversation.]', "gate_next", flags=f("gate_arc_complete", "relationship_paused")),
              c('[End the romance. You cannot accept the role she is asking you to play, even if she says she does not want a keeper.]', "gate_next", flags=f("gate_arc_complete", "relationship_ended"))),
            n('gate_next', 'Commander', '''The next meeting is not scheduled as a test. Areelu leaves the time blank and gives you the option to choose it, decline it, or ask her to send one invitation later. She has learned that a person can be present without being a witness on command. Whether she remembers that lesson when she wants something remains to be seen.''',
              c('[Meet again after the observer publishes the report.]', next='gate_result_followup', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open']),
              c('[Let Areelu contact you once the families’ survey is complete.]', next='gate_result_followup', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open']),
              c('[End the personal relationship and leave the site record with the archivist.]', flags=['areelu.trickster_opening.closed', 'areelu.trickster_opening.gate_arc_complete'], abort=True)),
            n('gate_result_followup', 'Areelu', '''The observer brings the site report. Areelu waits while you turn to the measurements.''',
              c('[Review the closure and the lost anchor.]', next='gate_aftercare', requires=['areelu.trickster_opening.gate_anchor_spent']),
              c('[Review the closure achieved without an anchor.]', next='gate_aftercare', forbids=['areelu.trickster_opening.gate_anchor_spent', 'areelu.trickster_opening.gate_left_unresolved']),
              c('[Review the unresolved site and continued evacuation.]', next='gate_unresolved_followup', requires=['areelu.trickster_opening.gate_left_unresolved'])),
            n('gate_unresolved_followup', 'Areelu', '''The gate is still active. The observer has put a red line across the old footpath and posted someone at each approach.
The families can reach water by the upper road, but it adds an hour to every trip.
Areelu proposes a survey from outside the ring. Their representative refuses to move the boundary until the first readings return.
'You are making ignorance expensive,' she says.
'It was already expensive. We used to pay without knowing why.'
She studies the map. Then she marks the position from which the next reading can be taken without crossing the line.
Her working archive remains intact. Keeping it has left you with a live hazard and people who must continue living around it.''',
              c('[Fund the longer water route and leave the boundary in place.]', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.unresolved_monitoring_funded']),
              c('[Leave the survey in local hands. Offer no experiment today.]', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.unresolved_monitoring_local'])),
            n('gate_aftercare', 'Areelu', '''The observer's report is published without turning the safe outcome into a guarantee about the future. One of the residents writes to the archive with a correction: the evacuation route was clear, but the marked boundary cut across a path their family uses for water. The map is amended. Areelu does not dismiss the detail because the central reading interested her more.

She asks the archivist to inspect the footpath before the families return. The observer says the additional survey will delay access by three days. Areelu accepts the delay. The decision is inconvenient and small. It matters because the people affected were able to correct the record after the experiment ended.

When she meets you again, she brings no flowers and no proof of what the day meant. She asks whether you want to hear what the map correction changed. If you say yes, she tells you. If not, she lets the subject go. The relationship does not require that you become interested in every consequence she learns to face.''',
              c('[Hear the correction, then choose whether to discuss the relationship.]', next='gate_debrief', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.aftercare_heard']),
              c('[Leave the report with the archivist. Meet Areelu without making work the price of closeness.]', next='gate_debrief', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.aftercare_not_needed'])),
            n('gate_debrief', 'Areelu', '''The aftercare survey finds a narrow path along the outer wall that was missing from the first map. It does not change the gate report, but it changes where the families can collect water while the area stays closed. The archivist adds the map, the residents check it, and Areelu signs the correction without rewriting the earlier version.

She says she once thought the work was complete when the central mechanism was solved. The families' correction proves that ending the spell and understanding its reach are different tasks. The gate might be sealed; the consequences do not end at its boundary.

Areelu leaves the corrected map with the observer. The work for today is finished. You decide whether to walk back together or take your own road.''',
              c('[Walk together, then keep the next meeting on the date you both choose.]', next='gate_reinspection', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.gate_debrief_shared'], forbids=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_paused']),
              c('[Take your own road and wait for the next survey.]', next='gate_reinspection', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.gate_debrief_apart'])),
            n('gate_reinspection', 'Commander', '''The archivist schedules a site reinspection after the ground has settled. You attend with Areelu, but the residents' representative remains the person who decides whether anyone approaches the boundary. The survey team finds no active pressure reading. It does find heat in the stone at the point where the old ring met the wall.

The observer asks whether the heat means the gate is beginning to open again. Areelu says it could be residual warmth from the intervention, a property of the stone, or a sign that the seal is incomplete. The available measurements cannot separate those explanations. The team marks the wall and schedules another reading rather than taking a sample without the residents' agreement.

Areelu wants to keep the site closed until she understands the heat. The representative wants access to the path restored as soon as the survey finds it safe. You ask what evidence would be sufficient for each decision. The team agrees on a temperature threshold, a second reading after seven days, and a route that does not pass through the old arch. No one gets certainty. They get a specific condition they can revisit.

Areelu signs the plan even though it does not grant her more time at the site. She says she used to call unresolved information an invitation to continue. The reinspection gives her a boundary instead: the work continues only when the people affected agree to it and the next reading meets the agreed conditions. If the facts change, the decision can change too.''',
              c('[Accept the survey plan and leave the site to the appointed team.]', next='gate_archive_followup', flags=['areelu.trickster_opening.reinspection_plan_set']),
              c('[Ask the archivist to send you the next reading, but do not return to the site.]', next='gate_archive_followup', flags=['areelu.trickster_opening.reinspection_remote'])),
            n('gate_archive_followup', 'Areelu', '''The next reading and Areelu's working papers are ready for comparison.''',
              c("[Compare the surviving measurements against the spent archive's index.]", next='gate_followthrough', requires=['areelu.trickster_opening.gate_anchor_spent']),
              c('[Compare the readings with the intact working archive.]', next='gate_archive_kept', forbids=['areelu.trickster_opening.gate_anchor_spent'])),
            n('gate_archive_kept', 'Areelu', '''The second reading confirms that the closed gate has stayed quiet. Areelu lays the intact archive beside it and finds the corresponding sequence without hesitation.
'You see what we kept,' she says. 'Precision. Not a heroic story about a blank page.'
The surveyor finds heat at the old ring's edge. Areelu traces it to a broken conduit, which the team will inspect before allowing anyone under the arch.
A narrow route outside the ring meets the residents' agreed limits. Their representative opens that route alone; the ruin remains fenced.
Areelu keeps her original sequence. The survey office keeps the measurements and its own account of the ordinary closure.
Neither is a substitute for the other.''',
              c('[Let the residents mark the safe route.]', next='gate_ordinary_marker', flags=['areelu.trickster_opening.route_reopened']),
              c('[Receive later reports without attending the walk.]', next='gate_ordinary_marker', flags=['areelu.trickster_opening.monitoring_residents_choose'])),
            n('gate_followthrough', 'Areelu', '''The next reading arrives seven days later. The heat has faded, the ground has settled, and the residents' representative asks for the marked path to reopen. The survey team recommends a narrow route around the arch and another inspection before winter. Areelu asks whether the evidence justifies keeping the whole site closed. The representative says it does not.

Areelu does not argue that her caution should override the recommendation. She asks the surveyor to explain what the open route will and will not guarantee. The route avoids the old ring; it cannot prove that the stone will never shift again. The residents accept that uncertainty because it is the same uncertainty they lived with before. They do not need Areelu to promise safety. They need a plan that tells them who to contact if the reading changes.

The archivist assigns a local observer and publishes the threshold. Areelu gives them every remaining note about the old gate. The archive she spent remains gone. She does not treat the loss as a reason to keep the residents away indefinitely so that her sacrifice will seem more valuable.

You ask whether she regrets spending the archive. She says yes, because she wanted the record. She also says she would make the choice again under the same conditions. The answer is hers; you are not asked to make it heroic. The residents sign their names beneath the route plan, not beneath Areelu's account of what the choice meant.''',
              c('[Close the field record and let the residents use the route under the published conditions.]', next='gate_residents_revisit', flags=['areelu.trickster_opening.route_reopened']),
              c('[Keep receiving the survey reports, but let the residents decide when they no longer need them.]', next='gate_residents_revisit', flags=['areelu.trickster_opening.monitoring_residents_choose'])),
            n('gate_ordinary_marker', 'Areelu', '''The marker names the closed gate and the route around it. There is no sacrificed archive to commemorate.
The residents ask Areelu which conduit remains unexamined. She points it out and adds a warning to the survey sketch.
'It would have been more satisfying to solve all of it,' she says on the way back.
'Then you should have chosen a less inconvenient world.'
She gives you a sidelong look. 'I did try.'
The original papers stay in her case. The gate stays closed, with an unfinished inspection beside its name.''',
              c('[Leave the site with the ordinary closure recorded.]', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.marker_residents_authored'])),
            n('gate_residents_revisit', 'Commander', '''The residents open the route the next morning. Their representative asks Areelu to attend the first walk, not as the person who solved the gate, but as the person who authorized the test. Areelu accepts. The residents do not ask for her explanation; they ask where the old ring was and which stones were replaced.

She answers each question without claiming that the intervention restored the original structure. The rep asks why she chose the archive as an anchor. Areelu says it was the only object that carried the full sequence and that she chose to spend it. The representative asks whether she regrets the loss. She says yes. They say that is not their concern. They want to know if the record can be reconstructed from the copies.

The archivist says the broad measurements survive, but the sequence does not. The residents decide to build a new marker that records the gate's closure and the date of the survey. It will not bear Areelu's name alone. It will list the observers and the families who approved the route. Areelu asks if she may contribute to the cost. The representative says the repair funds already cover what was requested; any further payment would need a new request.

She accepts that limit. You notice that she still wants to be remembered as part of the event, and that wanting recognition is not automatically a reason to deny it. The question is who decides what the marker says. The residents do. The archive holds the longer account. You and Areelu leave the site after the walk, with no medal to bring into your relationship.''',
              c('[Let the marker carry the residents’ names and the observers’ account, without a romantic dedication.]', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.marker_residents_authored']),
              c('[Decline the ceremony and leave the account to the archivist.]', flags=['areelu.trickster_opening.gate_arc_complete', 'areelu.trickster_opening.second_question_open', 'areelu.trickster_opening.marker_ceremony_declined'])),
        ],
        requires=("areelu.trickster_opening.copy_arc_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=168,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_unmeasured_answer",
        "The unmeasured answer",
        "Areelu",
        5,
        "unmeasured_entry",
        [
            n("unmeasured_entry", "Areelu", '''The invitation arrives after the archivist closes the last review for the season. It names a place outside Drezen, a disused survey station whose foundations predate the Worldwound. Areelu adds that she has checked its wards twice and that you should still bring your own precautions. At the bottom, in smaller script, she writes: "This is not a request to inspect a record. If you come, I would like to speak with you without one between us. If that changes, leave."

The station sits above a narrow ravine. A temporary lamp glows in the entrance. Areelu has left the door unlocked and the nearest escape route unobstructed. She stands beside a bare table, wearing the same composed expression she uses when a result is already disappointing her.

"I am aware of the irony," she says. "I have invited you to a room I selected, prepared, and warded, then written that you are free to leave. It is still my room. I thought you should be able to see the means of departure before deciding whether to trust the words."

You look over the wards. They protect against intrusion and do nothing to keep anyone inside. "That is a start."

"I dislike starts. They suggest a destination."

You tell her that a start only proves she has not yet chosen the ending. Her mouth shifts, nearly a smile. "You have made a career of treating the distinction as an invitation."

She has not placed the chairs behind the table. You choose one, and she takes the other. For a moment neither of you speaks. The empty surface between you is a choice she has made visible. No instrument, no memory, no ledger will answer in either of your places.

The survey station has a slit window facing the ravine. Moonlight catches the old stone and the scrub grass below it. Nothing here resembles the wound she opened in the world. It is a quiet place built by people who expected their measurements to outlive them, and then forgot to leave a record of what they wanted measured.

You ask whether she chose it because the place has no history.

"Because its history is not ours," she says. "I do not want to pretend that makes this neutral. I wanted a room where you would not have to look at my work while deciding what you feel about me. I wanted to be alone with you, and I wanted the setting not to argue in my favor."

You tell her that a room cannot make a choice innocent. It can only make the choice easier to see.

"That is probably why I have never liked rooms without instruments." She glances at the blank table. "They make it harder to pretend I came for a result."

You ask if the thought frightens her.

"It irritates me. Fear would be more flattering. I would like to believe that only fear makes me hesitate." She meets your gaze. "I have often mistaken a compelling explanation for a good reason. Tonight I do not have one. I want you here because I want you here."

The directness is almost a dare. You could answer with a joke, or with one of the carefully balanced phrases that has kept the two of you from asking too much. Instead you say that wanting can be honest and selfish at once. Neither quality decides what to do with it.

"You think I want absolution."

You tell her that you think she wants more than one thing, and she dislikes having to choose which one to admit first.

Her gaze sharpens. The old rivalry returns, but its edge is turned toward the claim rather than toward your throat. "And you believe you can tell me which desire is real?"

You say you believe she can. You also believe she may lie to herself about it, as anyone can. You are not offering to be her judge. You are asking her not to make you an instrument she uses to avoid judging herself.

For several breaths, she says nothing. Then she moves one chair slightly away from the table. It is a small gesture, unremarkable to anyone else. You understand it as an answer: she will not ask the room to decide what she has to say.''',
              c('[Ask what she wants to discuss, and leave the door open behind you.]', "unmeasured_question", flags=f("unmeasured_door_open")),
              c('[Close the door after checking the ward yourself. The room is hers, but your choice is yours.]', "unmeasured_question", flags=f("unmeasured_ward_checked")),
              c('[Tell her you are not ready for a private meeting. Keep the research channel closed tonight.]', None, flags=f("unmeasured_declined"), abort=True)),
            n('unmeasured_question', 'Commander', '''You ask what she wants from the evening. Areelu folds her hands, then unfolds them when she sees you notice.

"I have spent these weeks correcting what I could in the public record," she says. "I have also spent these weeks knowing that I cannot correct what I chose merely by describing it more accurately. I wanted the record to say I was right. Then I wanted it to say I understood why I was wrong. Both wishes were attempts to put myself at the center."

She looks at you, and there is no paper between you to make the look safer. "I do not know whether I want to be loved because I am still capable of wanting someone, or whether I want you in particular. The distinction may be false. It may also be one I prefer to leave unresolved because the answer could embarrass me."

You tell her that the distinction matters, but no proof she offers can decide it for you. If she wants you, she must say so without presenting her grief as evidence and without making your desire a pardon.

"You are asking me to make an unqualified statement in a room I prepared for an argument." Her fingers tap once against the chair. "That is an irritatingly good observation."

You ask if that means she would rather leave. "No. It means I would rather find a better argument. I am trying not to confuse the two."

You say that is still an argument. This time she smiles, though the expression carries more challenge than warmth. "Then answer one honestly. What do you want from me that has nothing to do with the past?"

You could say you want her to make amends, to be less dangerous, or to become someone easier to love. None of those answers is the one she asked for. You tell her that you want her to want you, and to risk saying so without demanding that the answer repair anything.

Areelu asks whether you remember the adult life that preceded the graft. She does not ask for a name, a confession, or proof. She asks whether it feels like yours.

You tell her that you remember fragments that belong to the person you were: rooms, work, the dull certainty of having had a life before a stranger's ritual made your soul part of someone else's design. The memories are not complete, and you cannot divide every later feeling into what came from you and what the graft may have changed. That uncertainty does not make the life unreal.

She listens without trying to tell you what the memories mean. "I chose a soul because it was there," she says. "I treated its availability as permission to assign it a place in my theory. There was a whole person behind that fact, and I did not ask what the life meant to them."

You tell her the soul was yours before the graft, but the adult life is not an argument you owe her. She says she understands the distinction. It takes effort not to follow with a question about what you remember next.

"I wanted the dead to become an answer," she says. "I looked at you and treated the answer I needed as more important than the person who was already there. Calling that grief does not make it less selfish."

You tell her that this history does not decide whether you want her now. She says she knows. The pause that follows is the first one tonight that does not ask either of you to prove anything.''',
              c('[Name your desire, but refuse to let it become evidence of redemption.]', next='unmeasured_wants', flags=['areelu.trickster_opening.unmeasured_desire_named']),
              c('[Keep the evening about work. She has not answered the question you asked.]', next='unmeasured_work', flags=['areelu.trickster_opening.unmeasured_personal_boundary'])),
            n("unmeasured_wants", "Areelu", '''She studies your face as though waiting for the hidden premise. When none appears, she looks briefly irritated with you for making the direct answer harder to evade.

"I want you to disagree with me when the result matters. I want you to notice when I am trying to win the room instead of answer the question. I want to be able to ask you to stay after you have seen me do that, and I want your staying to remain a choice rather than a verdict."

The statement is neither tender nor polished. It does not mention the child, the graft, the Worldwound, or the families whose names are now in the archive. That is why it sounds more dangerous than her earlier admissions. She has left the past where it belongs and still made a claim about what she wants.

"And physically?" you ask.

Her eyes return to yours. For a few seconds her poise is so complete it could be a wall. Then her thumb traces a faint ink stain at the side of her hand.

"I want to know what it would be like to touch you without having first designed the conditions under which you might permit it." She lets that sit. "The want is mine. You need not reward me for stating it."

You tell her the answer is not a reward. It is yours to give or withhold. She inclines her head. "Then I will not make the mistake of answering for you."

The old temptation appears in her face: to turn the pause into a test whose answer she can control. She sees you notice. For once, she lets the silence remain a silence.

You say that you want her too. You also want the freedom to stop, to change your mind, or to leave after wanting her. She says, "Yes. I can want you, be disappointed, and still let you go. Those things do not cancel each other."

The words are not a vow that she will never resent you. She does not offer a promise she cannot guarantee. She says only what she can choose now.''',
              c('[Ask her to kiss you. Let the next step be a question, not a prediction.]', "unmeasured_kiss", flags=f("unmeasured_mutual_desire")),
              c('[Take her hand, but keep the evening nonsexual. You want closeness without a test.]', "unmeasured_touch", flags=f("unmeasured_mutual_desire", "unmeasured_touch_chosen")),
              c('[Tell her you want her, but not tonight. Let the desire remain unresolved.]', "unmeasured_after", flags=f("unmeasured_desire_deferred"))),
            n("unmeasured_work", "Areelu", '''"You are right," she says. "I have answered the question I wished you had asked."

She moves one chair away from the table and sits. The gesture changes nothing about the invitation; it makes the room less like a negotiation. "The work can wait. I wanted a private hour with you, and I was afraid to say that plainly because you might refuse."

You say that she may ask without promising to like the answer. "I know. I dislike knowing it."

You ask why she chose this place. Areelu looks toward the open door. "Because it has no history between us. I could have chosen the laboratory, but every surface there is an instruction. I could have chosen the archive, but then I would have asked you to be close while the families' letters sat in the next room. That would have been an abuse of the work, even if you agreed to come."

The admission costs her something visible. She is not asking you to say that she did well. You tell her that choosing a room carefully does not make the meeting safe, but it does let you see she considered what would make you feel watched.

"I considered what I would want if our positions were reversed," she says. "That is not the same as understanding it."

You answer that it is a place to begin. She gives you a look. "You keep using that word as if it is not a kind of hope."

You say you are not asking her to hope. Only to stop hiding a want behind a calculation. She does not answer at once. Then she asks if she may sit closer. You say yes. She moves one chair's width, not the whole distance. The restraint feels more honest than a dramatic gesture.''',
              c('[Let the conversation continue, and let her choose whether to ask for more.]', "unmeasured_after", flags=f("unmeasured_closeness_offered")),
              c('[Tell her that tonight should remain a conversation. No touch is needed.]', "unmeasured_after", flags=f("unmeasured_touch_declined"))),
            n("unmeasured_kiss", "Areelu", '''You step close enough for her to see the answer before you touch her. When you kiss her, she meets it with a hunger she has made no effort to disguise.

Her hand pauses beside your jaw. She asks with a look, then with the words. You answer yes. The touch is warm and deliberate. When you draw back, she lets you go, although her eyes remain on your mouth.

"That is a more convincing argument than the ones I prepared."

You tell her not to turn it into evidence. "I know. I am considering whether to risk a second demonstration."

She smiles at your expression, then grows serious.
"I want you to stay tonight. If you would rather leave, say so now. I can bear an answer I dislike."

The lamp is still burning. Your cloak hangs beside the open door. She has left you room to reach it.''',
              c('[Stay for a private evening. You want to be close to her.]', "unmeasured_night", flags=f("unmeasured_evening_accepted")),
              c('[The kiss is enough tonight. Say good night and leave.]', "unmeasured_after", flags=f("unmeasured_kiss_only")),
              c('[Tell her you want to leave now.]', "unmeasured_after", flags=f("unmeasured_departure_chosen"))),
            n("unmeasured_night", "Areelu", '''You take your cloak from its hook and lay it over the chair.
Areelu watches the gesture before she moves closer.

The second kiss is less careful than the first. You let her feel how much you wanted it, and she answers by drawing you toward her. When you pause to speak, she listens. When she changes her mind about a touch, you follow her hand instead of making her explain.

The lamp burns low. Neither of you reaches for a notebook.
For once, there is no result waiting to be recorded.

Later, she traces a line in the dust on the table.
"A poor attempt not to reach for the answer before I know the question," she says when you ask what it means.

"You could ask the question."

She turns her hand palm-up.
"Will you stay until morning?"''',
              c('[Stay beside her until morning.]', "unmeasured_morning", flags=f("unmeasured_stay_chosen")),
              c('[You want your own room tonight. Take your cloak and say good night.]', "unmeasured_after", flags=f("unmeasured_departure_chosen"))),
            n("unmeasured_morning", "Areelu", '''The survey station is pale with morning light.
Areelu has made coffee badly and resents your smile at the result.

"It is possible to be brilliant and still need instruction," you tell her.

"I will have to decide whether that was a compliment."

She takes your cup, tries it, and sets it down with an expression that makes further argument unnecessary.
The ease lasts only a moment. Neither of you tries to preserve it by explaining what it means.

Your cloak is still over the chair. When you rise to take it, she comes with you to the door.''',
              c('[Speak with her before leaving.]', "unmeasured_after", flags=f("unmeasured_night_shared"))),
            n("unmeasured_touch", "Areelu", '''You offer your hand. Areelu looks at it as if the gesture is a problem with no elegant solution. Then she places her fingers in yours.

The contact is almost formal. It is not cold. She rubs her thumb once over your knuckles and stops, waiting to see whether you will draw away. You do not.

"This is less conclusive than a kiss," she says.

"Good."

She gives a soft, surprised laugh. The sound changes her face more than any carefully measured smile. For once, she lets herself be amused without turning the moment into a weapon.

You sit beside each other. She asks what you want from the next hour, and you tell her the answer is the same as it was before: to speak honestly, to want what you want, and to be allowed to leave without having the choice used against you later.

"I can agree to that," she says. "I cannot promise that I will never be angry when you go. I can promise not to call the anger your fault."

You tell her that is enough for tonight. Her hand tightens for one heartbeat, then relaxes. The boundary does not diminish the attraction. It gives the attraction somewhere to stand.

The hour passes with talk about what neither of you knows how to do well: a quiet evening, a disagreement that does not become a contest, an invitation made without assuming it will be accepted. When you leave, she asks if she may write to you. You say yes, if the letter is a request and not a claim. She agrees. She does not ask for a promise that you will answer.''',
              c('[Say good night at the door.]', "unmeasured_after", flags=f("unmeasured_quiet_evening"))),
            n("unmeasured_after", "Commander", '''At the door, Areelu says, "I wanted you before I knew what you would answer. I want you now that I know you can refuse me. Those are not the same feeling."

You tell her the second one is the only one that can become a choice between you.

"Yes." She steps aside, leaving the way clear. "And if you do not choose me tomorrow?"

"Then tomorrow's answer will belong to tomorrow."

She absorbs this without trying to improve it. The old instinct to bargain flickers behind her eyes. She lets it pass.

Areelu lays her cup aside. "When I send another invitation, will you answer?" She asks it without the cool assurance that usually makes her questions sound like orders. Outside, the wind moves through the ravine. Your cloak is fastened and your hand rests on the door. She knows you are leaving.

Areelu asks whether she may write to you. You tell her yes, if the letter is a request and not a claim. She says she can do that. The door remains open until you cross it.''',
              c('[Continue the relationship, knowing desire does not cancel the account you shared.]', None, flags=f("unmeasured_scene_complete", "unmeasured_relationship_continue"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Keep the relationship open. Continue only by asking again, one meeting at a time.]', None, flags=f("unmeasured_scene_complete", "unmeasured_relationship_open"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Pause personal contact. Keep the public record and leave the next answer to me.]', None, flags=f("unmeasured_scene_complete", "relationship_paused"), requires=f("relationship_started"), forbids=f("relationship_ended")),
              c('[End the romance. What happened here mattered, but it does not obligate a future.]', None, flags=f("unmeasured_scene_complete", "relationship_ended"), requires=f("relationship_started"))),
        ],
        requires=("areelu.trickster_opening.gate_arc_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY, "areelu.trickster_opening.relationship_started"),
        forbids=("areelu.trickster_opening.closed", "areelu.trickster_opening.relationship_ended", "areelu.trickster_opening.relationship_paused"),
        delay=72,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
    scene(
        "areelu_trickster_opening.the_choice_after",
        "A life that does not answer for the past",
        "Areelu",
        5,
        "choice_entry",
        [
            n("choice_entry", "Commander", '''The public report closes with four columns: the original decisions, the people identified, the actions taken afterward, and what remains unknown. The gate either stands sealed or under evacuation while the survey continues. The archivist will keep the records. The families will decide whether they want further contact. None of the columns says that Areelu has made amends.

She asks you to meet in a garden above the city, somewhere neither of you has used as a laboratory. There are no notes on the table and no waiting signal. Areelu has chosen a plain dark dress instead of the clothes she wears to work. She looks like herself, not softened into an emblem of the person you might hope she could become.

"I have wanted to ask you a question without making it a test," she says. "I am not certain I know how. I can want you, resent that you can see through me, and be afraid that I will make the same kind of choice again. The fact that I desire you does not prove I will become safe. The fact that I have harmed others does not make desire for me unreal. Both facts remain."

She holds your gaze. "I want a life with you. Not a life in which you keep watch over me, or I use your affection as a private acquittal. A life that can include work, anger, appetite, quiet, and the possibility that one day you decide you have had enough. I want your body. I want your mind when you choose to share it. I want the chance to ask you to stay, and the knowledge that you may say no." She lets the words stand without reaching for your hand.

"You do not owe me an answer because we survived all this together," she says. "Tell me what you want, including if it is only tonight or nothing further."''',
              c('[Tell her the private bargain still matters. You want a partner in power as well as in your bed.]', "choice_power_future", flags=f("power_future_requested"), requires=f("private_research_pact", "relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Tell her you choose an enduring relationship, with no promise that love means approval or protection from consequences.]', "choice_commit", flags=f("relationship_commitment_requested"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Tell her you want her, but are not ready to name a lasting partnership. Continue by choice, one meeting at a time.]', "choice_continue", flags=f("relationship_continues_by_choice"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Say that the relationship has ended for you. Keep the public record intact and ask her not to follow.]', "choice_end", flags=f("relationship_ended", "relationship_closes_here")),
              c('[Say nothing personal now. You want another pause before deciding what can continue.]', "choice_pause", flags=f("relationship_paused", "relationship_closes_here"))),
            n("choice_power_future", "Areelu", '''"Then say which partner you expect to obey," Areelu replies.

"Neither. That is what will make the arrangement entertaining."

"For spectators, perhaps. I would prefer that they survive long enough to envy it."

She rests her elbows on the stone table. There is no invitation to touch her yet. She asks about the next patron who offers a province for a service you can perform in an hour. Will you tell her before accepting? Will you let her refuse the work without calling refusal a betrayal? These are questions about power, and she will not permit you to answer them with a kiss.

You repeat the bargain made below the ruined watch post. She receives the full terms before lending her knowledge. Neither of you owes the other an experiment. She can take her books and go.

"The books are not the difficult part," she says. "I could take those from an emperor. Leaving someone I wanted would be less convenient."

You ask whether she thinks wanting you has made her careless. She laughs once, without pleasure.

"You are sitting across from me because I have become willing to risk something I cannot replace. Do you require the admission in simpler words?"

You could build a formidable household from what both of you know. People would come to its doors afraid, hopeful, carrying gifts. Some would call it necessary; others would call it an extortion. She imagines the same doors. You see it in the care with which she asks who would hold the keys.

"Both of us," you answer. "And neither barred from leaving."

"I will keep my own workshop. You will not enter it simply because you have slept beside me."

You accept that condition. She accepts that you will sometimes refuse her a use of your power, even if she believes refusal is idiotic. That last concession takes her longer.

At last she reaches across the table, palm upward. "I am not promising to become harmless. I am offering to let you close enough to know when I am lying to myself. If you intend to use that knowledge against me, choose the occasion well. I will notice."

It is a dangerous offer. The warmth of her waiting hand makes it no less so.''',
              c('[Take her hand. You want the woman who made that offer.]', "choice_commit", flags=f("power_partnership_terms")),
              c('[Keep the research bargain, but decline a lasting relationship.]', "choice_continue", flags=f("relationship_continues_by_choice"))),
            n("choice_commit", "Areelu", '''Areelu does not answer with a vow. She asks what enduring means to you. You describe a chosen partnership rather than a promise that neither of you will change: the right to speak openly about other attractions, the right to set boundaries around intimacy, and the duty to disclose choices that affect the other person. Neither of you has asked for exclusivity. Any other person involved must know what is being offered, and may refuse without being cast as an obstacle.

"You will disagree with my work," she says. "Sometimes you will be right. Sometimes you will be unbearably certain because a fortunate result has spared you the consequences of a foolish method. I intend to tell you which I think it is."

You tell her you would be disappointed by anything less. She studies you a moment longer, looking for the easy compliment concealed in the answer.

"And I will not ask you to applaud the Worldwound because you want to share my bed," she says. "I know what you have seen. Spare me the lover who explains away everything he once had the courage to hate."

She steps closer. "There will be doors I keep locked. There will be evenings you should leave me alone. I am offering you a place in my life, not the authority to reorganize it." Her eyes settle on your mouth. "If you still want to kiss me, now would be a suitable time to say so."''',
              c('[Say yes. Kiss her, and let the commitment be a choice you will keep making.]', "choice_committed", flags=f("relationship_committed"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Say yes to the relationship, but not to a kiss now. Let the words be enough tonight.]', "choice_committed", flags=f("relationship_committed", "touch_deferred"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused")),
              c('[Change your mind. Keep the relationship open but do not commit.]', "choice_continue", flags=f("relationship_continues_by_choice"), requires=f("relationship_started"), forbids=f("relationship_ended", "relationship_paused"))),
            n("choice_committed", "Commander", '''Areelu hears your answer without trying to improve it. She moves to stand beside you at the balustrade, leaving the distance you chose. Below the garden, the city's lamps are being lit. A voice carries from a balcony, someone calling a name neither of you knows.

"I had an excellent argument prepared," she says.

"For what?"

"For why this would be a mistake. It was concise. You would have disliked it."

"You can still deliver it."

"I am considering whether to save it for our first quarrel."

The moment stays small by design. You are not declaring that the relationship is healthy in every respect or that no one else will be hurt by Areelu's future choices. You are declaring that you both want to continue, with the terms visible and the exits real. She tells you she wants to wake beside you when she can. You tell her what would make that welcome and what would not. She remembers the answer. For tonight, she keeps the distance you asked for.

She turns toward you. "I want you," she says, quieter. "You. With your intolerable answers and the things you still refuse to tell me." She has stopped watching the lamps. Whatever else she meant to say can wait for your answer.''',
              c('[Stay together tonight, with the same right to pause at any moment.]', "choice_future_terms", flags=f("relationship_ending_committed")),
              c('[Part for the night and begin the partnership tomorrow, in ordinary daylight.]', "choice_future_terms", flags=f("relationship_ending_committed", "intimacy_deferred"))),
            n('choice_future_terms', 'Areelu', '''The commitment does not make the relationship exclusive by default. You say that any future intimacy involving another person needs that person's full knowledge and separate consent. The arrangement must be spoken plainly to anyone else who might share it. No one will be invited to soothe jealousy, prove Areelu is healed, or serve as a reward for the Commander. You and Areelu will speak to each other before changing an agreement that affects both of you.

Areelu says she would prefer to know when you desire someone else, not because she can claim a veto but because secrecy would make her feel that she was again being managed through omission. She tells you that she may react badly before she reacts honestly. You tell her that reaction is hers to handle; you will not treat discomfort as a command, but you will listen when she speaks clearly.

She asks what happens if either of you wants to end the partnership. You tell her that the answer remains no. Neither of you gets to turn shared history into ownership. If she leaves, you will let her walk through the door. You expect the same from her.

Areelu listens without trying to negotiate down the boundary. "I want to be chosen without being guaranteed," she says. "It is more frightening than I expected." She leaves her hand resting against the balustrade. "I will try to remember that the freedom to leave is part of what makes this a choice."''',
              c('[Go somewhere private with her. Check in before each new touch and let either of you stop.]', next='choice_private_hour', flags=['areelu.trickster_opening.private_hour_chosen']),
              c('[End the evening here. The partnership begins without a sexual promise.]', next='choice_epilogue', flags=['areelu.trickster_opening.intimacy_deferred'])),
            n("choice_private_hour", "Commander", '''Areelu asks whether you want to return to her rooms. You say yes, then ask whether she wants to be touched tonight. She answers yes, and adds that she wants you to ask again after the door closes. You agree. No confidence earned in the earlier argument carries across the threshold as consent.

At her rooms, she stops before the lock and asks if you are still willing. You say yes. She turns the key only after your answer. She removes her outer garment herself, watching to see whether you are following her or only watching. You tell her what you want. She answers with what she wants: your hands at her waist, your mouth at her throat, the chance to be close without being asked to explain the old grief while she is trying to feel pleasure.

You touch her slowly enough that she can guide or stop your hand. She does both. When you pause, she asks if you are uncertain. You tell her you are listening. She says, "Then listen to this: I want you." The words are heated, not a puzzle. You kiss her, and the two of you move toward the bed together.

Her robe falls to the floor; your clothing follows by mutual choice. She pulls you closer, then asks you to wait when the intensity becomes more than she wants. You wait. She takes a breath, finds your hand, and tells you what would feel good now. She remains Areelu: commanding when she wants, guarded when a memory rises, capable of wanting pleasure without pretending it repairs anyone.

Later, you rest beside each other in the quiet. She asks whether you want her to stay awake with you or give you space. Your answer is allowed to change. The night closes without a promise about tomorrow's mood, only the shared knowledge that both of you asked and answered in the moment.''',
              c('[Stay close until morning, and let the next conversation happen after sleep.]', "choice_month_later", flags=f("intimacy_shared")),
              c('[Leave for your own room after saying good night. Desire does not remove the need for solitude.]', "choice_month_later", flags=f("intimacy_shared", "space_after_intimacy")),
              c('[Ask to stop and leave now. The choice remains yours even after the night began.]', "choice_month_later", flags=f("intimacy_stopped_by_choice"))),
            n('choice_month_later', 'Areelu', '''A week into the partnership, a letter arrives from Areelu with no question hidden in it. She says that she missed you last night, was angry about the archivist's last correction this morning, and is not asking you to choose which part you prefer. When you meet, she looks tired. The desire between you has not been diminished by that ordinary fact.

She tells you she wanted to change a paragraph in the public copy. She did not. She sent the proposed edit to the archivist with the reason she wanted to make it and the evidence that would justify it. The archivist rejected the change because it would replace an earlier uncertainty with a later interpretation. Areelu was furious. She did not retaliate, withdraw the archive, or ask you to make the rejection kinder.

"I wanted to say that I handled it well," she says. "I did not. I wanted to take the page back. I did not do that either." She allows the two statements to stay beside one another. You ask what she wants from you now. "To sit together. To be wanted. If you are able to give either without turning it into evidence about the record." She moves closer, but waits for your answer.

You tell her the partnership does not make you available on demand. She says she knows. You remind her that knowing and remembering are different things. She accepts the correction, though you can see how much she wants to argue that the moment is not a test.''',
              c('[Sit with her and speak about the anger only if she wants to continue.]', next='choice_shared_space', flags=['areelu.trickster_opening.ordinary_day_shared']),
              c('[Tell her you want her too, then ask whether she wants a kiss or company without touch.]', next='choice_shared_space', flags=['areelu.trickster_opening.ordinary_day_shared']),
              c('[Leave her to work through the anger alone, and plan another meeting later.]', next='choice_day_apart', flags=['areelu.trickster_opening.ordinary_day_apart'])),
            n('choice_day_apart', 'Narrator', '''You leave Areelu with the unfinished letter.
She does not call you back. At the foot of the stairs, you hear her shut the study door.
Your evening passes elsewhere. There will be time for the argument when you both choose to return to it.''',
              c('[Leave the next meeting for another day.]', next='choice_year', flags=['areelu.trickster_opening.partnership_reaffirmed', 'areelu.trickster_opening.ordinary_day_apart'])),
            n('choice_shared_space', 'Commander', '''Areelu chooses company without touch, at first. She talks about the rejected edit: what she wanted the sentence to say, what the archivist said the evidence supported, and why she believed the older wording had been unfair to the people who made the choice under pressure. You answer that an unfair account can be corrected with evidence; it cannot be corrected by erasing the parts that implicate her.

She challenges you in return. She returns to the cost you weighed at the gate. Would you spend an irreplaceable archive to end a danger that ordinary means might contain? The question is hypothetical; she wants to know which uncertainty you find easier to bear. You say that depends on what people were being asked to risk and what alternatives existed. She says that is an answer shaped to avoid a yes or no. You agree. A relationship is not a contest in which the fastest answer wins.

The disagreement stays alive, but the room grows easier to occupy. Areelu reaches for your hand, stops, and asks. You may let her hold it, kiss her, or end the meeting. She accepts that the choice says what you want in this moment, not what every future moment must mean.''',
              c('[Take her hand. Keep the argument unfinished and the partnership intact.]', next='choice_year', flags=['areelu.trickster_opening.partnership_reaffirmed']),
              c('[Kiss her, after answering yes. You are still attracted to the difficult person in front of you.]', next='choice_year', flags=['areelu.trickster_opening.partnership_reaffirmed', 'areelu.trickster_opening.desire_reaffirmed']),
              c('[Leave for tonight. You can love her and still need an evening alone.]', next='choice_year', flags=['areelu.trickster_opening.partnership_reaffirmed', 'areelu.trickster_opening.space_after_intimacy'])),
            n('choice_year', 'Areelu', '''The following week brings another letter from the archivist. A family has found a second record in a storage room and asks whether it changes the account. The document shows that the water ward was already failing before Areelu diverted the caravan. It does not excuse the decision. It changes how much protection the alternate route might have provided.

Areelu wants to call a new public review. The archivist recommends first comparing the document against the original maintenance logs. Areelu argues that waiting leaves the old correction unqualified for another two days. The archivist says that an immediate public revision based on a single page may make the record less reliable. Neither one is simply wrong. Areelu is impatient because she wants the account to be precise, and because she wants to control the uncertainty before it becomes another criticism she cannot answer.

She asks you what you think. You tell her that you cannot decide for the archivist or the families. You can say that the current account already marks the alternate road as uncertain, so waiting to verify a new document does not conceal its limits. Areelu objects that the public may read the delay as an attempt to protect herself. You agree that it may. The cost of a careful process is that suspicion does not pause while evidence is checked.

She remains frustrated. "I dislike leaving my name beside a question mark." You tell her that this is exactly why she should not rush the review. Her eyes flash. "Do you always have to find the least comforting answer?" You say that comfort is not the task she gave you. She exhales, almost a laugh, then declines to pretend she enjoys the answer. The archivist will check the maintenance log before either of you writes a new conclusion.''',
              c('[Let the review take the two days it needs. Keep the existing uncertainty visible.]', next='choice_shared_future', flags=['areelu.trickster_opening.second_review_waited']),
              c('[Ask the archivist to publish the new page as an unverified source, clearly marked as such.]', next='choice_shared_future', flags=['areelu.trickster_opening.second_document_provisional']),
              c('[Leave the review to the archivist. Your relationship cannot be the appeal process.]', next='choice_shared_future', flags=['areelu.trickster_opening.commander_left_review'])),
            n('choice_shared_future', 'Commander', '''The two-day review ends without a clean answer. The maintenance log confirms that the ward had begun to fail, but no surviving record says how long it would have held if the caravan had taken the other road. The archive adds the document and keeps the question open. Areelu does not get the certainty she wanted. She also does not ask the archivist to remove the new material.

When she comes to see you, she brings no papers. She asks what you have wanted from her since the first contact. You say you wanted her to treat your identity as yours, even when grief gave her a more convenient story. You wanted her to choose you as an adult she desires, not as a way to continue the failed restoration. You wanted her to remain dangerous and difficult without using those traits to make every boundary negotiable.

She listens. "I wanted you to be impossible to reduce," she says. "I wanted that because it made me curious, and because curiosity is easier to admit than need." She tells you she wants your body, the arguments, the quiet hours, and the chance that you might leave if she uses any of those things to hide from her responsibility. You tell her that wanting you is not the same as earning your trust. She says she knows, and adds that wanting you is still hers to say.

You are close enough to touch. She asks if you want to kiss her tonight. You can say yes, ask her to wait, or leave. The commitment does not convert desire into an automatic answer.''',
              c('[Say yes. Kiss her, then decide together whether the evening continues.]', next='choice_year_end', flags=['areelu.trickster_opening.desire_reaffirmed']),
              c('[Ask her to wait. You want her, but not tonight.]', next='choice_year_end', flags=['areelu.trickster_opening.intimacy_deferred']),
              c('[Leave. The relationship remains real, and so does your need for space.]', next='choice_year_end', flags=['areelu.trickster_opening.space_after_intimacy'])),
            n('choice_year_end', 'Areelu', '''A week after that review, the archivist sends the final scheduled review. The public record remains open to new evidence but has not been altered again. The family who asked for no contact has not changed their request. The families who accepted help have not sent a message. The report says only that the records were preserved and that each request was honored.

Areelu reads the notice at her desk. She does not call the interval a success. She says she used to measure progress by whether the next experiment could move forward. Over these weeks, some progress meant leaving a question unanswered, allowing a review to delay her work, and accepting that the people most affected might never speak to her.

You ask whether she regrets answering your first invitation. She says no. She says she has wanted you badly enough to imagine that wanting could make the past less ugly. She did not get that. What she got was a relationship in which you can desire her without acquitting her, and in which she can be loved without being promised immunity from criticism. She says that is harder than the fantasy she began with. It is also more real.

The evening remains yours to choose. She asks whether you want to spend it together. You can say yes, ask for a quieter night, or decline. She waits beside the open door, her cloak over one arm.''',
              c('[Spend the evening together and leave the next meeting undecided.]', next='choice_final_future', flags=['areelu.trickster_opening.year_end_together']),
              c('[Choose separate plans tonight and set another date when you both want it.]', next='choice_final_future', flags=['areelu.trickster_opening.year_end_apart']),
              c('[End the relationship here. These weeks together do not oblige us to continue.]', next='choice_final_future', flags=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_ending_ended', 'areelu.trickster_opening.year_end_relationship_closed'])),
            n('choice_final_future', 'Commander', '''The letters lie between you on the desk. Areelu has corrected a date in the margin of the first.
"Even this," you say.
"Especially this. If I am to keep a foolish letter, I want to know when I wrote it."
She sorts her own pages from yours. She leaves your decision about the relationship where you put it, without reaching for your hand or asking you to reconsider.
"Take what belongs to you. I have no wish to find it later and pretend I misunderstood."
You decide what to keep.''',
              c('[Decide what to do with the private letters.]', next='choice_last_page', flags=['areelu.trickster_opening.route_ending_recorded'])),
            n("choice_last_page", "Areelu", '''Before leaving, Areelu asks whether you want the last page filed with the archive or kept between the two of you. The letters are personal; the report belongs to everyone whose life it changed. You decide that the private details stay private: the letters, the arguments, the nights together, and the moments you asked for distance. The choices that affected families, records, or the gate remain in the archive.

She says she had thought that keeping the private life hidden would protect it from judgment. You tell her privacy is not the same as secrecy used to escape accountability. She can protect the parts that are yours to share without removing the public consequences of what she did.

Areelu adds no explanation to the bundle. She slips a blank sheet beneath the last letter, then looks at it with a brief, rueful smile.
"Habit. I keep expecting to require another page."
She removes it. What you have said is already written. What you might say next will have to wait until you mean it.

Areelu asks if you want to say anything before the page is sealed. You may say that you love her, that you want her, that you are finished, or nothing. She will not supply the answer for you.''',
              c('[Keep the letters where you can both find them.]', "choice_ordinary_future", flags=f("route_ending_recorded", "route_record_sealed"), requires=f("relationship_committed", "relationship_ending_committed"), forbids=f("relationship_ended", "relationship_ending_ended", "relationship_paused", "relationship_ending_paused", "relationship_ending_open")),
              c('[Keep her letters. You still want to see her.]', "choice_open_future", flags=f("route_ending_recorded", "route_record_sealed"), requires=f("relationship_ending_open"), forbids=f("relationship_ended", "relationship_ending_ended", "relationship_paused", "relationship_ending_paused")),
              c('[Put the letters away until you know whether to write again.]', "choice_paused_future", flags=f("route_ending_recorded", "route_record_sealed"), requires=f("relationship_ending_paused"), forbids=f("relationship_ended", "relationship_ending_ended")),
              c('[Keep one letter to remember her by, and say goodbye.]', "choice_closed_future", flags=f("route_ending_recorded", "route_record_sealed"), requires=f("relationship_ending_ended"))),
            n('choice_ordinary_future', 'Areelu', '''The next morning has no archivist waiting and no record to correct. Areelu asks whether you want breakfast. She has bought the wrong bread because she remembers your preference from a conversation you had weeks earlier and decided that memory was close enough to certainty. You tease her about the choice. She says she will learn the difference between the bread you liked once and the bread you want today by asking instead of declaring it a fact.

She asks what you want from her now. You tell her that the most difficult parts of the relationship do not become easier because you have made a promise. You still want her to desire you openly, to argue with you, to trust you with choices without making you responsible for the result. You want to keep your own life and let her keep hers. You may share a room, a bed, a secret, or a future, but none of those things lets either of you decide what the other person means.

Areelu says she wants you to stay for breakfast and wants to kiss you before you leave. She does not want you to tell her that the promise will be forever. She wants to ask again when the day changes and hear the answer then. You say yes to breakfast. She asks whether you want the kiss now. You say yes, and she kisses you with the same intention as at the beginning: desire, not absolution.

Morning finds her reading beside an open window, one bare foot tucked beneath her. She has taken your cup again. When you point this out, she inspects it with extravagant care. "An untested hypothesis. You will have to come closer." There is another cup beside her chair. She has poured it already.''',
              c('[Join her by the window.]', flags=['areelu.trickster_opening.route_ending_recorded', 'areelu.trickster_opening.ordinary_future_chosen'])),
            n("choice_open_future", "Commander", '''You leave the garden with the relationship still possible and still undecided. Areelu does not call the absence of a label a failure. She says she wants to ask you for dinner next week, and you tell her she may ask. Whether you accept will depend on the day and the answer you want then.

The two of you have named the attraction, the boundaries, the record that remains public, and the possibility that desire can continue without becoming a pledge. Neither of you has promised where another meeting will lead. When her next letter arrives, you turn it over twice before breaking the seal.''',
              c('[Read her invitation.]', flags=f("route_ending_recorded", "open_future_chosen"))),
            n("choice_paused_future", "Commander", '''The pause remains a pause. Areelu does not send a message each week to ask if it is over. The archive continues through the archivist; your personal channel stays quiet unless you choose to reopen it. If you return, she will ask what you want now. She will not use the old yes as an answer to that question.

You put her letters in a drawer. When a courier passes outside, you glance toward the window before returning to your work. You have not decided whether to write again. For now, there is no letter on your desk.''',
              c('[Close the drawer.]', flags=f("route_ending_recorded", "paused_future_chosen"))),
            n("choice_closed_future", "Areelu", '''The relationship ends without being rewritten into a test she failed or a life you were afraid to want. Areelu wanted you. You wanted her, for a time. That remains true after you leave. She does not contact you through the archive, and the archivist continues to handle necessary correspondence.

The public record remains available. Your private life does not become evidence for or against Areelu. You leave without being told to wait, and she stays without being promised that she can bring you back.''',
              c('[Put her last letter away.]', flags=f("route_ending_recorded", "closed_future_chosen"))),
            n('choice_continue', 'Areelu', '''"Then I will not call this a promise," she says. "I will call it a choice I hope you make again." She asks whether you want to meet next week, and leaves the date open for you to choose. She strikes the proposed date from her notes. "Then we leave that question open."

Areelu reaches for your hand, then stops before contact. She asks. If you say yes, she holds it without drawing you closer. If you decline, she puts both hands on the table and continues talking. Her desire remains; her answer does not depend on your touch.''',
              c('[Keep meeting at a pace you choose together.]', next='choice_epilogue', flags=['areelu.trickster_opening.relationship_ending_open']),
              c('[Keep the research collaboration but end the romance.]', next='choice_end', flags=['areelu.trickster_opening.relationship_ended', 'areelu.trickster_opening.relationship_closes_here'])),
            n("choice_pause", "Areelu", '''Areelu nods. She does not ask you to define the pause or promise when it will end. "I will leave the next step to you," she says. "That is not a threat, and it is not a test. I want you. I can want you and still wait." She leaves the garden first, giving you room to follow or remain alone.''',
              c('[Ask her to wait for your letter before arranging another meeting.]', "choice_epilogue", flags=f("relationship_ending_paused")),
              c('[End the romance and keep only the public record.]', "choice_end", flags=f("relationship_ended", "relationship_closes_here"))),
            n("choice_end", "Commander", '''Areelu receives your decision without asking what you might have said under different circumstances. She does not turn the public record into a reason you should stay, and she does not promise to become someone else for the chance to change your mind. The personal channel closes. The archive and its reports remain available through the archivist.

"I wanted a life with you," she says. "I am sorry I cannot ask you to keep wanting it after you have told me no." She steps back. You leave with no private absolution, no secret obligation, and no instruction to wait for her.''',
              c('[Say goodbye. Leave the public account untouched.]', "choice_epilogue", flags=f("relationship_ending_ended")),
              c('[Close all personal and research contact.]', "choice_epilogue", flags=f("relationship_ending_ended", "all_contact_ended"))),
            n("choice_epilogue", "Narrator", '''The garden bell sounds below you. Areelu takes her cloak from the stone bench and fastens it without looking down. She has heard your answer. There is one practical matter left before you part: the letters and private notes still kept with the research papers.

"Those belong to us," she says. "The archivist has enough to read."

She waits beside the gate while you decide what to keep.''',
              c('[Settle the private papers before leaving.]', "choice_last_page", flags=f("route_ending_recorded"))),
        ],
        requires=("areelu.trickster_opening.unmeasured_scene_complete", "areelu.trickster_opening.gate_arc_complete", "areelu.trickster_opening.active_trickster_path", ENTRY_READY),
        forbids=("areelu.trickster_opening.closed",),
        delay=240,
        optional=True,
        Relationship="areelu",
        Remote=False,
    ),
]


# BookEvent pages do not advance campaign time. End the current event at each
# dated transition and use the existing timestamped Requires/DelayHours scheduler.
FOLLOWUP_DELAYS = {
    "private_close": 12,
    "returned_after_walk": 168,
    "returned_future": 144,
    "returned_long_term": 168,
    "copy_followup": 168,
    "copy_revisit": 48,
    "copy_second_review": 168,
    "copy_long_term": 48,
    "copy_pause_notice": 72,
    "gate_result_followup": 72,
    "gate_reinspection": 72,
    "gate_archive_followup": 168,
    "gate_residents_revisit": 12,
    "unmeasured_morning": 8,
    "choice_month_later": 168,
    "choice_year": 168,
    "choice_shared_future": 48,
    "choice_year_end": 168,
    "choice_ordinary_future": 12,
}
FOLLOWUP_SCENES = {}
NODE_ORIGINS = {}


def _schedule_followups(authored_scenes):
    from copy import deepcopy

    delivered = []
    for authored in authored_scenes:
        nodes = {node["Id"]: node for node in authored["Nodes"]}
        cuts = set(nodes) & FOLLOWUP_DELAYS.keys()
        roots = [authored["Entry"], *[key for key in FOLLOWUP_DELAYS if key in cuts]]
        assigned = set()
        # Completion means the chosen sequence ended, not that its first report arrived.
        completion = {
            "returned_entry": "returned_arc_complete",
            "copy_entry": "copy_arc_complete",
            "gate_entry": "gate_arc_complete",
        }.get(authored["Entry"])
        for root in roots:
            reachable, pending = set(), [root]
            while pending:
                key = pending.pop()
                if key in reachable:
                    continue
                reachable.add(key)
                for choice in nodes[key]["Choices"]:
                    check = choice.get("Check") or {}
                    for target in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                        if target and target not in cuts:
                            pending.append(target)
            names = {key: key if key not in assigned else key + "__" + root for key in reachable}
            assigned.update(reachable)
            item = deepcopy(authored)
            if root != authored["Entry"]:
                item["Id"] += ".followup." + root
                ready = f("scheduled." + root)[0]
                item["Requires"].append(ready)
                item["DelayHours"] = FOLLOWUP_DELAYS[root]
                FOLLOWUP_SCENES[ready] = item["Id"]
            # C# displays Entry as answer text and starts at Nodes[0].
            item["Entry"] = authored["Title"]
            done = f("delivered." + root)[0]
            item["Forbids"].append(done)
            item["Nodes"] = []
            for source in authored["Nodes"]:
                key = source["Id"]
                if key not in reachable:
                    continue
                node = deepcopy(source)
                node["Id"] = names[key]
                NODE_ORIGINS[node["Id"]] = key
                for choice in node["Choices"]:
                    target = choice.get("Next")
                    check = choice.get("Check")
                    if completion and (target or check):
                        choice["Set"] = [flag for flag in choice["Set"] if flag != f(completion)[0]]
                    if target in cuts:
                        choice["Next"] = None
                        choice["Set"].append(f("scheduled." + target)[0])
                    elif target:
                        choice["Next"] = names[target]
                    if check:
                        assert check["Success"] not in cuts and check["Failure"] not in cuts
                        check["Success"] = names[check["Success"]]
                        check["Failure"] = names[check["Failure"]]
                    if not choice.get("Next") and not check:
                        choice["Set"].append(done)
                    choice["Set"] = list(dict.fromkeys(choice["Set"]))
                item["Nodes"].append(node)
            item["Nodes"].sort(key=lambda node: node["Id"] != names[root])
            delivered.append(item)
    return delivered


# These are manuscript changes using existing delivery fields, not registered events.
for _item in SCENES:
    if _item["Id"].endswith(("the_second_graft", "the_private_hour", "the_unmeasured_answer", "the_choice_after")):
        _item["Forbids"] = list(dict.fromkeys([*_item["Forbids"], *f("relationship_ended", "relationship_paused", "rivalry_only")]))
SCENES = _schedule_followups(SCENES)


def _assert_graph():
    ids = {node["Id"] for item in SCENES for node in item["Nodes"]}
    assert len(ids) == sum(len(item["Nodes"]) for item in SCENES)
    for item in SCENES:
        local = {node["Id"] for node in item["Nodes"]}
        assert item["Nodes"][0]["Id"] in local
        assert item["Entry"] == item["Title"] and item["Entry"].strip()
        assert item["MinChapter"] <= item["MaxChapter"] and item["DelayHours"] >= 0
        nodes = {node["Id"]: node for node in item["Nodes"]}
        assert len(nodes) == len(item["Nodes"])
        reached, pending = set(), [item["Nodes"][0]["Id"]]
        while pending:
            key = pending.pop()
            if key in reached:
                continue
            reached.add(key)
            for answer in nodes[key]["Choices"]:
                check = answer.get("Check") or {}
                pending.extend(target for target in (answer.get("Next"), check.get("Success"), check.get("Failure")) if target)
        assert reached == local, (item["Id"], "unreachable from C# first node", local - reached)
        for node in item["Nodes"]:
            assert node["Text"].strip() and node["Choices"]
            for choice in node["Choices"]:
                if choice["Next"] is not None:
                    assert choice["Next"] in local, (item["Id"], node["Id"], choice["Next"])
                check = choice.get("Check")
                if check is not None:
                    assert choice["Next"] is None and not choice["Abort"] and choice.get("Revive") is None
                    assert check["DC"] > 0 and check["Success"] != check["Failure"]
                    assert check["Skill"] in {"SkillAthletics", "SkillMobility", "SkillStealth", "SkillThievery",
                        "SkillKnowledgeArcana", "SkillKnowledgeWorld", "SkillLoreNature", "SkillLoreReligion",
                        "SkillPerception", "SkillUseMagicDevice", "CheckDiplomacy", "CheckBluff", "CheckIntimidate"}
                    assert check["Success"] in local
                    assert check["Failure"] in local
    active_path = "areelu.trickster_opening.active_trickster_path"
    assert set(SCENES[0]["Requires"]) == {ENTRY_READY, active_path}
    assert all(active_path in item["Requires"] for item in SCENES)
    assert "second_contact_open" in SCENES[1]["Requires"][0]
    assert SCENES[1]["Requires"][1] == RIVALRY_FLAG
    assert NATIVE_MEMORY_RECORD_VERIFIED in SCENES[1]["Requires"]
    assert active_path in SCENES[1]["Requires"] and ENTRY_READY in SCENES[1]["Requires"]
    assert any(path.endswith("Ending_AreeluSacrificeTrickster.jbp") for path in NATIVE_ENDING_VETO_MATRIX["hard_veto"])
    assert NATIVE_GRIEF_CONTEXT["source_cue"]["World/Dialogs/c6/SecondFloor/AreeluBurnTheWitch/Cue_0069.jbp"]
    assert NATIVE_CRADLE_MEMORY_SOURCE["projector_destroyed"][1] != ""
    assert NATIVE_MEMORY_STATE_CONTRACT["protected_result"] != NATIVE_MEMORY_STATE_CONTRACT["contested_result"]
    assert MEMORY_INTERVENTION_CONTRACT["protection_result"] != MEMORY_INTERVENTION_CONTRACT["loss_result"]
    _assert_memory_transitions()
    _assert_contact_gate()
    _assert_trickster_copy_test()
    _assert_field_scene()
    commit_flags = {
        flag for item in SCENES for node in item["Nodes"] for choice in node["Choices"] for flag in choice["Set"]
        if flag == RELATIONSHIP["CommittedFlag"]
    }
    assert commit_flags == {RELATIONSHIP["CommittedFlag"]}
    commitment_scene = next(item for item in SCENES if item["Id"].endswith("the_choice_after"))
    commitment_nodes = {node["Id"]: node for node in commitment_scene["Nodes"]}
    assert any(
        RELATIONSHIP["CommittedFlag"] in choice["Set"]
        for choice in commitment_nodes["choice_commit"]["Choices"]
    )
    assert all(
        RELATIONSHIP["CommittedFlag"] not in choice["Set"]
        for choice in commitment_nodes["choice_continue"]["Choices"]
    )


def _assert_memory_transitions():
    active_path = "areelu.trickster_opening.active_trickster_path"
    choices = [choice for item in SCENES for node in item["Nodes"] for choice in node["Choices"]]
    memory_choices = [choice for choice in choices if {MEMORY_PROTECTED, MEMORY_CONTESTED} & set(choice["Set"])]
    assert memory_choices
    for choice in memory_choices:
        set_flags = set(choice["Set"])
        assert not ({MEMORY_PROTECTED, MEMORY_CONTESTED} <= set_flags)
        assert {MEMORY_PROTECTED, MEMORY_CONTESTED} <= set(choice["Forbids"])
        if MEMORY_PROTECTED in set_flags:
            assert NATIVE_MEMORY_RECORD_VERIFIED in choice["Requires"]
        if MEMORY_CONTESTED in set_flags or "test_withdrawn" in choice["Set"]:
            action = "accept_risk" if MEMORY_CONTESTED in set_flags else "withdraw"
            assert set(MEMORY_CHOICE_EFFECTS[action]["Requires"]) <= set(choice["Requires"])

    valid = dict(
        current_trickster=True,
        entry_ready=True,
        areelu_agrees=True,
        native_answer_verified=True,
        answer_key="Answer_0013",
    )
    accepted = apply_memory_choice("accept_risk", **valid)
    assert accepted["outcome"] == "accept_risk"
    assert accepted["state"] == frozenset({MEMORY_CONTESTED})
    assert accepted["native_answer"] == valid["answer_key"] and accepted["annotation"]

    protected = apply_memory_choice("protect", **{**valid, "areelu_agrees": False})
    assert protected["state"] == frozenset({MEMORY_PROTECTED})
    assert apply_memory_choice("protect", **{**valid, "native_answer_verified": False})["outcome"] == "rejected_unverified_answer"
    withdrawn = apply_memory_choice("withdraw", **valid)
    assert withdrawn["state"] == frozenset({MEMORY_PROTECTED})

    assert apply_memory_choice("accept_risk", **{**valid, "current_trickster": False})["outcome"] == "rejected_ineligible"
    assert apply_memory_choice("accept_risk", **{**valid, "entry_ready": False})["outcome"] == "rejected_ineligible"
    assert apply_memory_choice("accept_risk", **{**valid, "native_answer_verified": False})["outcome"] == "rejected_unverified_answer"
    refusal = apply_memory_choice("accept_risk", **{**valid, "areelu_agrees": False})
    assert refusal["outcome"] == "areelu_refused" and not refusal["state"]
    declined = apply_memory_choice("accept_risk", **{**valid, "answer_key": "Answer_0016"})
    assert declined["outcome"] == "native_answer_declined" and not declined["state"]
    assert apply_memory_choice("protect", **{**valid, "answer_key": "Answer_0016"})["state"] == frozenset({MEMORY_PROTECTED})
    assert apply_memory_choice("accept_risk", **{**valid, "answer_key": "Answer_9999"})["outcome"] == "rejected_invalid_answer"

    repeated = apply_memory_choice("accept_risk", prior_state=accepted["state"], **valid)
    assert repeated["outcome"] == "rejected_already_final" and repeated["state"] == accepted["state"]
    contradictory = apply_memory_choice("protect", prior_state=(MEMORY_PROTECTED, MEMORY_CONTESTED), **valid)
    assert contradictory["outcome"] == "rejected_contradictory_prior"
    assert contradictory["state"] == frozenset({MEMORY_PROTECTED, MEMORY_CONTESTED})
    assert accepted["native_answer"] == "Answer_0013"
    consent_node = next(node for node in SCENES[1]["Nodes"] if node["Id"] == "consent_offer")
    test_agreed = "areelu.trickster_opening.areelu_test_agreed"
    assert all(test_agreed in choice["Set"] for choice in consent_node["Choices"])
    model_node = next(node for node in SCENES[1]["Nodes"] if node["Id"] == "model")
    assent_choice = next(choice for choice in model_node["Choices"] if choice["Next"] == "intervention_offer")
    safeguard_choice = next(choice for choice in next(node for node in SCENES[1]["Nodes"] if node["Id"] == "intervention_offer")["Choices"] if choice["Next"] == "consent_offer")
    assert {active_path, ENTRY_READY} <= set(assent_choice["Requires"])
    assert {active_path, ENTRY_READY} <= set(safeguard_choice["Requires"])
    off_path_flags = set(SCENES[1]["Requires"]) - {active_path}
    assert not _requirements_satisfied(SCENES[1]["Requires"], (), off_path_flags)
    on_path_flags = off_path_flags | {active_path}
    assert _requirements_satisfied(SCENES[1]["Requires"], (), on_path_flags)
    assert not _requirements_satisfied(assent_choice["Requires"], assent_choice["Forbids"], off_path_flags)
    assert not _requirements_satisfied(safeguard_choice["Requires"], safeguard_choice["Forbids"], off_path_flags)


def _assert_contact_gate():
    available = dict(
        native_revelations=True,
        au_acknowledged=True,
        current_trickster=True,
        areelu_alive=True,
        areelu_contactable=True,
    )
    assert resolve_contact_gate(**available)["invitation_available"]
    assert resolve_contact_gate(**{**available, "native_revelations": False})["outcome"] == "unavailable"
    assert resolve_contact_gate(**{**available, "au_acknowledged": False})["outcome"] == "unavailable"
    assert resolve_contact_gate(**{**available, "current_trickster": False})["outcome"] == "unavailable"
    assert resolve_contact_gate(**{**available, "areelu_contactable": False})["outcome"] == "unavailable"
    dead_path = next(iter(NATIVE_ENDING_VETO_MATRIX["hard_veto"]))
    assert resolve_contact_gate(**available, active_endings=(dead_path,))["outcome"] == "native_conflict"
    child_identification_cue = next(iter(NATIVE_GRIEF_CONTEXT["source_cue"]))
    cue_context = resolve_contact_gate(**available, seen_cues=(child_identification_cue,))
    assert cue_context["invitation_available"] and cue_context["grief_context_seen"]
    hold_path = next(iter(NATIVE_ENDING_VETO_MATRIX["hold_for_living_contact_proof"]))
    assert resolve_contact_gate(
        **{**available, "areelu_alive": False}, active_endings=(hold_path,)
    )["outcome"] == "living_contact_unproven"

    accepted = apply_contact_reply(invitation_available=True, areelu_accepts=True)
    declined = apply_contact_reply(invitation_available=True, areelu_accepts=False)
    assert accepted["state"] == frozenset({CONTACT_ACCEPTED})
    assert declined["state"] == frozenset({CONTACT_DECLINED})
    assert apply_contact_reply(
        prior_state=accepted["state"], invitation_available=True, areelu_accepts=False
    )["outcome"] == "rejected_already_final"
    assert apply_contact_reply(
        prior_state=(CONTACT_ACCEPTED, CONTACT_DECLINED), invitation_available=True, areelu_accepts=True
    )["outcome"] == "rejected_contradictory_prior"
    assert apply_contact_reply(invitation_available=False, areelu_accepts=True)["outcome"] == "rejected_unavailable"
    accepted_contact_flags = {ENTRY_READY}
    assert not _requirements_satisfied(SCENES[0]["Requires"], (), accepted_contact_flags)
    accepted_contact_flags.add("areelu.trickster_opening.active_trickster_path")
    assert _requirements_satisfied(SCENES[0]["Requires"], (), accepted_contact_flags)


def _assert_field_scene():
    scene4 = next(item for item in SCENES if item["Id"].endswith("the_live_fold"))
    active_path = "areelu.trickster_opening.active_trickster_path"
    assert {ENTRY_READY, active_path, RIVALRY_FLAG, "areelu.trickster_opening.second_question_open"} <= set(scene4["Requires"])
    aftermath = next(node for node in scene4["Nodes"] if node["Id"] == "field_aftermath")
    interest_choice = next(choice for choice in aftermath["Choices"] if choice["Next"] == "field_interest_offer")
    professional_choice = next(choice for choice in aftermath["Choices"] if choice["Next"] == "field_professional")
    interest_flag = "areelu.trickster_opening.commander_interest_stated"
    withdrawal_flag = "areelu.trickster_opening.interest_withdrawn"
    assert interest_flag in interest_choice["Requires"]
    assert withdrawal_flag in interest_choice["Forbids"]
    assert not _requirements_satisfied(interest_choice["Requires"], interest_choice["Forbids"], {interest_flag, withdrawal_flag})
    assert _requirements_satisfied(interest_choice["Requires"], interest_choice["Forbids"], {interest_flag})
    assert not _requirements_satisfied(professional_choice["Requires"], professional_choice["Forbids"], {interest_flag})
    assert _requirements_satisfied(professional_choice["Requires"], professional_choice["Forbids"], set())
    offer = next(node for node in scene4["Nodes"] if node["Id"] == "field_interest_offer")
    assert all("areelu.trickster_opening.areelu_desire_admitted" in choice["Set"] for choice in offer["Choices"])


def _requirements_satisfied(requires, forbids, flags):
    flags = set(flags)
    return set(requires) <= flags and not (set(forbids) & flags)


def _assert_trickster_copy_test():
    choices = [choice for item in SCENES for node in item["Nodes"] for choice in node["Choices"]]
    choice = next(choice for choice in choices if TRICKSTER_METHOD_FLAG in choice["Set"])
    assert set(TRICKSTER_COPY_CHOICE["Set"]) <= set(choice["Set"])
    assert set(TRICKSTER_COPY_CHOICE["Requires"]) <= set(choice["Requires"])
    assert set(TRICKSTER_COPY_CHOICE["Forbids"]) <= set(choice["Forbids"])
    result = apply_trickster_copy_choice(current_trickster=True, page_is_native=False)
    assert result["outcome"] == "contradiction_demonstrated"
    assert result["native_history_changed"] is False and result["annotation"]
    assert apply_trickster_copy_choice(current_trickster=False, page_is_native=False)["outcome"] == "rejected_ineligible"
    assert apply_trickster_copy_choice(current_trickster=True, page_is_native=True)["outcome"] == "rejected_native_source"
    repeated = apply_trickster_copy_choice(
        prior_state=result["state"], current_trickster=True, page_is_native=False
    )
    assert repeated["outcome"] == "rejected_already_final"
    assert repeated["native_history_changed"] is False


def _assert_route_expansion():
    expected = {
        "areelu_trickster_opening.the_inventory",
        "areelu_trickster_opening.the_reply",
        "areelu_trickster_opening.the_second_graft",
        "areelu_trickster_opening.the_private_hour",
        "areelu_trickster_opening.the_open_record",
        "areelu_trickster_opening.the_unmeasured_answer",
    }
    by_id = {item["Id"]: item for item in SCENES}
    assert expected <= by_id.keys()
    current_path = "areelu.trickster_opening.active_trickster_path"
    for item in SCENES:
        assert current_path in item["Requires"]
    assert "areelu.trickster_opening.inventory_complete" in by_id[
        "areelu_trickster_opening.the_reply"
    ]["Requires"]
    assert "areelu.trickster_opening.relationship_started" in by_id[
        "areelu_trickster_opening.the_second_graft"
    ]["Requires"]
    private = by_id["areelu_trickster_opening.the_private_hour"]
    assert "areelu.trickster_opening.graft_scene_complete" in private["Requires"]
    assert "areelu.trickster_opening.relationship_paused" in private["Forbids"]
    assert "areelu.trickster_opening.private_scene_complete" in by_id[
        "areelu_trickster_opening.the_open_record"
    ]["Requires"]
    choices = [choice for item in SCENES for node in item["Nodes"] for choice in node["Choices"]]
    assert any("areelu.trickster_opening.inventory_complete" in choice["Set"] for choice in choices)
    assert any("areelu.trickster_opening.relationship_started" in choice["Set"] for choice in choices)
    assert any("areelu.trickster_opening.graft_scene_complete" in choice["Set"] for choice in choices)
    unmeasured = by_id["areelu_trickster_opening.the_unmeasured_answer"]
    assert unmeasured["Nodes"][0]["Id"] == "unmeasured_entry"
    assert "areelu.trickster_opening.relationship_started" in unmeasured["Requires"]
    assert "areelu.trickster_opening.unmeasured_scene_complete" in by_id[
        "areelu_trickster_opening.the_choice_after"
    ]["Requires"]
    gate_nodes = {node["Id"]: node for node in by_id[
        "areelu_trickster_opening.the_residual_gate"]["Nodes"]}
    bargain = next(choice for choice in gate_nodes["gate_aftermath"]["Choices"]
                   if choice["Next"] == "gate_power_bargain")
    assert not _requirements_satisfied(bargain["Requires"], bargain["Forbids"], ())
    assert _requirements_satisfied(bargain["Requires"], bargain["Forbids"], f("gate_closed_by_trickster"))
    assert f("private_research_pact")[0] in gate_nodes["gate_power_bargain"]["Choices"][0]["Set"]
    future_nodes = {node["Id"]: node for node in by_id[
        "areelu_trickster_opening.the_choice_after"]["Nodes"]}
    power_future = next(choice for choice in future_nodes["choice_entry"]["Choices"]
                        if choice["Next"] == "choice_power_future")
    assert not _requirements_satisfied(power_future["Requires"], power_future["Forbids"], f("relationship_started"))
    assert _requirements_satisfied(power_future["Requires"], power_future["Forbids"],
                                   f("relationship_started", "private_research_pact"))
    assert not _requirements_satisfied(power_future["Requires"], power_future["Forbids"],
                                       f("relationship_started", "private_research_pact", "relationship_ended"))


def _walk_selected(start, initial_flags, scenes=None):
    """Traverse actual choices and scheduled followups with their live predicates."""
    items = scenes or SCENES
    by_scene = {item["Id"]: item for item in items}
    by_node = {node["Id"]: (item, node) for item in items for node in item["Nodes"]}
    relevant = {flag for item in items for flag in (*item["Requires"], *item["Forbids"])}
    relevant.update(flag for _, node in by_node.values() for choice in node["Choices"]
                    for flag in (*choice["Requires"], *choice["Forbids"]))
    relevant.update(f("year_end_relationship_closed", "relationship_ended", "relationship_paused"))
    pending = [(start, frozenset(initial_flags))]
    visited = set()
    while pending:
        key, flags = pending.pop()
        state = (key, flags & relevant)
        if state in visited:
            continue
        visited.add(state)
        item, node = by_node[key]
        choices = [choice for choice in node["Choices"]
                   if _requirements_satisfied(choice["Requires"], choice["Forbids"], flags)]
        assert choices, (key, "no available choices")
        yield key, flags, choices
        for choice in choices:
            if choice["Abort"]:
                continue
            updated = flags | frozenset(choice["Set"])
            check = choice.get("Check") or {}
            targets = [check["Success"], check["Failure"]] if check else [choice.get("Next")]
            for target in targets:
                if target:
                    pending.append((target, updated))
                else:
                    for flag in choice["Set"]:
                        scene_id = FOLLOWUP_SCENES.get(flag)
                        if scene_id in by_scene:
                            followup = by_scene[scene_id]
                            assert followup["DelayHours"] > 0
                            if _requirements_satisfied(followup["Requires"], followup["Forbids"], updated):
                                pending.append((followup["Nodes"][0]["Id"], updated))


def _assert_final_outcomes():
    endings = [item for item in SCENES if item["Id"].startswith("areelu_trickster_opening.the_choice_after")]
    ending = endings[0]
    outcomes, breakup_seen = set(), False
    for previous in ((), f("relationship_committed"), f("private_research_pact"),
                     f("relationship_committed", "private_research_pact")):
        initial = (*ending["Requires"], *f("relationship_started"), *previous)
        for key, flags, choices in _walk_selected(ending["Nodes"][0]["Id"], initial, endings):
            origin = NODE_ORIGINS[key]
            if origin == "choice_last_page":
                assert len(choices) == 1
                choice = choices[0]
                outcome = choice["Next"]
                if outcome:
                    outcome = NODE_ORIGINS[outcome]
                elif f("scheduled.choice_ordinary_future")[0] in choice["Set"]:
                    outcome = "choice_ordinary_future"
                outcomes.add(outcome)
                if f("year_end_relationship_closed")[0] in flags:
                    breakup_seen = True
                    assert outcome == "choice_closed_future"
    assert breakup_seen
    assert outcomes == {"choice_ordinary_future", "choice_open_future", "choice_paused_future", "choice_closed_future"}
    physical = next(item for item in SCENES if item["Id"].endswith("the_unmeasured_answer"))
    assert physical["Remote"] is False


def _assert_choice_semantics():
    by_node = {node["Id"]: (item, node) for item in SCENES for node in item["Nodes"]}

    def selected(source, fragment, extra=()):
        item, node = by_node[source]
        choice = next(choice for choice in node["Choices"] if fragment in choice["Text"])
        flags = frozenset((*item["Requires"], *extra, *choice["Requires"], *choice["Set"]))
        starts = [choice["Next"]] if choice["Next"] else []
        for flag in choice["Set"]:
            scene_id = FOLLOWUP_SCENES.get(flag)
            if scene_id:
                starts.append(next(item["Nodes"][0]["Id"] for item in SCENES if item["Id"] == scene_id))
        result = set()
        for start in starts:
            result.update(NODE_ORIGINS[key] for key, _, _ in _walk_selected(start, flags))
        return result

    # These assertions follow the selected answer, not every edge from its menu.
    leave = selected("private_kiss", "Stop and leave")
    assert "private_departure" in leave and "private_after" not in leave
    limited = selected("private_kiss", "kiss is enough")
    assert "private_kiss_only" in limited and "private_after" not in limited
    waiting = selected("reply_terms", "wait before touching")
    assert "reply_no_touch" in waiting and "reply_touch" not in waiting
    dinner = selected("returned_future", "Decline tonight")
    assert "returned_declined_dinner" in dinner and "returned_final_meeting" not in dinner
    no_touch = selected("returned_final_meeting", "without touching")
    assert "returned_no_touch" in no_touch and "returned_after_review" not in no_touch
    for source, label in (("returned_receipt", "Close the personal"),
                          ("returned_aftercare", "End the romance"),
                          ("returned_final_meeting", "no further personal")):
        ended = selected(source, label)
        assert "returned_nonromantic" in ended
        assert not ended & {"returned_after_walk", "returned_final_meeting", "returned_after_review", "returned_long_term"}
    ended = selected("copy_revisit", "Close the personal")
    assert "copy_end" in ended and "copy_second_contact" not in ended
    nonphysical = selected("copy_revisit", "nonphysical")
    assert "copy_nonphysical" in nonphysical
    assert not nonphysical & {"copy_second_contact", "copy_long_term"}
    apart = selected("choice_month_later", "Leave her to work", f("relationship_started", "relationship_committed", "relationship_ending_committed"))
    assert "choice_day_apart" in apart and "choice_shared_space" not in apart

    quiet = selected("unmeasured_wants", "keep the evening nonsexual")
    assert "unmeasured_touch" in quiet and "unmeasured_after" in quiet
    assert not quiet & {"unmeasured_night", "unmeasured_morning"}
    for source, label in (("unmeasured_kiss", "kiss is enough"),
                          ("unmeasured_kiss", "leave now"),
                          ("unmeasured_night", "your own room")):
        leaving = selected(source, label)
        assert "unmeasured_after" in leaving and "unmeasured_morning" not in leaving
    staying = selected("unmeasured_night", "until morning")
    assert "unmeasured_morning" in staying and "unmeasured_after" in staying
    night_writers = {NODE_ORIGINS[node["Id"]] for _, node in by_node.values()
                     if any(f("unmeasured_night_shared")[0] in choice["Set"] for choice in node["Choices"])}
    assert night_writers == {"unmeasured_morning"}
    morning = next(item for item in SCENES if item["Nodes"][0]["Id"] == "unmeasured_morning")
    assert f("scheduled.unmeasured_morning")[0] in morning["Requires"] and morning["DelayHours"] == 8
    assert not any(f("scheduled.unmeasured_morning")[0] in choice["Set"]
                   for _, node in by_node.values() if NODE_ORIGINS[node["Id"]] in quiet
                   for choice in node["Choices"])
    for guarded in ("returned_entry", "copy_entry", "gate_entry"):
        assert next(item for item in SCENES if any(node["Id"] == guarded for node in item["Nodes"]))["Nodes"][0]["Id"] == guarded

    private = selected("inventory_terms", "private counterledger")
    assert "inventory_private_consequence" in private and "inventory_consequence" not in private
    reply = next(item for item in SCENES if item["Nodes"][0]["Id"] == "reply_entry")
    private_reply = {NODE_ORIGINS[key] for key, _, _ in _walk_selected(
        "reply_entry", (*reply["Requires"], *f("inventory_private_record")))}
    assert "reply_private_findings" in private_reply and "reply_public_findings" not in private_reply

    copy_scene = next(item for item in SCENES if item["Nodes"][0]["Id"] == "copy_entry")
    protected = {NODE_ORIGINS[key] for key, _, _ in _walk_selected(
        "copy_entry", (*copy_scene["Requires"], MEMORY_PROTECTED))}
    assert "copy_protected_entry" in protected and "copy_contested_entry" not in protected
    for key in protected:
        text = next(node["Text"] for _, node in by_node.values() if node["Id"] == key)
        assert "risk you knowingly accepted" not in text
        assert "contradiction you made" not in text

    unresolved = selected("gate_withdraw", "", f("relationship_started"))
    assert "gate_unresolved_followup" in unresolved
    assert not unresolved & {"gate_followthrough", "gate_residents_revisit", "gate_archive_kept", "gate_ordinary_marker"}
    ordinary = selected("gate_ground", "", f("relationship_started"))
    assert "gate_archive_kept" in ordinary and "gate_ordinary_marker" in ordinary
    assert not ordinary & {"gate_followthrough", "gate_residents_revisit", "gate_unresolved_followup"}
    spent = selected("gate_closed_trickster", "", f("relationship_started", "gate_anchor_spent"))
    assert "gate_followthrough" in spent and "gate_residents_revisit" in spent
    assert not spent & {"gate_archive_kept", "gate_ordinary_marker", "gate_unresolved_followup"}

    for item in SCENES:
        for node in item["Nodes"]:
            text = node["Text"]
            assert not any(leak in text for leak in (
                "The game can store", "penalty in the story", "campaign has an ending", "ending state",
                "relationship state", "The ending does not say", "The ending preserves"))
            assert not any(jump in text for jump in (
                "A month passes", "A month later", "Several months later", "next winter",
                "At the end of the year", "spent a year", "A month into"))
    for flag, scene_id in FOLLOWUP_SCENES.items():
        followup = next(item for item in SCENES if item["Id"] == scene_id)
        assert flag in followup["Requires"]
        assert followup["DelayHours"] == FOLLOWUP_DELAYS[NODE_ORIGINS[followup["Nodes"][0]["Id"]]]
        assert any(flag in choice["Set"] and choice["Next"] is None
                   for item in SCENES for node in item["Nodes"] for choice in node["Choices"])


if __name__ == "__main__":
    _assert_graph()
    _assert_memory_transitions()
    _assert_contact_gate()
    _assert_field_scene()
    _assert_trickster_copy_test()
    _assert_route_expansion()
    _assert_final_outcomes()
    _assert_choice_semantics()
    print(f"{len(SCENES)} unintegrated scenes; {sum(len(s['Nodes']) for s in SCENES)} nodes; topology valid")

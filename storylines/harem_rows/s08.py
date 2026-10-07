"""S08 staging; authored renunciation, not native liberation or a drain cure.

The reviewed A sheet explicitly blocks emission until its DC, remaining favour,
and authenticated reply contract are supplied. These drafts preserve its IDs
and answer positions for coordinator review; register deliberately emits none.
No new echo, return, relationship terms, intimacy or native rewrite is supplied.
"""
from story_format import c, n, scene
from storylines import household


PREFIX = "household.pair.arueshalae_nocticula."
NATIVE_CUE = "5cef950cacdd67c48866a2cb92517f0e"
NATIVE_SEEN = PREFIX + "kneeling_seen"
BLOCKERS = (
    "A.S08.4: approved numeric CheckDiplomacy Tier-3 DC is absent",
    "A.S08.4: approved remaining-favour producer, availability and debit are absent",
    "A.S08.2/11: one protected outcome's authenticated reply timing is unresolved",
    "A.common: pending failure versus first-wins enmity needs owner reconciliation",
)


def P(suffix):
    return PREFIX + suffix


# Witness recipes for the shared controller, never attitude/enmity writes.
LADDER = {
    ("arueshalae", "nocticula", "respect"): [
        P("resolved"), P("nocticula_rank_answered"), P("cost.nocticula_claim_limited")],
    ("nocticula", "arueshalae", "respect"): [
        P("resolved"), P("arueshalae_renounced"), P("cost.arueshalae_public_defiance")],
}

COMMON_REQUIRES = (
    "trickster", "trickster.now", household.PAGE_TAKEN, household.STANCE_ELIGIBLE,
    household.KEPT, "arueshalae.harem.eligible", "nocticula.harem.eligible",
    "arueshalae.present_now", "nocticula.reachable_by_letter",
    "noct.acq.renewed_agreement", "noct.acq.seal_received",
    "noct.acq.an_answer_of_her_own_done",
)
COMMON_FORBIDS = (
    "fool_king.gone", "trickster.failed", "noct.closed", "noct.acq.closed",
    # Threshold's earned return cannot override the Ch5 correspondence silence.
    "noct.acq.council_fight", "arueshalae.closed",
    "arueshalae.epoch_unavailable", "nocticula.epoch_unavailable",
    P("resolved"), P("permanent_refusal"),
    household.enmity("arueshalae", "nocticula"),
    household.enmity("nocticula", "arueshalae"),
)
CHANNEL_GROUPS = (
    ("noct.acq.channel_provisional",),
    ("noct.acq.channel_letters_only",),
)


def _terminal_flags(step, held=False, failed=False):
    flags = [P(step + ".seen")]
    if held:
        flags.extend([P("resolved"), P("arueshalae_renounced"),
                      P("nocticula_rank_answered"), P("cost.arueshalae_public_defiance"),
                      P("cost.nocticula_claim_limited")])
    elif failed:
        flags.append(P("settle.failed"))
    else:
        flags.extend([P("permanent_refusal"), P("unsettled")])
    return flags


def draft_scenes():
    """Review-only templates. Null DC and unpaid favour make them NON-EXPORTABLE.

    No registration helper is called here: reviewing drafts spends no allowance,
    registers no foresight consumer, and mutates no shared module or payload.
    """
    result = []
    for step in ("settle", "retry"):
        for branch in ("redeemed", "corrupted"):
            fallen = branch == "corrupted"
            renunciation = (
                '"Write this down. Arueshalae. Not her pet, not her escaped property. '
                'If she wants me kneeling, she can come and try."' if fallen else
                '"I want her to hear my name without an order attached to it. '
                'Arueshalae. I will speak to her. I will not kneel."')
            reaction = (
                '"Lady in Shadow. I can say it without crawling."' if fallen else
                '"Lady in Shadow, then. She has no claim on the life I choose here."')
            start = (
                '{n}A scout sets a bloodstained map beside the cups. Arueshalae moves it '
                'clear of the lamp and lays a sheet beside the Commander’s wrapped half-seal. '
                'The soldiers waiting for their orders can hear her.{/n}\n' + renunciation)
            if step == "retry":
                start = (
                    '{n}Fresh reports from the Worldwound cover the Table. Arueshalae lays '
                    'the unanswered renunciation beside them. She has not changed its wording.{/n}\n'
                    + renunciation)
            choices = []
            if step == "settle":
                choices.append(c('[Present her renunciation and acknowledge the queen’s rank.]',
                                 check=dict(Skill="CheckDiplomacy", DC=None,
                                            Success="held", Failure="failed")))
            # Reserved sheet answer. It must receive the approved existing favour
            # guards and debit before ANY of these templates can be exported.
            choices.extend([c('[Call in the remaining Nocticula favour.]', "held"),
                            c('"Then leave the claim disputed."', "refused"),
                            c('[Later.]', abort=True)])
            nodes = [
                n("start", "Arueshalae", start, *choices, portrait="Arueshalae"),
                n("held", "Narrator",
                  '{n}Nocticula’s answering stroke completes the broken seal. You read the '
                  'reply aloud over the map.{/n}\n'
                  '"Arueshalae. Your little audience may keep its soldier. Do not mistake '
                  'that for permission to spit on my throne. You will address me as Lady in Shadow."\n'
                  '{n}The signature bites through the paper. No summons follows it.{/n}',
                  c('Continue', "answer"), portrait="Nocticula"),
                n("answer", "Arueshalae", reaction + '\n'
                  '{n}She signs beneath her own name and slides the scout’s map back into the light.{/n}',
                  c('Continue', flags=_terminal_flags(step, held=True)), portrait="Arueshalae"),
                n("refused", "Arueshalae",
                  ('"Then she can choke on the claim. I have fighting to do."' if fallen else
                   '"It can remain disputed. I am staying with the crusade."') + '\n'
                  '{n}She takes her sheet away. The half-seal remains wrapped; no answer has been requested.{/n}',
                  c('Continue', flags=_terminal_flags(step)), portrait="Arueshalae"),
            ]
            if step == "settle":
                nodes.append(n("failed", "Narrator",
                               '{n}The answering stroke completes the seal. Beneath the copied '
                               'renunciation, Nocticula has written a single line.{/n}\n'
                               '"My subject has learned to dictate. You have learned to repeat her. '
                               'Neither has given me a reason to accept this insolence."\n'
                               '{n}Arueshalae snatches the sheet back. Her name remains above the reply.{/n}',
                               c('Continue', flags=_terminal_flags(step, failed=True)), portrait="Nocticula"))
            requires = COMMON_REQUIRES + ("arueshalae." + branch,)
            forbids = COMMON_FORBIDS + (P(step + ".seen"),)
            if not fallen:
                forbids += ("arueshalae.corrupted",)
            if step == "retry":
                requires += (P("settle.failed"),)
            result.append(scene(
                P(step + "." + branch), "A name without kneeling", "Arueshalae", 5,
                '[Arueshalae’s renunciation]' if step == "settle" else '[The disputed claim]',
                nodes, requires=requires, forbids=forbids, delay=48 if step == "retry" else 0,
                last=5, Relationship="household", Chapters=[5], Areas=[household.DREZEN],
                InteractionHub=household.TABLE_HUB, Participants=["arueshalae"],
                Pair=["arueshalae", "nocticula"], RestAllowance="household.protected",
                HouseholdCategory="protected", HouseholdWitness=P(step + ".seen"),
                RequiresAnyGroups=[list(g) for g in CHANNEL_GROUPS],
                ForbidOverrides={household.enmity(a, b): a + ".harem.reconciled." + b
                                 for a, b in (("arueshalae", "nocticula"), ("nocticula", "arueshalae"))}))
    return result


def register(payload, scenes, refs):
    """Keep unresolved sheet inputs inert; never ship a free favour or guessed DC."""
    if BLOCKERS:
        return
    # Removing the blocker list alone must not activate incomplete templates.
    raise ValueError("S08 requires approved contracts and final registration before emission")

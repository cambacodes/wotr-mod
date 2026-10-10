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


NOCT_HELD = {'settle': '{n}The half-seal warms through its wrapping before anyone touches it. The answering mark crawls out across the sheet, under Arueshalae\'s name, in a hand the whole Table can read.{/n} "Arueshalae. So the girl has a name now, and says it to my face in front of soldiers. How brave. How very mortal of her." {n}The mark stops, the way a cat stops with one paw still on the mouse.{/n} "I am the Lady in Shadow, girl, and I do not need you on your knees to remain so. Keep your little life among the crusaders. I shall not summon you, and I shall not send for you. But every succubus in my city will know that you walked out of my service and that I let you, and they will wonder what you paid for it. Let them wonder. It will cost you more than kneeling would have."', 'retry': '{n}This time the half-seal is warm before the sheet is even unfolded, as if it had been waiting. The mark writes under Arueshalae\'s name without hurrying.{/n} "Again, and louder. Very well, girl: Arueshalae. There, I have said it, in my own hand, where the whole Table can read it." {n}A pause, long enough to be insulting.{/n} "I am the Lady in Shadow, and I do not need you on your knees to remain so. Keep your little life among the crusaders. I shall not summon you, and I shall not send for you. But every succubus in my city will know that you walked out of my service and that I let you, and they will wonder what you paid. Let them wonder. It will cost you more than kneeling would have."'}
NOCT_FAILED = '{n}The half-seal stays cold for an hour. Then the sheet comes back folded, sealed with her mark pressed so hard the wax has split, and inside, under Arueshalae\'s renunciation, one stroke through the whole of it.{/n} "Mine. Come home on your knees, girl, or do not come home at all; but do not send me paper telling me what you are."'
ARUE_START = {'settle': '{n}Arueshalae unrolls the crusade map across the Table with both hands and puts one claw through the black blot that is Alushinyrra.{/n} "Say it for her, darling, out loud, since she has a seal on your table now. \'Arueshalae. Of nobody\'s house.\' Not hers. Not Vellexia\'s. Not yours, either, before you get ideas." {n}She smiles at the seal as if it could see her, and her wings are pressed flat against her back.{/n} "I bowed to her my whole life, because that is what one does. I worship one god now. She is standing here, and she is hungry, and she does not kneel."', 'retry': '"Again, darling? You are stubborn." {n}She flattens the map with the heel of her hand, over the old claw-mark.{/n} "Louder, then. \'Arueshalae. Of nobody\'s house.\' Let the seal hear it twice."'}
ARUE_ANSWER = '"She said my name." {n}She laughs, low and delighted, and does not quite stop her hands from shaking.{/n} "Our Lady in Shadow said my name, and not \'my succubus\'. Do you know how few of her creatures have heard that and lived to sulk about it?" {n}She signs under the queen\'s line with one claw, through the paper and into the wood of the Table.{/n} "Arueshalae. Mine. She can keep the rest of the city. I\'ve had all of it I want."'
ARUE_REFUSED = '"Then leave it." {n}She rolls the map up, quick and neat, before anyone can see where her claw went in.{/n} "Let her think she owns me. Let her come and collect, if she likes. I\'d rather be hunted by a queen than pardoned by one; at least the hunt is interesting." {n}She drops the map on the Table.{/n} "Now feed me something. Defiance makes me hungry."'


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
                '"I want her to hear my name without an order attached to it. '
                'Arueshalae. I will speak to her. I will not kneel."')
            reaction = (
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
                n("start", "Arueshalae", (ARUE_START[step] if fallen else start), *choices, portrait="Arueshalae"),
                n("held", "Narrator",
                  NOCT_HELD[step],
                  c('Continue', "answer"), portrait="Nocticula"),
                n("answer", "Arueshalae", (ARUE_ANSWER if fallen else reaction + '\n'
                  '{n}She signs beneath her own name and slides the scout’s map back into the light.{/n}'),
                  c('Continue', flags=_terminal_flags(step, held=True)), portrait="Arueshalae"),
                n("refused", "Arueshalae",
                  (ARUE_REFUSED if fallen else '''"It can remain disputed. I am staying with the crusade."
{n}She takes her sheet away. The half-seal remains wrapped; no answer has been requested.{/n}'''),
                  c('Continue', flags=_terminal_flags(step)), portrait="Arueshalae"),
            ]
            if step == "settle":
                nodes.append(n("failed", "Narrator",
                               NOCT_FAILED,
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

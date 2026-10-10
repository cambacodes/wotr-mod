"""S44: authored wrestling escape; native recognition does not establish ownership.

Sources: HAREM-SHEETS-42-47, row 44; harem-lore-check, shared corrections/S44.
The fallen F->R extension is reserved, not enabled: its reviewed branch ceiling
must be installed by the registry owner first (WAVE-PLAN W3-S44.evil).
This row writes incident witnesses only. The integrator owns attitude/enmity.
"""
from story_format import c, n
from storylines import household

P = "household.pair.shamira_arueshalae."
PAIR = ("shamira", "arueshalae")
SUCCESS = ("shamira_released", "arueshalae_ornament_returned",
           "claim.name_relinquished", "cost.shamira_public_release",
           "cost.arueshalae_trophy_yielded")
REQUIRES = ("shamira.trickster.embodied", "shamira.trickster.game_proposed",
            "shamira.present_now", "arueshalae.present_now")
FORBIDS = ("fool_king.gone", "trickster.failed", "shamira.closed",
           "shamira.trickster.cost.kept_captive", "shamira.trickster.cast_out",
           "shamira.trickster.ally", "shamira.killed", "shamira.epoch_unavailable",
           "arueshalae.closed", "arueshalae_dead", "arueshalae.evil_dead",
           "arueshalae.kicked_out", "arueshalae.kicked_out_evil",
           "arueshalae.plot_absent", "arueshalae.epoch_unavailable")

# Reserved cut node: no export or intimacy eligibility before the ceiling review.
# Slot supplies no answer, flag, ward or attraction. The future committing
# warded[0] answer must spend the scroll/apply the ward before reaching this cut.
EXPLICIT_SLOT = n("household.pair.shamira_arueshalae.choice.explicit.1", "Narrator",
    """{n}Shamira catches Arueshalae by the waist. Arueshalae pulls her closer by the borrowed coat, laughing against her mouth. The chapel reader's ward has seven minutes left; they leave the cushions where they fall.{/n}""")


def later():
    return c("[Later.]", abort=True)


def terminal(step, node, text, suffixes, answer="[Clear the landing.]"):
    return n(node, "Narrator", text,
             c(answer, flags=tuple(P + f for f in (step + ".seen",) + suffixes)), later())


def nodes(evil, retry=False):
    name = '"Arueshalae. Say it. I am not one of your pets."' if evil else (
        '"My name is Arueshalae. I will show you the escape. I will not answer as someone else\'s creature."')
    opening = """{n}The Fool King's upper landing overlooks soldiers drinking before their next march to the Worldwound. Shamira removes a loose bracelet and sets it beside the rail.{/n}
"One of my queen's creatures will demonstrate an escape. I shall test the grip myself."
{n}Arueshalae answers without lowering her wing.{/n}
""" + name + '''
{n}Arueshalae spreads one wing. Shamira studies the angle, then reaches for the bracelet again.{/n}
"Show me, then. This body was grown in a garden for a customer who never paid. I want to know whether it can break a hold before somebody at my court finds out that it cannot."
'''
    if not evil:
        opening += '"Over the coat," {n}Arueshalae says, drawing the cloth over her wrist.{/n} "I still hunger. This is a hold, not a feeding."'
    else:
        opening += '"Over the coat. Unless you mean to feed me?" {n}Arueshalae bares her teeth. Shamira gives her a cold look and holds out the covered wrist.{/n}'
    success = """{n}Arueshalae indicates the turn of the wing and the wrist. The bracelet will slip if Shamira follows it. Below, a soldier bangs an empty cup against the table.{/n}
"I can keep the hold," {n}Shamira says.{/n} "Or let her finish it."
"And I can keep what falls out of your hand," {n}Arueshalae answers.{/n}
""" + ('"It would look delicious on me."' if evil else '"But I came to show you how to escape, not to take a trophy."')
    # Work remains proposed through each result node. Only its terminal answer
    # enacts the two independent deeds; Abort never preserves a deed for free.
    close = ('[Clear the landing. Shamira opens her grip: "Arueshalae, then." '
             'Arueshalae slips free and returns the fallen bracelet.]')
    if retry:
        return [n("start", "Narrator", opening + """
{n}The failed landing has been cleared. A pile of cushions lies beside the rail; Shamira points at you rather than offering her wrist yet.{/n}
"You first, Commander. I have seen enough of your catching.\"""",
            c("[Do the padded demonstration myself.]", "kept"),
            c('"Leave the claim unanswered."', "refused"), later()),
            terminal("retry", "kept", success + """
{n}The padding is ready. You will take the first slow tumble, with the soldiers watching, before the two women attempt the escape.{/n}""",
                ("retry.done",) + SUCCESS + ("cost.commander_demonstration",),
                close.replace("Clear the landing.", "Finish the padded demonstration.")),
            terminal("retry", "refused", '"Then I keep my claim," {n}Shamira says.{/n} "She was my city\'s before she was anybody\'s." {n}Arueshalae folds her wings and leaves the bracelet untouched.{/n}',
                ("retry.declined", "claim.unsettled"), "[Finish.]" )]
    return [n("start", "Narrator", opening + """
{n}The narrow landing leaves little room to catch a falling body. There are cushions downstairs, but fetching them means helping the demonstrator drag them up — and taking the first tumble yourself.{/n}""",
        c("[Keep the landing clear while they try the hold.]", check=dict(
            Skill="SkillAthletics", DC=26, Success="held", Failure="fell")),
        c("[Fetch the padding and take the slow demonstration.]", "padded"),
        c('"No court games tonight."', "declined"), later()),
        terminal("settle", "held", success, ("settle.done",) + SUCCESS, close),
        terminal("settle", "padded", success + """
{n}You will carry the cushions upstairs and take the first tumble. The soldiers below have already begun making wagers on your dignity.{/n}""",
            ("settle.done",) + SUCCESS + ("cost.commander_demonstration",),
            close.replace("Clear the landing.", "Carry the padding and take the first tumble.")),
        terminal("settle", "fell", """{n}Your foot slips on spilled beer. Arueshalae draws back before taking the hold; Shamira closes her fingers over the bracelet.{/n}
"No. I am not breaking my neck for your tavern.\"""",
            ("settle.failed", "landing_stopped")),
        terminal("settle", "declined", '"A pity," {n}Shamira says.{/n} "I had girls flayed for less than walking out of my court, little bird. You were always lucky." {n}Arueshalae looks at the bracelet, then back at her.{/n} "Keep it. And keep your hands off my name."',
            ("settle.declined", "claim.unsettled"))]


def register(payload, scenes, refs):
    """Register once, through the Table; household.integrate emits the entries.

    Register the sheet's engine-evaluated respect declarations, never choice
    writes to attitude. Only claim.unsettled
    (the two explicit refusal terminals), never settle.failed, is the final
    unresolved input owed to the shared first-wins implementation.
    """
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, PAIR[::-1]):
        for flag in (a + ".harem.enmity." + b, a + ".harem.reconciled." + b):
            if flag not in pending:
                pending.append(flag)
    derived = payload.setdefault("Derived", {})
    suppressed = []
    for a, b in (PAIR, PAIR[::-1]):
        key = P + "suppressed." + a
        derived[key] = [[a + ".harem.enmity." + b]]
        payload.setdefault("DerivedForbids", {})[key] = [a + ".harem.reconciled." + b]
        suppressed.append(key)
    for key, witnesses in {
        "arueshalae.harem.attitude.shamira.respect": ["shamira_released", "cost.shamira_public_release"],
        "shamira.harem.attitude.arueshalae.respect": ["arueshalae_ornament_returned", "cost.arueshalae_trophy_yielded"],
    }.items():
        derived[key] = [[P + flag for flag in witnesses]]
        payload.setdefault("DerivedForbids", {})[key] = list(suppressed)
    women = payload.setdefault("SeatWomen", {})
    for woman in PAIR:
        women.setdefault(woman, dict(Relationship=woman,
            Requires=[woman + ".present_now"],
            UnavailableFlags=[f for f in FORBIDS if f.startswith((woman + ".", woman + "_"))],
            UnavailableOverrides={"shamira.killed": "shamira.trickster.returned"} if woman == "shamira" else {}))
    ids = {s["Id"] for s in household.ENTRIES}
    for retry in (False, True):
        step = "retry" if retry else "settle"
        for evil in (False, True):
            sid = P + step + (".evil" if evil else ".good")
            if sid in ids:
                continue
            branch = "arueshalae.corrupted" if evil else "arueshalae.redeemed"
            require = REQUIRES + (branch,)
            forbid = FORBIDS + (P + "retry.seen", P + "settle.declined") if retry else (
                FORBIDS + (P + "settle.seen", P + "retry.seen"))
            if not evil:
                forbid += ("arueshalae.corrupted",)
            body = household.table_entry(sid, "A name and a loose bracelet",
                "[Shamira and Arueshalae: the upper landing]", nodes(evil, retry),
                pair=PAIR, trigger=P + "settle.failed" if retry else "shamira.trickster.game_proposed",
                requires=require, forbids=forbid, chapters=(5,), delay=48 if retry else 0,
                RestAllowance="household.protected", ParticipantWomen=list(PAIR),
                HouseholdCategory="protected", HouseholdWitness=P + step + ".seen",
                RouteOpen=list(PAIR), ForbidOverrides={"shamira.killed": "shamira.trickster.returned"})
            # The native recruited body, not a retained personality/return flag.
            # Good companion state covers both recruitment sites; fallen contact
            # requires her living native lair recruitment.
            body["RequiresAnyGroups"] = [["arueshalae.evil_recruited"]] if evil else [
                ["arueshalae.recruited_drezen", "arueshalae.recruited_redoubt"]]

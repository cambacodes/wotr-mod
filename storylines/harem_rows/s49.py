"""S49: authored Drezen consignment/watch handover, respect ceiling only.

Native combat history is recall, never attraction. The optional Nera extension
is withheld pending reviewed ceiling metadata and its entire body-window contract.
No native events, partner terms, returns or reconciliation producers are changed.
"""
import copy

from story_format import c, n
from storylines import household

P = "household.pair.wenduag_vellexia."
FRICTION = "household.friction.wenduag.vellexia."
PAIR = ("wenduag", "vellexia")


def flags(*suffixes):
    return tuple(P + suffix for suffix in suffixes)


def later():
    return c('"Later."', abort=True)


def held(step, paid=False):
    result = flags(step + ".seen", step + ".held", "settled", "wenduag_quarry_yielded",
                   "vellexia_watch_kept", "cost.wenduag_kill_yielded",
                   "cost.vellexia_amusement_yielded", "cost.commander_relief_watch")
    if paid:
        result += flags("cost.commander_decoy", "cost.wagon_spent")
    return result + (FRICTION + "settled",)


def success(step, paid=False):
    return [
        n("quarry", "Wenduag", '''{n}In your storehouse, Wenduag catches the cult courier's wrist against a crate. Her knife rests under his jaw. He stops struggling when it draws blood.{/n}
"I caught him. I could finish him before she gets out of that chair." {n}She looks at Vellexia, then shoves him across the narrow aisle, alive.{/n} "Your watch. Let him slip and I'll know what you're worth."''', c("Continue", "watch")),
        n("watch", "Vellexia", '''{n}Vellexia twists the courier's wounded hand behind his back. He whimpers; she smiles, then pushes him toward the waiting wagon instead of making him kneel.{/n}
"Such a lovely noise. And you expect me to spend the evening watching a door." {n}She takes Wenduag's knife by the hilt and returns it, clean side first.{/n} "Very well. Bring me something harder to keep next time."
{n}Wenduag stays until the wagon clears the yard. You take the cold relief watch beside your remaining cargo. Neither woman takes your place.{/n}''', c("Continue", flags=held(step, paid))),
    ]


def row_scenes():
    notice = [
        n("start", "Wenduag", '''{n}Wenduag drops a cut cargo seal on the Table. Your consignment from the Midnight Isles has reached Drezen with a false mark on one crate. Vellexia turns the seal over with a lacquered nail.{/n}
"A cult runner will come for it," {n}Wenduag says.{/n} "I want him before he reaches the gate. She wants to play with him. Which of us is supposed to be watching your goods?"''',
          c('"My cargo. Let me see you hand it over."', "history"),
          c('"Find another amusement."', flags=flags("notice.seen", "notice.refused")),
          later()),
        n("history", "Narrator", '''{n}Wenduag turns the broken seal between her fingers. Vellexia watches her hands.{/n}''',
          c("Continue", "recall", requires=("wenduag.vellexia_conflict",)),
          c("Continue", "unknown", forbids=("wenduag.vellexia_conflict",))),
        n("recall", "Wenduag", '''"You remember her house? I wanted her blood then. I haven't forgotten." {n}Wenduag curls her fingers around the broken seal.{/n} "But if I have to hold every throat myself, what use is anybody following me? She gets the runner breathing. She keeps him."''', c("Continue", "terms")),
        n("unknown", "Wenduag", '''"Look at her. Already deciding which scream she'd like best." {n}Wenduag bares her teeth at Vellexia.{/n} "I can catch the runner. Let's see if she can keep him without spoiling the catch."''', c("Continue", "terms")),
        n("terms", "Vellexia", '''"And let's see whether you can let go of a throat, little huntress." {n}Vellexia taps the seal against Wenduag's knuckles.{/n} "I'll take your catch and keep the wagon moving. No delightful little diversions. You may watch me do it."
{n}She slides the seal back to you.{/n} "Your storehouse, your cargo. When we are finished, you stand the relief. I won't waste my whole visit on your crates."''', c("Continue", flags=flags("notice.seen", "notice.accepted"))),
    ]
    handover = [
        n("start", "Vellexia", '''{n}Two nights later, you lead them from the Table to your storehouse. The courier waits by the crates, holding up a seal. Wenduag has him covered from the rafters. Vellexia sits beside the wagon, leaving its path clear.{/n}
"He says he has come for your goods. Shall I let him load them?" {n}Her gaze rests on the courier's fingers.{/n} "Or have you brought me another way to pass the evening?"''',
          c('[Perception] "That seal is false. Take him."', check=dict(Skill="SkillPerception", DC=22, Success="quarry", Failure="lost")),
          c('"I will draw him out. Use the second wagon."', "quarry_paid"),
          c('"Keep your quarrel. The cargo comes home with me."', "refused"), later()),
        *success("handover"),
        n("quarry_paid", "Wenduag", '''{n}You take a wagon loaded with your own decoy crates out into the yard. The courier follows. Wenduag drops behind him and catches his knife arm; Vellexia brings the second wagon through the open doors.{/n}
"Caught. Don't start carving him up, bitch. Your turn is to keep him."''', c("Continue", "watch_paid")),
        n("watch_paid", "Vellexia", '''"I could make him tell us such filthy things before he died." {n}Vellexia holds the wagon door open. Wenduag lowers her knife and pushes the courier toward it.{/n} "But the huntress wants to see her catch delivered. How demanding."
{n}Your wagoner holds out his hand. With his fee paid, the courier and consignment can leave together. The cold relief watch will be yours.{/n}''', c('"Pay for the wagon and take the relief watch."', flags=held("handover", True), crusade=("Materials", -150)), later()),
        n("lost", "Wenduag", '''{n}The courier drives a hooked blade through the wagon's tether. It rolls into the yard before Wenduag can reach him. Vellexia seizes his sleeve; he leaves it in her hand and vanishes between the crates. By the time the doors are barred, your best cargo is gone.{/n}
"You watched the seal. I watched her. He watched the wagon." {n}Wenduag kicks the severed tether aside.{/n} "Next time we use a decoy."''', c("Continue", flags=flags("handover.seen", "handover.failed", "cost.commander_cargo_lost"))),
        n("refused", "Vellexia", '''"Pack it, then." {n}Vellexia steps aside. Wenduag gathers the loose crates without handing her a thing.{/n} "But don't tell me you have seen what either of us can do. You have seen your goods carried home."
{n}The false seal goes back into your pocket. No courier has been caught.{/n}''', c("Continue", flags=flags("handover.seen", "handover.refused"))),
    ]
    retry = [
        n("start", "Wenduag", '''{n}Wenduag brings the false seal back to the Table. Vellexia lifts it out of her hand before she can set it down.{/n}
"Another wagon," {n}Wenduag says.{/n} "You ride the bait. I catch the runner. She keeps him. Everyone sees what's in the crates first."
{n}Vellexia snaps the seal in two.{/n} "And this time your cargo pays for the amusement, Commander. Two hundred in materials. I'm tired of watching it go wrong."''',
          c('"Pay for another decoy. Nothing hidden in the bait."', "paid"),
          c('"No second watch."', flags=flags("retry.seen", "retry.refused", "unsettled") + (FRICTION + "failed",)), later()),
    ]
    # Paid terminal choices narrate both deeds at execution; unaffordable answers
    # remain hidden, with a selectable Abort. GLOBAL-TC publishes flags atomically.
    retry += [n("paid", "Narrator", '''{n}At your storehouse, Wenduag tests the decoy wagon's tailboard with her boot.{/n} "I'll catch him here. And hand him over before I cut too deep."
"My favourite part, wasted," {n}Vellexia says. She opens the second wagon's door.{/n} "I'll keep him moving. You may count his fingers when he reaches the gate."
{n}The wagoner waits for his fee. Once the runner and cargo leave, you will have the cold relief watch. Neither woman offers to stand it for you.{/n}''', c('"Pay for the wagon and take the relief watch."', flags=held("retry", True), crusade=("Materials", -200)), later())]
    return (("notice", notice, (P + "ready",), (), 0),
            ("handover", handover, flags("notice.accepted"), (), 48),
            ("retry", retry, (P + "ready",), (flags("handover.failed", "handover.refused"),), 48))


def register(payload, scenes, refs):
    """Append S49 only. Safe to call on the coordinator's assembled payload."""
    derived = payload.setdefault("Derived", {})
    derived[P + "ready"] = [[household.eligible(w) for w in PAIR]]
    derived["wenduag.harem.attitude.vellexia.respect"] = [list(flags("settled", "vellexia_watch_kept", "cost.vellexia_amusement_yielded"))]
    derived["vellexia.harem.attitude.wenduag.respect"] = [list(flags("settled", "wenduag_quarry_yielded", "cost.wenduag_kill_yielded"))]
    # This pair is new to the shared host's current partner census. Reserve the
    # existing engine hook names, without inventing enmity or reconciliation.
    pending = payload.setdefault("PendingHooks", [])
    for woman, other in (PAIR, tuple(reversed(PAIR))):
        for key in (household.enmity(woman, other), woman + ".harem.reconciled." + other):
            if key not in pending:
                pending.append(key)
    existing = {s["Id"] for s in scenes}
    for step, nodes, requires, groups, delay in row_scenes():
        if P + step in existing:
            continue
        # table_entry supplies the canonical Table/page/stance/enmity contract.
        # Avoid global registrations: this module owns the appended payload scenes.
        entries = list(household.ENTRIES)
        consumers = dict(household.CONSUMERS)
        try:
            body = household.table_entry(P + step, "A predator's watch", '[Wenduag and Vellexia: the consignment]', nodes,
                PAIR, requires[0], requires=requires[1:] + ("trickster.now", "wenduag.present_now", "vellexia.present_now", "vellexia.trickster.in_person"),
                forbids=flags(step + ".seen") + ("wenduag.closed", "vellexia.closed", "vellexia.trickster.kept_as_mirror", "sacrifice") + (flags("settled") if step == "retry" else ()),
                chapters=(5,), delay=delay, RequiresAnyGroups=[list(g) for g in groups],
                RestAllowance="household.protected", HouseholdCategory="protected", HouseholdWitness=P + step + ".seen")
            body["RequiresAnyGroups"].append(["wenduag.in_party", "wenduag.trickster.echo.abyss.returned_available"])
            scenes.append(copy.deepcopy(body))
        finally:
            household.ENTRIES[:] = entries
            household.CONSUMERS.clear()
            household.CONSUMERS.update(consumers)

"""S27: authored forest-offering claim and witnessed, limited withdrawal.

Respect ceiling only. No spirit, cure, resurrection, partner agreement or echo
is produced here. See tools/route_packs/harem/s27.md for native evidence.
"""
from copy import deepcopy

from story_format import c, n, scene

P = "household.pair.soana_camellia."
AREA = "0a5654e7dc18f074d9356009d55eb51b"
SOANA = "64805abb52739e44280a758f850b300c"
CAMELLIA = "397b090721c41044ea3220445300e1b8"
CLAIM = (P + "claim.spoken", P + "claim.scope.forest_offering")
DEED = (*CLAIM, P + "claim.renounced", P + "camellia.forestoffering_yielded",
        P + "soana.withdrawal_named", P + "cost.camellia.spirit_pretext_yielded",
        P + "cost.soana.witness_time", P + "cost.commander.witness_time")
ENMITY = ("soana.harem.enmity.camellia", "camellia.harem.enmity.soana")
LIVE = ("trickster", "foresight.page_taken", "household.stance_eligible",
        "household.table.kept", P + "ready", "soana.present_now", "camellia.present_now")
BLOCKED = ("household.closed", "trickster.failed", "engine.l12.commander_unreturned",
           "soana.closed", "camellia.closed", *ENMITY)


def terminal(key, speaker, text, step, outcome, extra=()):
    return n(key, speaker, text, c(flags=(P + step + ".seen", P + step + "." + outcome, *extra),
                                  requires=CLAIM if outcome == "kept" else ()),
             portrait=speaker)


def withdrawal(key, step):
    return terminal(key, "Soana", '''{n}Camellia draws herself up. Her hand leaves the amulet.{/n}
"Then I relinquish that offering, from this forest. That is all I have relinquished."
{n}Soana points her stick at the dark stain. Camellia's smile tightens.{/n}
"Your claim to that blood. Nothing else. I heard you. So did the hunter."
"How attentive you both are. Shall we go? The demons have not stopped killing while we stand here."
{n}Soana stays across the entrance until Camellia steps back from it. Then she lowers her stick.{/n}''',
                    step, "kept", DEED[2:])


def envelope(step, nodes, requires=(), forbids=(), delay=0):
    # Manual event presentation, with physical contacts: Remote never supplies a
    # body. Both contacts and the actual area are rechecked during continuation.
    return scene(P + step, "Blood at the cave threshold", "Soana", 5,
                 "[Visit Soana's cave with Camellia.]", nodes,
                 requires=(*LIVE, *requires), forbids=(*BLOCKED, *forbids),
                 delay=delay, last=5, Relationship="household", Chapters=[5],
                 Remote=True, ManualOnly=True, Kind="event", Areas=[AREA],
                 ContactUnit=SOANA, AdditionalContactUnits=[CAMELLIA],
                 Participants=["soana", "camellia"], Pair=["soana", "camellia"],
                 RestAllowance="household.protected", HouseholdCategory="protected",
                 HouseholdWitness=P + step + ".seen",
                 ForbidOverrides={ENMITY[0]: "soana.harem.reconciled.camellia",
                                  ENMITY[1]: "camellia.harem.reconciled.soana"})


def build_scenes():
    check = dict(Skill="SkillLoreReligion", DC=20, Success="withdrawn", Failure="botched", CommanderOnly=True)
    nodes = [n("start", "Soana", '''{n}Soana's stick strikes the cave threshold, beside a dark smear. Camellia stops with one boot above it. Beyond the trees, something howls; the old woman turns her head, listens, then looks back at Camellia.{/n}
"Blood on your cuff. Blood on my stone. Have you brought the demons' work to my door, child?"
"I have been very helpful against the demons." {n}Camellia smooths the stained cuff instead of hiding it.{/n} "There are offerings even an elder should not begrudge."
"Then say who you think can demand one here."''',
        c('"Say exactly what you are claiming."', "claim.check"),
        c('"I will witness what you give up."', "claim.witness"),
        c('"Leave this between you."', "declined"), c("[Later.]", abort=True), portrait="Soana")]
    for method in ("check", "witness"):
        nodes.append(n("claim." + method, "Camellia", '''{n}Camellia touches the amulet at her throat.{/n}
"My spirit has a right to an offering from this forest. That blood was hers to ask for."
{n}Soana thrusts her stick between Camellia's boot and the stain.{/n}
"Your blood is on my threshold. Do not put a spirit's name over it. I know what I have bound here. You will not feed something of yours on my land."
{n}Camellia looks at the stick, then at you. She has stopped smiling.{/n}''',
            c(next="answer." + method, flags=CLAIM), portrait="Camellia"))
    nodes.append(n("answer.check", "Camellia", '''"Well, my friend? You wished me to be exact."
{n}Her fingers tighten around the amulet. Soana waits, blocking the cave mouth.{/n}''',
        c('"Withdraw that claim before her."', check=deepcopy(check), forbids=("camellia.mireya_unmasked",)),
        c('"You invented Mireya. Withdraw this claim to her forest."', check=deepcopy(check),
          requires=("camellia.mireya_unmasked",)), portrait="Camellia"))
    nodes.append(n("answer.witness", "Soana", '''"An offering from my forest. Those were your words, child. Take them back where the hunter can hear you."
{n}Camellia lifts her chin. She looks past Soana into the cave, then lets the amulet fall against her dress.{/n}''',
                   c(next="witnessed"), portrait="Soana"))
    nodes.extend([withdrawal("withdrawn", "settle"), withdrawal("witnessed", "settle"),
        terminal("botched", "Soana", '''"Her spirit's claim? You have given it a name and a place at my door!"
{n}Camellia's smile returns.{/n} "I was only trying to explain. You heard the Commander."
"I heard enough. Go. Come back when you can say whose blood you are talking about."
{n}Soana scrapes the stained earth away from the threshold. Camellia watches without offering a hand.{/n}''',
                 "settle", "failed", (P + "claim.scope_muddled",)),
        terminal("declined", "Soana", '''{n}Soana plants her stick across the entrance.{/n}
"Then take her away from my cave."
"Such hospitality." {n}Camellia turns, keeping the stained cuff in view.{/n}''', "settle", "declined")])
    settle = envelope("settle", nodes, forbids=(P + "settle.seen",))
    retry = envelope("retry", [n("start", "Soana", '''{n}The dark soil has been scraped away. Soana stands on the bare stone. Camellia stops short of her stick.{/n}
"I have demons in my forest, hunter. I will not spend another day listening to this one's excuses. Which claim did you come to settle?"
"I remember what I said." {n}Camellia's voice is cold.{/n} "Let us not enlarge it."''',
        c('"That offering, from this forest. Withdraw that claim."', "witnessed"),
        c('"Let her keep the claim."', "failed"), c('"Leave it unanswered."', "declined"),
        c("[Later.]", abort=True), portrait="Soana"), withdrawal("witnessed", "retry"),
        terminal("failed", "Soana", '''"Then she keeps it beyond my forest."
{n}Soana strikes the stone with her stick. Camellia steps back, her lips pinched.{/n}
"I have heard you, elder. Spare the shouting."
"And you have not taken back a word. Go."''', "retry", "failed", (P + "claim.left_standing",)),
        terminal("declined", "Soana", '''{n}Soana turns toward her cave.{/n}
"I shall remember what she claimed. And what you would not hear."
{n}Camellia's eyes follow her until the darkness hides her face.{/n}''', "retry", "declined")],
        requires=(P + "settle.failed", *CLAIM),
        forbids=(P + "retry.seen", P + "settle.kept", P + "settle.declined"), delay=48)
    return [settle, retry]


def ledger_entry():
    def line(text, requires=(), forbids=()):
        return dict(Text="{n}" + text + "{/n}", Requires=list(requires), Forbids=list(forbids), AnyGroups=[])
    return dict(Id=P + "ledger", Section="Seating Notes", Portrait="Soana", Title="Blood at the cave threshold",
        Text="{n}Camellia's claim to an offering from Soana's forest.{/n}",
        Requires=["foresight.page_taken", P + "ready"], Forbids=[], AnyGroups=[], Lines=[
            line("Camellia withdrew her claim to an offering from Soana's forest. Soana named the withdrawal before me.",
                 requires=(P + "claim.renounced",)),
            line("I muddled the scope of the claim.", requires=(P + "settle.failed",), forbids=(P + "retry.seen",)),
            line("The claim to the forest offering was left standing.", requires=(P + "retry.failed",)),
            line("I would not witness the claim.", requires=(P + "settle.declined",)),
            line("I would not witness the claim.", requires=(P + "retry.declined",)),
            line("The elder has not heard a withdrawal.", forbids=(P + "settle.seen",))])


def register(payload, scenes, refs):
    from storylines import foresight, lastcall_ledger
    # Reserve this row's integrator-owned state readers, just as table_entry's
    # integration does. This declares hooks; it does not produce their state.
    pending = payload.setdefault("PendingHooks", [])
    for flag in (*ENMITY, "soana.harem.reconciled.camellia", "camellia.harem.reconciled.soana"):
        if flag not in pending:
            pending.append(flag)
    existing = {s["Id"] for s in payload["Scenes"]}
    payload["Scenes"].extend(s for s in build_scenes() if s["Id"] not in existing)
    payload.setdefault("Derived", {}).update({
        P + "ready": [["soana.harem.eligible", "camellia.harem.eligible", "soana.present_now", "camellia.present_now"]],
        P + "rival": [[P + "ready"]], P + "respect": [list(DEED)]})
    for step in ("settle", "retry"):
        foresight.CONSUMERS[P + step] = "foresight.page_taken"
    if not any(e["Id"] == P + "ledger" for e in lastcall_ledger.EXTRA_ENTRIES):
        lastcall_ledger.EXTRA_ENTRIES.append(ledger_entry())

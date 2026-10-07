"""S35: authored contested stores demand; hs-A, schedule 5.04.

Native cues are voice anchors, not producers of this forgery. Respect-only:
publish incident witnesses; the household controller owns attitudes and enmity.
No new return, collateral, treasury charge, echo or intimate interval.
"""
from copy import deepcopy

from story_format import c, n, scene
from storylines import arsinoe_trickster, household

PREFIX = "household.pair.arsinoe_nurah."
WORLD_DC = 30
WOMEN = ("arsinoe", "nurah")
LIEN = arsinoe_trickster.LIEN


def flags(*names):
    return tuple(PREFIX + name for name in names)


def held(step, method):
    return flags(step + ".seen", "resolved", "arsinoe_flaw_named", "nurah_author_named",
                 "cost.arsinoe_claim_limited", "cost.nurah_forgery_exposed", "method." + method)


def result_nodes(step):
    return [
        n("audit_held", "Arsinoe", '''{n}You lay the freight calculation beside the demand. The same wagon has been charged twice. Arsinoe presses her seal across the false total before the waiting teamster can take it away.{/n}
"That demand will not reach the stores. The hand is yours, Nurah. The sum does not follow."
"At least you noticed the hand," {n}Nurah says. She takes the pen from beside Arsinoe's wrist and signs the correction with an extravagant flourish.{/n} "Don't credit some quartermaster with my work. He couldn't forge his own mother's blessing."
"Your name stays on the forgery as well as the correction."
"Good. Put yours beside it. I want to know who caught me."''',
          c("Continue", flags=held(step, "audit"))),
        n("lien_held", "Arsinoe", '''{n}Arsinoe unfolds the existing cauldron lease beside the demand, keeping her palm on its gold seal.{/n}
"I already hold your lien. Very well: I will withdraw this demand, rather than pursue both claims. The lease remains enforceable."
{n}She marks the duplicated freight charge, then pushes the pen toward Nurah.{/n} "And this remains a forgery. Name its author."
"Nurah Dendiwhar. No 'property of' above it."
"Authorship is not title to the crusade's stores."
{n}Nurah signs, grinning.{/n} "You caught the wagon. I kept the name. We might both survive the afternoon."''',
          c("Continue", flags=held(step, "lien"))),
        n("word_held", "Arsinoe", '''{n}The total on the demand dwindles beneath Arsinoe's finger. The copied freight charge is still there. She holds the page against the lamp, watching the ink move.{/n}
"I saw that. You have made the demand harmless. You have not made it honest."
"Oh, do let me watch next time," {n}Nurah says, leaning over the sheet.{/n} "I spend hours matching ink."
{n}Arsinoe puts a stroke through the false charge and turns the pen toward her.{/n} "Your name. On your work. I will limit the claim to this bill; I will not certify your good character."
"Then we understand each other." {n}Nurah signs. Arsinoe keeps the altered bill beside the original calculation.{/n}''',
          c("Continue", flags=held(step, "word"))),
        n("refused", "Arsinoe", '''"Then the demand stays disputed. I will not put Abadar's seal on it."
{n}Nurah snatches up the pen before Arsinoe can put it away.{/n} "And I will not have my name changed to 'the Commander's grateful servant.' You can leave that disputed too."
{n}Outside, the teamster shouts for a decision about the crusade's stores. Arsinoe takes the unsigned bill back to her counter.{/n}''',
          c("Continue", flags=flags(step + ".seen", "permanent_refusal", "unsettled"))),
    ]


def audit_nodes():
    return [
        n("start", "Arsinoe", '''{n}A teamster waits at the tavern door, his whip tucked under one arm. Arsinoe has spread a demand for the crusade's stores across the Table. Nurah is holding its corner down with her empty cup.{/n}
"The temple is being asked to honor this before the wagons leave. It bears a convincing seal. It also bears Nurah's hand."
"Convincing? I was hoping for impeccable."
{n}Arsinoe moves the cup and sets the loading tally beside the demand.{/n} "Drezen needs those supplies. I want the charge proved before anyone opens the stores."
"And I want my name on my work," {n}Nurah says.{/n} "Not yours, Commander. Not some fat fool who thinks holding the purse makes him the author."''',
          c('[Knowledge (World)] "Compare the freight charges before the wagons leave."',
            check=dict(Skill="SkillKnowledgeWorld", DC=WORLD_DC, Success="audit_held",
                       Failure="missed", CommanderOnly=True)),
          c('"Withdraw this demand. You already hold my lien."', "lien_held", requires=(LIEN,)),
          household.word_made_true('"The demand is no greater than the stores actually owe."',
                                   "word_held", use="arsinoe_nurah"),
          c('"Leave it in dispute."', "refused"),
          c('"Later."', abort=True)),
        n("missed", "Arsinoe", '''{n}The teamster takes his loading tally back. You have found no discrepancy you can prove. Arsinoe folds the demand without sealing it.{/n}
"I will keep my copy. Bring the figures back in order, if you want me to act on them."
"Perhaps the wagons are carrying arithmetic," {n}Nurah says.{/n} "It seems to have escaped you."
{n}She reaches for the demand. Arsinoe puts it beneath her hand.{/n} "This stays with me. Drezen has lost enough stores to clever people."''',
          c("Continue", flags=flags("audit.seen", "audit.failed"))),
        *result_nodes("audit"),
    ]


def retry_nodes():
    return [
        n("start", "Arsinoe", '''{n}The loading tally has returned. Arsinoe puts it beside the disputed bill; Nurah swings her feet beneath the bench, watching the priestess rather than the paper.{/n}
"One wagon. Two freight charges. Now there is time to compare them."
"I wondered how long you would take," {n}Nurah says.{/n}
"Long enough to prove it. Take the pen. This correction needs its author's name."
{n}Nurah catches the pen between two fingers.{/n} "Only the correction to this bill. You can find another woman to write a confession of wickedness."''',
          c('"Strike the duplicate charge and name its author."', "audit_held"),
          c('"Leave it in dispute."', "refused"),
          c('"Later."', abort=True)),
        # Keep only this retry's authorized audit remedy and refusal.
        *[node for node in result_nodes("retry") if node["Id"] in ("audit_held", "refused")],
    ]


def entry(step, nodes, delay=0):
    edges = [household.enmity(a, b) for a, b in (WOMEN, WOMEN[::-1])]
    return scene(PREFIX + step, "The bill that names its author", "Arsinoe", 5,
                 '[Arsinoe and Nurah: the disputed bill]' if step == "audit" else
                 '[Arsinoe and Nurah: the returned loading tally]', nodes,
                 requires=("trickster", "trickster.now", household.PAGE_TAKEN, household.KEPT,
                           household.STANCE_ELIGIBLE, "arsinoe.harem.eligible", "nurah.harem.eligible",
                           "arsinoe.present_now", "nurah.present_now", "nurah.meeting_arrived") +
                          (flags("audit.failed") if step == "retry" else ()),
                 forbids=(household.KING_GONE, "trickster.failed", "nurah.prison",
                          "nurah.meeting_declined", "nurah.meeting_withdrawn", "sacrifice") +
                         tuple(edges) + flags(step + ".seen", "resolved", "permanent_refusal"),
                 delay=delay, last=5, Relationship="household", Areas=[household.DREZEN], Chapters=[5],
                 InteractionHub=household.TABLE_HUB, Participants=list(WOMEN), Pair=list(WOMEN),
                 ForbidOverrides={edge: a + ".harem.reconciled." + b
                                  for edge, (a, b) in zip(edges, (WOMEN, WOMEN[::-1]))},
                 RestAllowance="household.protected", HouseholdCategory="protected",
                 HouseholdWitness=PREFIX + step + ".seen", Kind="event")


SCENES = [entry("audit", audit_nodes()), entry("retry", retry_nodes(), 48)]


def ledger_entry():
    return dict(Id="seating.arsinoe_nurah.audit", Section="Seating Notes", Portrait="Arsinoe",
                Title="The disputed bill", Text="{n}Arsinoe challenged a forged demand on the crusade's stores.{/n}",
                Requires=list(flags("audit.seen")), Forbids=[], Lines=[
                    dict(Text=text, Requires=list(flags(*requires)), Forbids=list(flags(*forbids)))
                    for text, requires, forbids in [
                        ("{n}I found the duplicate freight charge. Arsinoe limited the claim; Nurah signed her own forgery and correction.{/n}",
                         ("resolved", "method.audit"), ()),
                        ("{n}Arsinoe withdrew the forged demand against the lien she already held. The cauldron lease remained in force; Nurah named her work.{/n}",
                         ("resolved", "method.lien"), ()),
                        ("{n}My Word reduced the demand. Arsinoe kept the proof of forgery. Nurah signed it; the debt of that Word remained mine.{/n}",
                         ("resolved", "method.word"), ()),
                        ("{n}I left the forged bill disputed.{/n}", ("permanent_refusal",), ("resolved",)),
                        ("{n}I failed to prove the flaw. The forged bill was still disputed.{/n}",
                         ("audit.failed",), ("resolved", "permanent_refusal")),
                    ]])


def register(payload, scenes, refs):
    """Append the reviewed row. Safe before route assembly and on repeat discovery.

    With the final Ledger available, append its history reader as well. The
    coordinator owns the loader call and attitude/first-wins witness bindings.
    """
    ids = {s["Id"] for s in scenes}
    scenes.extend(deepcopy(s) for s in SCENES if s["Id"] not in ids)
    from storylines import foresight
    consumers = {s["Id"]: household.PAGE_TAKEN for s in SCENES}
    foresight.CONSUMERS.update(consumers)
    payload.setdefault("ForesightConsumers", {}).update(consumers)
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None:
        entries = ledger.setdefault("Entries", [])
        # Retain this old entry's identity and lines, but retire its now-stale
        # "Arsinoe has not noticed yet" account after the incident is heard.
        for entry in entries:
            if entry["Id"] == "seating.arsinoe.nurah":
                gate = PREFIX + "audit.seen"
                if gate not in entry.setdefault("Forbids", []):
                    entry["Forbids"].append(gate)
        if not any(e["Id"] == "seating.arsinoe_nurah.audit" for e in entries):
            entries.append(ledger_entry())

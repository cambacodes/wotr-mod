"""S45: authored singleton trophy reclamation; fixed X, no ladder or slots.

Native evidence: TrueYaniel/Cue_0021, 7db270440f7e3954aabbd4ad295ed65b,
enGB 2c1d8dde-9f5c-461b-9e93-a0762f43f1fe (collection, not wax).
MinaghoAfterCombat/Cue_0032, efd4619513c6a884ab7c0c2e7b8aefe2,
enGB 891f1b4a-b1d1-4941-8949-c08a4c94f96e (calculating contempt).
The portable case, likeness, destruction and limited hearing are authored.
K2 is retired. Registration operates on exported copies, never route globals.
"""
import copy

from story_format import c, n, p, scene
from storylines import foresight

P = "household.pair.yaniel_minagho."
Y = "yaniel.trickster."
TOLD = Y + "minagho_told"
SECRET = "trickster.secret.yaniel_minagho"
LATER = P + "truth_now_told"
CONTACT = P + "respondent_current"
KNOWN = P + "known"
INTIMATE = P + "minagho_favoured"
SEEN = P + "hearing.seen"


def pause():
    return c("[Later.]", abort=True)


def outcomes():
    common = ["hearing.seen", "hearing.remedied", "hearing.quest_started",
              "proof.quest_done", "claim.dismantled", "cost.minagho_identification_tools",
              "cost.commander_likeness"]
    return {
        "destroyed": common + ["attendance_earned", "cost.yaniel_hearing"],
        "delivered": common + ["courier_chosen", "cost.yaniel_verification_watch"],
        "unsettled": ["hearing.seen", "hearing.unsettled", "hearing.quest_started", "claim.retained"],
        "declined": ["hearing.seen", "hearing.declined", "claim.unanswered"],
    }


def docket():
    nodes = [n("start", "Narrator",
               "{n}Yaniel stands her watch above Drezen's east gate. A cart of wounded crawls toward the arch below. She keeps her spear against the parapet while you approach.{/n}",
               c("[Speak about Minagho's collection.]", "informed.start", requires=(KNOWN,)),
               c("[Speak about the claim and what you withheld.]", "concealed.start",
                 requires=(SECRET,), forbids=(KNOWN, INTIMATE)),
               c("[Speak about the claim and what you withheld.]", "intimate.start",
                 requires=(SECRET, INTIMATE), forbids=(KNOWN,)), pause())]
    for variant in ("informed", "concealed", "intimate"):
        def go(target):
            return variant + "." + target
        nodes.append(n(go("start"), "Yaniel",
            '"If she is offering a likeness of me, I want its label too." {n}Her thumb presses the scar on her wrist.{/n} '
            '"I want both. Not a promise that she will stop using them." '
            + ('{n}You have something withheld to tell her when you carry out this decision. She waits for your proposal.{/n}'
               if variant != "informed" else '"And do not dress this up as a friendly visit."'),
            c("[Take Yaniel's demand to the cache.]", go("demand"), requires=(CONTACT,)),
            c('"A courier can carry it. You need not see her."', go("courier"), requires=(CONTACT,)),
            c('"Let Minagho keep her souvenirs."', go("declined")), pause(),
            c("[Keep the demand unanswered until Minagho can be reached.]", go("absent"), forbids=(CONTACT,))))
        nodes.append(n(go("absent"), "Yaniel",
            '"Then there is no surrender to hear." {n}She looks down at the wounded cart.{/n} '
            '"Do not bring me an answer from someone who is not there to give it. I have waited longer than she deserves already."', pause()))
        for mode in ("demand", "courier"):
            nodes.append(n(go(mode), "Narrator",
                '{n}The demand is for the wax face and the strip identifying it. Minagho can have the portable case carried out of her quarters; Yaniel need not go inside. The guards will check the case before opening it.{/n}',
                c("[Bring the likeness and its identifying label out together.]",
                  go("claim.direct" if mode == "demand" else "claim.courier")),
                c('"Leave the cache untouched."', go("unsettled")), pause()))
        for mode in ("direct", "courier"):
            nodes.append(n(go("claim." + mode), "Minagho",
                '"You want the face and the name. You can have them. Reach for anything else and I will take your fingers." '
                '{n}She indicates the narrow case, still shut. A guard keeps his hand on its clasp.{/n} '
                '"I have no use for a trophy that brings your paladin scratching at my door every night. Burn it. She will still remember me."',
                c("[Give the objects to Yaniel to destroy.]", go("destroyed" if mode == "direct" else "delivered")),
                c("[Destroy them yourself and have the courier bring the remains.]", go("delivered")),
                c('"Keep the likeness. It may be useful."', go("unsettled")), pause()))
        texts = {
            "destroyed": '"Burn the label with the face. I will keep the ash." {n}Yaniel points to the brazier beside the gate stair.{/n} "After that, I will hear this one surrender. Guards between us. Nothing else. She does not get a visit for every piece of me she gives back."',
            "delivered": '"Send the pieces here. I will check them myself, and burn whatever is left." {n}Yaniel nudges the brazier closer with her boot.{/n} "The courier goes back alone. I have no business in her rooms."',
            "unsettled": '"Keep it, and it stays a tool she can use." {n}Yaniel closes her hand around her spear.{/n} "Do not tell me you have dealt with it if you mean to keep it."',
            "declined": '"Her souvenirs." {n}Yaniel repeats the word without raising her voice.{/n} "I tried to kill my guards every day I could stand. Remember that when you admire her collection."',
        }
        for result, flags in outcomes().items():
            answer = "[Accept the verdict.]" if result in ("destroyed", "delivered") else "[Leave the claim on the docket.]"
            terminal = [P + flag for flag in flags]
            if variant != "informed":
                answer = ('"Minagho is in my bed. I hid that from you."' if variant == "intimate" else
                          '"Minagho is under my protection. I meant to keep her close, and hid it from you."') + " " + answer
                terminal.append(LATER)
            nodes.append(n(go(result), "Yaniel", texts[result],
                           c(answer, flags=terminal, requires=(CONTACT,) if result in ("destroyed", "delivered") else ()), pause()))
    return scene(P + "hearing", "The labelled face", "Yaniel", 5,
                 '"About Minagho\'s collection."', nodes,
                 requires=("trickster", foresight.PAGE_TAKEN, "household.table.kept",
                           Y + "returned", "yaniel.freed.latched", "yaniel.present_now", Y + "minagho_seen"),
                 forbids=(SEEN, "yaniel.closed", "yaniel.killed.latched", Y + "left_free",
                          "yaniel.epoch_unavailable", "fool_king.gone", "trickster.failed", "inhuman"),
                 last=5, Relationship="household", Chapters=[5],
                 Areas=["2570015799edf594daf2f076f2f975d8"], InteractionHub="household.table",
                 RequiresAnyGroups=[[TOLD, LATER, SECRET]], RestAllowance="household.protected",
                 HouseholdCategory="protected", HouseholdWitness=SEEN,
                 # Protected claimant: Participants would impose romance-seat eligibility.
                 # Yaniel's actual body and route losses are guarded explicitly above.
                 Participants=[], ParticipantWomen=[])


def register(payload, scenes, refs):
    if any(s["Id"] == P + "hearing" for s in payload["Scenes"]):
        return
    derived = payload.setdefault("Derived", {})
    derived[KNOWN] = [[TOLD], [LATER]]
    derived[INTIMATE] = [["minachiv.complete", "minachiv.future_minagho", CONTACT],
                         ["minachiv.complete", "minachiv.future_two", CONTACT]]
    derived[CONTACT] = [["participant.minagho.available", "minagho.present_now",
                         "minagho_chivarro.trickster.minagho_in"]]
    payload.setdefault("DerivedForbids", {})[CONTACT] = ["minachiv.closed", "minagho.epoch_unavailable",
        "minagho_chivarro.trickster.declined_minagho", "minagho.returned_actor_lost", "inhuman"]
    payload.setdefault("SeenCues", {})["household.native.yaniel_trophies_told"] = ["7db270440f7e3954aabbd4ad295ed65b"]
    body = docket()
    payload["Scenes"].append(body)
    foresight.CONSUMERS[body["Id"]] = foresight.PAGE_TAKEN
    for s in payload["Scenes"]:
        if s["Id"] == Y + "after.watch":
            start = next(node for node in s["Nodes"] if node["Id"] == "start")
            exits = copy.deepcopy(start["Choices"])
            for answer in start["Choices"]:
                answer["Forbids"].append(SEEN)
            start["Choices"].append(c("[Hear her answer about the claim.]", "s45.watch", requires=(SEEN,)))
            s["Nodes"].append(n("s45.watch", "Yaniel",
                '"About Minagho." {n}She checks that the sentry has gone down the stair.{/n} "You have not bought her a pardon from me."',
                c("Continue", "s45.watch.direct", requires=(P + "attendance_earned",)),
                c("Continue", "s45.watch.courier", requires=(P + "courier_chosen",)),
                c("Continue", "s45.watch.unanswered", requires=(P + "hearing.unsettled",)),
                c("Continue", "s45.watch.unanswered", requires=(P + "hearing.declined",))))
            for suffix, text in (
                ("direct", '"I burned the face and heard the surrender. One hearing. That was all." {n}Her fingers close on a small pouch of ash.{/n}'),
                ("courier", '"I checked every piece the courier brought. The label burned with the wax. I kept the ash. I did not go to her."'),
                ("unanswered", '"The claim is still there. Whatever else we do here, remember that."')):
                s["Nodes"].append(n("s45.watch." + suffix, "Yaniel", text,
                    c("Continue", "s45.watch.late", requires=(LATER,), forbids=(TOLD,)),
                    c("Continue", "s45.watch.resume", requires=(TOLD,)),
                    c("Continue", "s45.watch.resume", forbids=(TOLD, LATER))))
            s["Nodes"].append(n("s45.watch.late", "Yaniel",
                '"And you told me what you kept back. Late. I have not forgotten the silence before it." '
                '{n}She looks toward the stair again.{/n} "Now. The watch."', c("Continue", "s45.watch.resume")))
            s["Nodes"].append(n("s45.watch.resume", "Yaniel", '"Speak. I am listening."', *exits))
        if s["Id"].startswith(Y + "commit.trade"):
            patched = False
            for node in s["Nodes"]:
                choices = node["Choices"]
                if len(choices) >= 3 and [a.get("Next") for a in choices[:3]] == ["told", "hid", "ask"]:
                    for a in choices[1:3]:
                        if LATER not in a["Forbids"]:
                            a["Forbids"].append(LATER)
                    choices.append(c("Continue", "household_minagho_told_later", requires=(LATER,), forbids=(TOLD,)))
                    patched = True
            if patched:
                s["Nodes"].append(n("household_minagho_told_later", "Yaniel",
                    '"You told me after I asked. After you kept it from me. I remember both." '
                    '{n}She keeps her hand extended for the iron.{/n} "And I remember her. The trade still stands."', c("Continue", "ask")))
        if s["Id"] in (Y + "epilogue.together", "yaniel.lastcall.page"):
            for node in s["Nodes"]:
                for para in node.get("Paragraphs", []):
                    if SECRET in para.get("Requires", []):
                        para["Forbids"] = list(dict.fromkeys(para.get("Forbids", []) + [TOLD, LATER]))
                node.setdefault("Paragraphs", []).extend([
                    p("{n}Yaniel learned the Commander's tie to Minagho before the war ended. She remembered having to ask, and being kept in the dark. She kept her watch, and the knife in her boot.{/n}", requires=(LATER,), forbids=(TOLD,)),
                    p("{n}The wax face and its label burned. Yaniel kept the ash. Minagho surrendered no other trophy, and Yaniel gave her no pardon.{/n}", requires=(P + "claim.dismantled",)),
                ])
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger:
        for entry in ledger["Entries"]:
            if entry["Id"] == "secret.yaniel_minagho":
                for line in entry.get("Lines", []):
                    if "Unknown to Yaniel" in line.get("Text", ""):
                        line.setdefault("Forbids", []).extend([TOLD, LATER])
                entry.setdefault("Lines", []).append(p(
                    "{n}Told later: Yaniel knows what was withheld about Minagho. The concealment remains part of their history.{/n}",
                    requires=(LATER,), forbids=(TOLD,)))
        ledger["Entries"].append(dict(Id="s45.claim", Section="Seating Notes", Title="Yaniel's claim", Portrait="Yaniel",
            Text="{n}Yaniel's objection to Minagho remains.{/n}", Requires=[SEEN], Forbids=[], AnyGroups=[],
            Lines=[p("{n}One likeness burned. None of the years returned. The Commander gave up its use as an impersonation tool.{/n}", requires=(P + "claim.dismantled",)),
                   p("{n}The likeness is still a tool. Yaniel's objection is still an objection.{/n}", any_groups=((P + "hearing.unsettled", P + "hearing.declined"),)),
                   p("{n}Yaniel chose a guarded hearing after the destruction; she owed Minagho no other visit.{/n}", requires=(P + "attendance_earned",)),
                   p("{n}Yaniel spent her watch verifying the surrendered pieces. The courier returned alone.{/n}", requires=(P + "courier_chosen",))]))

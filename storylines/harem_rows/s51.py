"""S51: authored Windstep pursuit-chart erasure, not a native murder accusation.

Private protected docket; no romance, page, attitude or reconciliation producer.
Areelu responds remotely at the native cell apparatus, never in Nidalynn's room.
See tools/route_packs/harem/s51.md for verified anchors and integration blockers.
"""
from story_format import c, n, p, scene
from storylines import nidalynn_trickster as nd, areelu_trickster as ar

P = "household.pair.nidalynn_areelu."
PROJECTOR_BROKEN = P + "projector_broken"
CELL_ROOT = ar.CELL_RETURN  # Cue_0035; safe leaf, original cell list on every outcome


def flags(*suffixes):
    return tuple(P + suffix for suffix in suffixes)


ERASED = flags("cell.seen", "cell.chart_erased", "chart.original_burned",
               "chart.pursuit_slip_burned", "cost.areelu_field_notes_lost",
               "cost.commander_research_lost")
BUNDLE_LOST = P + "cost.commander_bundle_lost"


def later():
    return c("[Later.]", abort=True)


def private(step, title, entry, nodes, requires=(), forbids=(), delay=0, groups=()):
    """Two exact existing bodies, one shared step witness and protected clock."""
    result = []
    for body, hub in (("widow", nd.WIDOW), ("chosen", nd.CHOSEN)):
        presence = nd.PRESENCES[hub]
        # Current power replaces the presence's historical Trickster prerequisite.
        positive = [key for key in presence["Requires"] if key != "trickster.ever"]
        extra = dict(Relationship="household", Chapters=[5], Participants=["nidalynn"],
                     ContactUnit=presence["Unit"], Areas=[presence["Area"]], InteractionHub=hub,
                     RequiresAnyGroups=[list(group) for group in groups],
                     HouseholdWitness=P + step + ".seen")
        if step == "notice":
            # Discovery has no allowance spend; every paid/witnessed sequel does.
            extra["HouseholdDiscovery"] = True
        else:
            extra.update(HouseholdCategory="protected", RestAllowance="household.protected")
        result.append(scene(P + step + "." + body, title, "Nidalynn", 5, entry, nodes,
                            requires=("trickster", "nidalynn.present_now", *positive, *requires),
                            forbids=tuple(dict.fromkeys(("trickster.failed", *presence["Forbids"],
                                                        "nidalynn.epoch_unavailable", P + step + ".seen", *forbids))),
                            delay=delay, last=5, **extra))
    return result


def build_scenes():
    out = private("notice", "The mare beneath the stars", '"What do you want Areelu to hear?"', [
        n("start", "Nidalynn", '''{n}Nidalynn turns over a scrap of cloth. On its reverse she has stitched a mare beneath three stars. Refugees are selling their last silver across the square; she watches a clan brooch change hands.{/n}
"Windstep. Reudger the White made cheese there. He sat smoking while the mares grazed. There's scorched ground now, and graves nobody can find."
{n}She presses the cloth flat.{/n}
"Don't bring her the names of the generals. Reudger made cheese. Tell her that. And if her work points the demons toward anyone still hiding out there, bring it back."''',
          c('"I\'ll carry their name to her."', "carried"),
          c('"I won\'t take this to her."', "refused"), later()),
        n("carried", "Nidalynn", '''"The mare's foreleg is raised. And the first ford lies below a split white boulder. Remember both."
{n}She puts the cloth in your hand, then closes your fingers over it.{/n}
"I've given you a way to find them. Don't make me sorry for it."''',
          c("[Take the cloth.]", flags=flags("notice.seen", "notice.carried", "cost.nidalynn_memory_given"))),
        n("refused", "Nidalynn", '''{n}She takes the cloth back.{/n} "Then I'll keep their names here. You've enough people asking you to forget what the Wound cost."''',
          c("[Leave.]", flags=flags("notice.seen", "notice.refused", "unanswered"))),
    ], requires=(P + "ready",))
    out.append(scene(P + "cell", "A usable trail", "Areelu", 5,
        '"Nidalynn remembers Windstep. Your field work may still lead hunters to its survivors."', [
        n("start", "Areelu", '''{n}A field bundle lies beside the cell's apparatus, under a cover marked with a mare. Areelu's projection watches you unfold Nidalynn's cloth; its hands remain smoke and light.{/n}
"The grazing ground. Yes. I followed the displacement east. Those leaves would still serve a hunter — or your scouts."
{n}Her gaze passes over the stitched stars.{/n}
"She wants the pasture back. I cannot give her that. These leaves are another matter. Take them, and stop calling them an apology. There is no second working copy here."
"I want you at Threshold. I will discard a field route to keep you moving toward it. I will not discard my purpose."''',
          c("[Perception] Find the pursuit slip before burning the route.",
            check=dict(Skill="SkillPerception", DC=24, Success="erased", Failure="incomplete", CommanderOnly=True)),
          c("[Burn the entire field bundle, including the route your scouts could use.]", "whole"),
          c('"Keep the route. I may want it."', "retained"), later()),
        n("erased", "Areelu", '''{n}The ford on the main sheet is false. A narrow slip tucked beneath the binding marks the split boulder and the continuing trail. You burn both, keeping only the recognizable cover. Ink curls black in the flame.{/n}
"You could have used that. Now neither you nor a demon picking over your belongings will. My memory remains, Commander. Do not mistake burning paper for taming me."''',
          c("[Leave the ashes; carry back the cover.]", flags=ERASED)),
        n("whole", "Areelu", '''{n}You pull off the mare-marked cover and feed every leaf into the flame. A folded pursuit slip falls from the binding; you push it back into the fire. The scouts' route burns with it.{/n}
"Wasteful. Thorough, though. If you wish to know what was there, you will have to ask me."''',
          c("[Carry back the cover.]", flags=(*ERASED, BUNDLE_LOST))),
        n("incomplete", "Areelu", '''{n}You burn the main sheet and roll the useful leaves for your scouts. As you tie them, a narrow slip slides from the binding: the split white boulder, followed by a trail the burnt sheet never showed.{/n}
"You preserved more than you intended. Take the remainder. You wanted something useful."
{n}You pack the unburned leaves and the pursuit slip beneath the marked cover and carry them away.{/n}''',
          c("[Take the incomplete exchange back to Nidalynn.]",
            flags=flags("cell.seen", "cell.failed", "chart.incomplete", "chart.bundle_carried", "cost.commander_copy_exposed"))),
        n("retained", "Areelu", '''"Then take it. But do not tell her you destroyed it. She knows the country better than you do."
{n}You wrap the chart, its loose pursuit slip and the remaining leaves in the mare-marked cover, and pack the whole bundle for the journey back.{/n}''',
          c("[Carry the field bundle away.]", flags=flags("cell.seen", "cell.refused", "chart.retained", "chart.bundle_carried"))),
    ], requires=("trickster", P + "notice.carried", P + "cost.nidalynn_memory_given"),
       forbids=("trickster.failed", "areelu.closed", "areelu.epoch_unavailable", PROJECTOR_BROKEN,
                P + "cell.seen", P + "notice.refused"), delay=48, last=5,
       Relationship="household", Chapters=[5], Participants=["areelu"],
       AnswerLists=[ar.CELL_LIST], NativeReturnCue=CELL_ROOT, HouseholdCategory="protected",
       HouseholdWitness=P + "cell.seen", RestAllowance="household.protected"))
    out.extend(private("retry", "The leaves you kept", '"I brought back the field bundle."', [
        n("start", "Nidalynn", '''{n}Nidalynn unrolls the carried leaves beside a brazier. Her finger stops at the white boulder on the loose slip.{/n}
"There. You left them a road. And kept one for yourself."
{n}She puts the slip on top of the bundle.{/n}
"I heard what she offered. Not sorrow. A piece of her work. You brought it here; you can burn it here. All of it."''',
          c("[Burn the carried remainder and the pursuit slip.]", "burned"),
          c('"Keep it."', "refused"), later()),
        n("burned", "Nidalynn", '''{n}You remove the marked cover. Every surviving leaf goes into the brazier, including the slip. Nidalynn turns the burning bundle with the poker until nothing legible remains.{/n}
"Your scouts will have to find another road. So will anyone who would have taken those papers from you."
{n}She gives you back the empty cover.{/n} "Bring me the account when you've finished with the ashes. I won't call this an apology."''',
          c("[Keep the cover for the inspection.]", flags=(*flags("retry.seen"), *ERASED[1:], BUNDLE_LOST))),
        n("refused", "Nidalynn", '''{n}She rolls the leaves again and puts them beside your pack.{/n} "Then they're still a road to living people. I won't thank you for carrying it farther."''',
          c("[Keep the bundle.]", flags=flags("retry.seen", "retry.refused", "unanswered", "chart.retained"))),
    ], requires=flags("chart.bundle_carried", "cost.nidalynn_memory_given"),
       forbids=flags("cell.chart_erased"), delay=48,
       groups=(flags("cell.failed", "cell.refused"),)))
    out.extend(private("receipt", "The cover without the road", '"Here is what remains of the chart."', [
        n("start", "Nidalynn", '''{n}Nidalynn holds out her hand for the mare-marked cover. Behind her, a refugee child tries to sound out the name on a broken clan brooch.{/n}
"Let me see it. And tell me what you burned. The ford, the boulder, the little slip. Don't leave anything out because you'd rather hear me say it's over."''',
          c("[Show the cover and describe the destruction of the original and pursuit slip.]", "inspected"),
          c('"Call it settled, without seeing it."', "refused"), later()),
        n("inspected", "Nidalynn", '''{n}She matches the raised foreleg to her stitching and feels along the empty binding. You name the split boulder and account for the original, the slip, and the research you lost.{/n}
"Good. There are people still hiding. You've made that harder to follow."
{n}She sets the cover beside her mending.{/n}
"Reudger is still dead. The pasture's still ash. She gave up leaves because she wants you at Threshold. I'll remember that too."''',
          c("[Leave the inspected cover with her.]", flags=flags("receipt.seen", "accounted", "cost.nidalynn_answer_heard", "no_absolution"))),
        n("refused", "Nidalynn", '''"No. Take it away, then. I asked to see what you brought, not to make you feel better about it." {n}Her hand drops to her lap.{/n}''',
          c("[Leave without the inspection.]", flags=flags("receipt.seen", "receipt.refused", "unanswered", "no_absolution"))),
    ], requires=flags("cell.chart_erased", "chart.original_burned", "chart.pursuit_slip_burned",
                      "cost.commander_research_lost"), delay=48))
    return out


def register(payload, scenes, refs):
    """Register only S51; called after route/presence/Last Call assembly."""
    payload.setdefault("Derived", {})[P + "ready"] = [[nd.MET]]
    # Native destruction is a read, never a terminal write or a replacement cue.
    payload.setdefault("SeenCues", {})[PROJECTOR_BROKEN] = ["591acfaf8500cc94aa7a8918db767d43"]
    additions = build_scenes()
    for body in additions:
        if body.get("InteractionHub"):
            presence = payload["Presences"][body["InteractionHub"]]
            body["Requires"] = list(dict.fromkeys([*body["Requires"], *(
                key for key in presence.get("Requires", []) if key != "trickster.ever")]))
            body["Forbids"] = list(dict.fromkeys([*body["Forbids"], *presence.get("Forbids", [])]))
            body["RequiresAnyGroups"].extend(presence.get("RequiresAnyGroups", []))
    existing = {s["Id"] for s in scenes}
    if existing.intersection(s["Id"] for s in additions):
        raise ValueError("S51 already registered")
    scenes.extend(additions)
    if payload["Scenes"] is not scenes:
        payload["Scenes"].extend(additions)
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None:
        ledger["Entries"].append(dict(
            Id="seating.s51.windstep", Section="Seating Notes", Portrait="Nidalynn", Title="Windstep",
            Text="{n}Nidalynn asked what became of the trail through the Windstep ruins.{/n}",
            Requires=list(flags("notice.seen")), Forbids=[], AnyGroups=[], Tooltip="RRT_SeatingNotes",
            Lines=[p("{n}The route through the Windstep ruins was burned. Nidalynn inspected what I brought back. The accusation remains.{/n}",
                     requires=flags("accounted", "no_absolution")),
                   p("{n}I left Nidalynn's complaint unanswered. Nothing in Areelu's notes made the lost pasture whole.{/n}",
                     requires=flags("unanswered")),
                   p("{n}I tried to keep useful leaves. The pursuit slip survived that first fire.{/n}",
                     requires=flags("cost.commander_copy_exposed")),
                   p("{n}Nidalynn entrusted me with the mare's brand and the first landmark. I had not brought back an inspected answer.{/n}",
                     requires=flags("notice.carried", "cost.nidalynn_memory_given"),
                     forbids=flags("accounted", "unanswered"))]))
    # Existing epilogue destinations only. Host guards retain presence/survival.
    readers = {
        "nidalynn.lastcall.page": "{n}Nidalynn kept the cover with the mare beneath the stars. She had inspected the answer brought from Areelu's cell; she had not forgiven the Architect. Reudger's name stayed beside the names of the warriors.{/n}",
        "nidalynn.trickster.epilogue.salt": "{n}The mare-marked cover remained by Nidalynn's mending. The trail through Windstep had burned, and with it a route the crusade could have used. She kept the accusation and the memory of Reudger the White.{/n}",
        "areelu.lastcall.page": "{n}Areelu had surrendered the Windstep field route to keep the Commander's attention on Threshold. The original and its pursuit slip had burned. Her larger work remained hers; Nidalynn's accusation remained against it.{/n}",
    }
    for host in scenes:
        if host["Id"] in ("areelu.trickster.wager.struck", "areelu.trickster.rivalry.lens"):
            # Append a recollection, preserving every original answer index/text.
            # Ordinary dialogue uses a node, never an epilogue paragraph.
            root = host["Nodes"][0]
            root["Choices"].append(c('"You gave up the Windstep field route."', "s51_field_route",
                                     requires=flags("cost.areelu_field_notes_lost", "cell.chart_erased")))
            host["Nodes"].append(n("s51_field_route", "Areelu",
                '''"I gave up a route through the ruins. You burned the original and its pursuit slip. Your scouts lost something useful too."
"Do you imagine I have forgotten how I found it? I have not. I chose which work to sacrifice. Nidalynn has her answer; I still expect mine at Threshold."''',
                c("[Return to the matter at hand.]", root["Id"])))
        if host["Id"] in readers:
            host["Nodes"][0].setdefault("Paragraphs", []).append(p(
                readers[host["Id"]], requires=flags("accounted", "no_absolution", "cost.areelu_field_notes_lost")))
        if host["Id"] in ("nidalynn.lastcall.page", "areelu.lastcall.page"):
            host["Nodes"][0].setdefault("Paragraphs", []).append(p(
                "{n}The Windstep complaint had gone unanswered. The lost pasture had not been made whole.{/n}",
                requires=flags("unanswered")))
            host["Nodes"][0].setdefault("Paragraphs", []).append(p(
                "{n}The Windstep complaint still lacked an inspected answer. Nidalynn's mare-marked cloth had been carried to no conclusion.{/n}",
                requires=flags("notice.carried"), forbids=flags("accounted", "unanswered")))

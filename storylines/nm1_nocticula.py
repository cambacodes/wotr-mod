"""NM1 (2026-10-01): the Nocticula acquired chain within its Chapter 5 budget.

Coordinator ruling: consolidate the acquired correspondence's Chapter 5 letters to the tier-B allocation (05 §4: two
Chapter 5 deliveries for a woman who cannot be met in person on Trickster) and defer the optional harbor content.

- **Consolidation.** The six correspondence scenes (the missing line, her hand, the borrowed signature, the paid address,
  the retained copy, her own answer) arrive as two deliveries. Each later letter is folded into the delivery before it:
  its nodes are copied after a short narrated wait (ids prefixed with the letter's key), and the host's terminal
  choices that set the letter's own prerequisite now continue into it. The folded letter's own terminal choices still
  set its `_done` flags, so its standalone scene (which forbids them) never arrives a second time. Save-safe: every
  scene, node and choice id and every choice index is kept; a save already between two letters still receives the next
  one standalone.
- **Deferral.** The harbor join (`noct.join.*`) and the acquired harbor copies (`*.acquired.*`) are retired by gating
  (they forbid `chapter_later`, which the runtime holds from Chapter 2 on), past the beta. Ids, nodes and choices are
  kept. The acquired correspondence gets its own closing page, so its commitment is not left without an ending.
"""
import copy

from story_format import c, n, scene
from storylines.nm1_fold import fold

DEFERRED = "chapter_later"   # runtime-held in every chapter from 2 on: retired by gating (Nurah DEAD_RETIRED precedent)
P = "noct.acq."

# (host, guest, the flag the guest's standalone scene requires from the host, the narrated wait between them)
FOLDS = (
    ("the_missing_line", "her_hand", P + "question_sent",
     '''{n}You put the packet in the drawer with the seal face down and go back to the war. It stays quiet for the rest of that night and most of the next day.{/n}'''),
    ("the_missing_line", "borrowed_signature", P + "her_hand_done",
     '''{n}The completed stroke does not move again for two days. On the third, a clerk brings up something that is not hers.{/n}'''),
    ("the_paid_address", "the_retained_copy", P + "the_paid_address_done",
     '''{n}You send the account through the wax that evening. Her answer is waiting under the seal the next morning, as if it had been written before yours arrived.{/n}'''),
    ("the_paid_address", "an_answer_of_her_own", P + "the_retained_copy_done",
     '''{n}The clean sheet stays clean through a day of dispatches. Late on the second evening, the mark beside your name begins to move.{/n}'''),
)

EPILOGUE = scene("noct.acq.epilogue.correspondence", "An answer kept", "Epilogue", 5, "", [
    n("page", "Narrator", '''{n}The half-seal stayed in a drawer in the Commander's rooms long after the crusade had left Drezen. On certain nights its mark moved without warning: a question, a sum corrected in another hand, once a single line about a broker in Alushinyrra who had tried to sell her name a second time and had not been seen since. The Commander answered every one of them, in ink, in person, at whatever hour the wax chose.{/n}
{n}Nobody else was allowed to open that drawer. One steward tried. He would not say afterwards what had answered him, only that it had called him by his mother's name and asked whether she knew where he slept.{/n}''',
      c())],
    requires=(P + "renewed_agreement",), forbids=("noct.complete", "noct.closed", P + "closed", "noct.dead", P + "council_fight", "sacrifice"),
    last=99, Relationship="nocticula.acquisition", ForbidOverrides={"sacrifice": "trickster.commander_back"})


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for host, guest, gate, wait in FOLDS:
        fold(scenes[P + host], scenes[P + guest], gate, wait, guest)
    deferred = 0
    for s in payload["Scenes"]:
        if s["Id"].startswith("noct.join.") or (s.get("Relationship") == "nocticula" and ".acquired." in s["Id"]
                                                 and not s["Owner"].endswith("Epilogue")):
            if DEFERRED not in s["Forbids"]:
                s["Forbids"].append(DEFERRED)
            deferred += 1
    if deferred < 3:
        raise ValueError("nm1: the harbor join and the acquired harbor were not found")
    # The deferred harbor is not advertised (Sol INT): the guidance names what the correspondence actually leads to.
    rel = payload["Relationships"]["nocticula"]
    old = "After completing the Trickster correspondence and accepting the hosted meetings, rest in Drezen to hear Nocticula's harbor proposal. "
    if old not in rel["Guidance"]:
        raise ValueError("nm1: the Nocticula guidance changed")
    rel["Guidance"] = rel["Guidance"].replace(old, "The Trickster correspondence ends in its own agreement, kept by letter. ")
    if EPILOGUE["Id"] in scenes:
        raise ValueError("nm1: duplicate " + EPILOGUE["Id"])
    payload["Scenes"].append(copy.deepcopy(EPILOGUE))

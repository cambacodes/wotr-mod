"""eng7-l14: guard live cross-route prose with existing, earned availability.

No commitment, attraction, page purchase or new return is required. Ordinary
book scenes which depend on a live guest read her route's existing losses and
earned overrides. Epilogue cameos are optional paragraphs, so an absent guest
does not extinguish the route owner's page. Existing IDs and answer positions
are retained. History and mourning use the same conservative L1 classifier.
"""
import copy

from tools.crossroute_checks.common import Block, AND, OR, Proof, blocks, fields, roster, verify, postwar, lit
from tools.crossroute_checks.other_woman import presence_guard, correspondence_reference, local_return_overrides, LIVING_AFTER_ROMANCE_REFUSAL, NATIVE_COMPANIONS, BODY_RETURNS, PRESENCE_LOSSES, NATIVE_AUDIENCES
from tools.crossroute_checks.mention_context import live_mentions


def availability(payload, woman, route, known=None, distant=False, native_audience=False):
    """A live predicate; never a latch on yesterday's availability.

    Use the runtime chapter inputs as a tautology in Chapters 1–6. Prologue
    scenes use direct scene forbids instead. Independent relationships read
    current losses; legacy pair seats read only the named woman's own losses.
    """
    key = "crossroute.%s.%s" % (woman, "native_available" if native_audience else "correspondent" if distant else "available")
    derived = payload.setdefault("Derived", {})
    if key in derived:
        return key
    # All real Chapters 1–6 have one ChapterFlag. The equivalent historical
    # Trickster arm also supports existing rules snapshots which call Complete
    # without the native ChapterFlag reader; it grants no loss/return bypass.
    groups = [["chapter_one"], ["chapter_later"], ["trickster.ever"]]
    seat = (payload.get("SeatWomen") or {}).get(woman)
    rel = payload["Relationships"][route]
    rel = dict(rel, UnavailableFlags=[*rel.get("UnavailableFlags", []), *PRESENCE_LOSSES.get(woman, [])])
    if distant:
        rel = dict(rel, UnavailableFlags=[f for f in rel.get("UnavailableFlags", []) if f != woman + "_gone"])
    if known is not None and any(f not in known for f in rel.get("UnavailableFlags", [])):
        # An existing opaque route input can be read only through the central
        # RouteOpen reader, not manufactured as a new bound flag here.
        derived[key] = groups
        payload.setdefault("DerivedOpenRoutes", {})[key] = [route]
        return key
    other = {f for name, spec in (payload.get("SeatWomen") or {}).items()
             if seat and spec["Relationship"] == route and name != woman
             for f in spec.get("UnavailableFlags", [])}
    overrides = {**rel.get("UnavailableOverrides", {}), **(seat or {}).get("UnavailableOverrides", {})}
    inputs = []
    if woman in BODY_RETURNS:
        inputs.extend(["trickster.ever", BODY_RETURNS[woman]])
    if woman in NATIVE_COMPANIONS:
        open_key, native_key, closure_key = key + ".romance_open", key + ".native_undeparted", key + ".closure_eligible"
        derived[open_key] = copy.deepcopy(groups)
        payload.setdefault("DerivedForbids", {})[open_key] = [rel["ClosedFlag"]]
        derived[native_key] = copy.deepcopy(groups)
        payload.setdefault("DerivedForbids", {})[native_key] = list(rel.get("UnavailableFlags", []))
        derived[closure_key] = [[open_key], [native_key]]
        inputs.append(closure_key)
    elif woman not in LIVING_AFTER_ROMANCE_REFUSAL and not native_audience:
        payload.setdefault("DerivedForbids", {})[key] = [rel["ClosedFlag"]]
    for i, loss in enumerate(f for f in rel.get("UnavailableFlags", []) if f not in other):
        if loss not in overrides:
            payload.setdefault("DerivedForbids", {}).setdefault(key, []).append(loss)
            continue
        clear = key + ".clear%d" % i
        derived[clear] = copy.deepcopy(groups)
        payload.setdefault("DerivedForbids", {})[clear] = [loss]
        answered = key + ".loss%d" % i
        derived[answered] = [[clear], [overrides[loss]]]
        inputs.append(answered)
    derived[key] = [list(dict.fromkeys(g + inputs)) for g in groups]
    return key


def unavailability(payload, woman, route, known=None, distant=False):
    key = availability(payload, woman, route, known, distant)
    absent = "crossroute.%s.%s" % (woman, "correspondent_unavailable" if distant else "unavailable")
    payload.setdefault("Derived", {})[absent] = [["chapter_one"], ["chapter_later"], ["trickster.ever"]]
    payload.setdefault("DerivedForbids", {})[absent] = [key]
    return absent


def scene_guard(scene, payload, woman, route, known=None, distant=False):
    # The composite reads existing losses and returns without requiring
    # another romance's progression. Register it as the participant contract.
    audience = NATIVE_AUDIENCES.get(woman)
    window = set(scene.get("Chapters") or range(scene.get("MinChapter", 0), scene.get("MaxChapter", 99) + 1))
    if (window != {0} and audience and audience[0] in scene.get("AnswerLists", [])
            and window <= audience[1] and scene.get("NativeReturnCue")):
        key = availability(payload, woman, route, known, distant, native_audience=woman == "nocticula")
        # eng7-l14: native inline audiences retain their fixed Requires/
        # Forbids lists. RequiresAnyGroups conjoins its OR groups: append a
        # singleton group so no existing alternative can bypass presence.
        groups = scene.setdefault("RequiresAnyGroups", [])
        if [key] not in groups:
            groups.append([key])
        return
    key = availability(payload, woman, route, known, distant)
    rel = payload["Relationships"][route]
    rel = dict(rel, UnavailableFlags=[*rel.get("UnavailableFlags", []), *PRESENCE_LOSSES.get(woman, [])])
    if distant:
        rel = dict(rel, UnavailableFlags=[f for f in rel.get("UnavailableFlags", []) if f != woman + "_gone"])
    if window == {0} and woman in NATIVE_COMPANIONS:
        # eng7-l14: ChapterFlag deliberately has no Prologue input. The
        # native audience still reads current loss flags directly; requiring
        # the Chapters 1–6 composite would hide her canonical introduction.
        for loss in rel.get("UnavailableFlags", []):
            if loss not in scene.setdefault("Forbids", []):
                scene["Forbids"].append(loss)
        return
    # eng7-l14: guest-state reader contracts apply across routes. Keep life,
    # closure and body exclusions inside the same live composite. Only the
    # existing Long Con native-host adapter needs its scoped gone override;
    # native reactions retain direct losses where their reader contract allows.
    foreign_state = {spec[f] for name, spec in payload["Relationships"].items()
                     if name != scene.get("Relationship", "tirabade")
                     for f in ("StartedFlag", "ClosedFlag", "CommittedFlag") if f in spec}
    native_reaction = scene.get("Reaction") and not any(
        f in foreign_state for f in rel.get("UnavailableFlags", []))
    direct_contract = local_return_overrides(payload, scene, woman) or native_reaction
    if not direct_contract:
        # Presence is an exclusion, not a newly timed prerequisite. Existing
        # DelayHours must still start at the route's original paid/event flag.
        absent = unavailability(payload, woman, route, known, distant)
        if absent not in scene.setdefault("Forbids", []):
            scene["Forbids"].append(absent)
        return
    if woman in BODY_RETURNS:
        for flag in ("trickster.ever", BODY_RETURNS[woman]):
            if flag not in scene.setdefault("Requires", []):
                scene["Requires"].append(flag)
    if woman not in LIVING_AFTER_ROMANCE_REFUSAL:
        closed = rel["ClosedFlag"]
        if closed not in scene.setdefault("Forbids", []):
            # Foreign relationship-state forbids are not valid on reactions.
            if scene.get("Reaction"):
                absent = unavailability(payload, woman, route, known, distant)
                if absent not in scene.setdefault("Forbids", []):
                    scene["Forbids"].append(absent)
            else:
                scene["Forbids"].append(closed)
    seat = (payload.get("SeatWomen") or {}).get(woman)
    other = {f for name, spec in (payload.get("SeatWomen") or {}).items()
             if seat and spec["Relationship"] == route and name != woman
             for f in spec.get("UnavailableFlags", [])}
    overrides = {**rel.get("UnavailableOverrides", {}), **(seat or {}).get("UnavailableOverrides", {})}
    local = local_return_overrides(payload, scene, woman)
    for loss in (f for f in rel.get("UnavailableFlags", []) if f not in other):
        if loss not in scene.setdefault("Forbids", []):
            scene["Forbids"].append(loss)
            if loss in overrides:
                scene.setdefault("ForbidOverrides", {})[loss] = overrides[loss]
        elif scene.get("ForbidOverrides", {}).get(loss) and scene["ForbidOverrides"][loss] != overrides.get(loss) and loss not in local:
            # Keep the old stricter scene contract, but an unrelated local
            # override must not lift a departure the woman's route cannot lift.
            if key not in scene.setdefault("Requires", []):
                scene["Requires"].append(key)


def integrate(payload):
    """One class sweep after all route generators and central registrations."""
    # Route helpers reuse loss/override dictionaries across scenes. Isolate
    # each scene before adding guards: deep-copying the entire list would
    # preserve those aliases and leak a guest's override into unrelated pages.
    payload["Scenes"] = [copy.deepcopy(s) for s in payload["Scenes"]]
    # eng7-l14 authored temporal clarifications: campaign harm receipts and
    # remembered counsel survive subsequent deaths/departures. Preserve those
    # facts without attributing current action to an absent woman.
    counsel = {
        ("soana.ending_native_loss", "camellia"): ("Camellia killed Soana.", "During the crusade, Camellia killed Soana."),
        ("soana.ending_unfinished_loss", "camellia"): ("Camellia killed Soana.", "During the crusade, Camellia killed Soana."),
        ("irabeth.a_name_on_the_list", "company"): ("Nevi says I built", "Nevi once said I built"),
        ("irabeth.without_an_account", "want"): ("Nevi says it's my worst tactic.", "Nevi once said it's my worst tactic."),
        ("anevia.a_key_that_is_hers", "room"): ("Beth says I should learn", "Beth once said I should learn"),
        ("anevia.trickster.gone.gate", "told"): ("Beth snores", "Beth used to snore"),
        ("irabeth.trickster.commit", "no"): ("Nevi's out on that road. I'm not doing this behind her back. Not while she's out there. Maybe not after.",
            "Nevi left Drezen. I'm not doing this behind her back. Maybe I never will."),
    }
    for scene in payload["Scenes"]:
        for node in scene["Nodes"]:
            pair = counsel.get((scene["Id"], node["Id"]))
            if pair:
                node["Text"] = node["Text"].replace(*pair)
    # eng-final: temporal corrections and the new widow variant must not
    # inherit unselected Commander dialogue. Preserve all node/answer IDs.
    for scene in payload["Scenes"]:
        for node in scene["Nodes"]:
            if (scene["Id"], node["Id"]) == ("anevia.a_key_that_is_hers", "room"):
                node["Text"] = node["Text"].replace('\n"Would it fit here?"', "").replace(
                    '"No. And I won\'t put it here.', '"I won\'t put it here.').replace(
                    '\n"You want that with Irabeth."', "").replace('"\n"', " ")
            elif (scene["Id"], node["Id"]) == ("irabeth.the_question_outside_duty", "rank"):
                node["Text"] = node["Text"].replace('"And away from council?"\n', "").replace('"\n"', " ")
    # eng7-l14 authored neutral variant: the original widow negotiation
    # passes through a page promising nights with Anevia. Preserve that page
    # and its incoming answer indices, and append the same boundary without
    # the living-wife promise for unavailable-wife worlds.
    for scene in payload["Scenes"]:
        if scene["Id"] != "irabeth.the_question_outside_duty":
            continue
        variant_id = "eng7_l14.rank_without_wife"
        if any(n["Id"] == variant_id for n in scene["Nodes"]):
            continue
        rank = next(n for n in scene["Nodes"] if n["Id"] == "rank")
        neutral = copy.deepcopy(rank)
        neutral["Id"] = variant_id
        neutral["Text"] = neutral["Text"].replace("Some nights I'll have promised Nevi.",
                                                 "Some nights I'll want an evening alone.")
        key = availability(payload, "anevia", "anevia")
        absent = unavailability(payload, "anevia", "anevia")
        # Keep the existing native death input on answers. Besides being a
        # direct witness, it keeps original traversal fixtures meaningful
        # without asking them to synthesize new runtime composite inputs.
        death = next(f for f in payload["Relationships"]["anevia"]["UnavailableFlags"]
                     if f not in payload["Relationships"]["anevia"].get("UnavailableOverrides", {}))
        for node in scene["Nodes"]:
            additions = []
            for choice in node["Choices"]:
                if choice.get("Next") != "rank":
                    continue
                bereaved = copy.deepcopy(choice)
                bereaved["Next"] = variant_id
                bereaved.setdefault("Requires", []).append(death)
                alternate = copy.deepcopy(choice)
                alternate["Next"] = variant_id
                alternate.setdefault("Requires", []).append(absent)
                alternate.setdefault("Forbids", []).append(death)
                choice.setdefault("Forbids", []).extend([absent, death])
                additions.extend([bereaved, alternate])
            node["Choices"].extend(additions)
        scene["Nodes"].append(neutral)
    # eng7-integ5 authored absence variant: Seelah's native soul-rescue
    # aftermath belongs to the rescued people, including when Arsinoe's
    # existing loss/busy flags bar a visit. Keep the original priestess
    # branch and ending, and append the same aftercare without that visit.
    for scene in payload["Scenes"]:
        if scene["Id"] != "seelah.souls" or "arsinoe" not in payload["Relationships"]:
            continue
        variant_id = "eng7_l14.end_without_arsinoe"
        if any(n["Id"] == variant_id for n in scene["Nodes"]):
            continue
        ending = next(n for n in scene["Nodes"] if n["Id"] == "end")
        neutral = copy.deepcopy(ending)
        neutral["Id"] = variant_id
        neutral["Text"] = neutral["Text"].replace(
            "speak to Arsinoe about the people who still need help",
            "visit the people who still need help")
        available = availability(payload, "arsinoe", "arsinoe")
        absent = unavailability(payload, "arsinoe", "arsinoe")
        for node in scene["Nodes"]:
            additions = []
            for choice in node["Choices"]:
                if choice.get("Next") != "end":
                    continue
                alternate = copy.deepcopy(choice)
                alternate["Next"] = variant_id
                alternate.setdefault("Forbids", []).append(available)
                choice.setdefault("Forbids", []).append(absent)
                additions.append(alternate)
            node["Choices"].extend(additions)
        scene["Nodes"].append(neutral)
    # eng7-l14: the native south-road branch still names a living Irabeth.
    # If another recorded loss now makes her unavailable, use the existing
    # reproach/killer page rather than stage her through the wall. Append
    # neutral answers; keep every original target and answer index.
    for scene in payload["Scenes"]:
        neutral_id = {"anevia.trickster.gone.wardrobe": "beth_dead",
                      "anevia.trickster.gone.gate": "beth_widow"}.get(scene["Id"])
        if neutral_id is None:
            continue
        ids = {n["Id"] for n in scene["Nodes"]}
        if not {"beth_left", neutral_id} <= ids:
            continue
        absent = unavailability(payload, "irabeth", "irabeth", distant=True)
        if scene["Id"] == "anevia.trickster.gone.gate":
            full_absent = unavailability(payload, "irabeth", "irabeth")
            for node in scene["Nodes"]:
                additions = []
                for choice in list(node["Choices"]):
                    if choice.get("Next") != "beth_back":
                        continue
                    if any(c.get("Next") == neutral_id and full_absent in c.get("Requires", []) for c in node["Choices"]):
                        continue
                    neutral = copy.deepcopy(choice)
                    neutral["Next"] = neutral_id
                    neutral.setdefault("Requires", []).append(full_absent)
                    additions.append(neutral)
                node["Choices"].extend(additions)
        for node in scene["Nodes"]:
            additions = []
            for choice in list(node["Choices"]):
                if choice.get("Next") != "beth_left":
                    continue
                if any(c.get("Next") == neutral_id and absent in c.get("Requires", []) for c in node["Choices"]):
                    continue
                neutral = copy.deepcopy(choice)
                neutral["Next"] = neutral_id
                neutral.setdefault("Requires", []).append(absent)
                additions.append(neutral)
                if "killer" in ids:
                    neutral.setdefault("Forbids", []).append("anevia.irabeth_killed_by_commander")
                    killed = copy.deepcopy(choice)
                    killed["Next"] = "killer"
                    killed.setdefault("Requires", []).extend([absent, "anevia.irabeth_killed_by_commander"])
                    additions.append(killed)
            node["Choices"].extend(additions)
    # eng7-l14: a prior resurrection does not place a subsequently departed
    # Irabeth back inside Drezen. Keep the live share_quiet page, and append
    # its existing south-road account for that unavailable-location history.
    for scene in payload["Scenes"]:
        if scene["Id"] != "anevia.trickster.gone.commit":
            continue
        absent = unavailability(payload, "irabeth", "irabeth")
        for node in scene["Nodes"]:
            additions = []
            for choice in list(node["Choices"]):
                if choice.get("Next") != "share_quiet":
                    continue
                if any(c.get("Next") == "left" and absent in c.get("Requires", []) for c in node["Choices"]):
                    continue
                neutral = copy.deepcopy(choice)
                neutral["Next"] = "left"
                # The existing left page recounts her south-road departure.
                # Read that native departure directly as well, so a return
                # added after a completed snapshot cannot select a stale
                # unavailable-wife fallback in an otherwise present world.
                neutral.setdefault("Requires", []).extend([absent, "irabeth_gone"])
                additions.append(neutral)
            node["Choices"].extend(additions)
    # eng7-l14: the fetched-history callback mixes an already completed
    # return with a future living-wife visit. Keep the historical receipt at
    # its original paragraph index and append the optional living variant.
    fetched_history = "Whenever the Commander asked, she said she had come back because Beth had fetched her."
    fetched_visit = "Whenever Beth was in the room, she said it was the other way round."
    for scene in payload["Scenes"]:
        if not scene.get("Owner", "").endswith("Epilogue") or "irabeth" not in payload["Relationships"]:
            continue
        for node in scene["Nodes"]:
            additions = []
            for paragraph in node.get("Paragraphs", []):
                if paragraph.get("Text") != fetched_history + " " + fetched_visit:
                    continue
                variant = copy.deepcopy(paragraph)
                paragraph["Text"] = fetched_history
                variant["Text"] = fetched_visit
                variant.setdefault("Requires", []).append(availability(payload, "irabeth", "irabeth"))
                additions.append(variant)
            node.setdefault("Paragraphs", []).extend(additions)
    model = verify.Model(copy.deepcopy(payload))
    names = roster(model)
    known = (model.authored | set(model.native) | model.builtin_derived
             | set(model.composites) | set(model.latches) | set(payload.get("PendingHooks", [])))
    if not payload.get("Etudes"):
        known = None   # symbolic, partial test stories have no binding registry
    originals = {s["Id"]: s for s in payload["Scenes"]}
    from tools.crossroute_checks.other_woman import native_participation_contexts
    native_contexts = native_participation_contexts(model)
    # If an unreturned body loss excludes both the owner and a live guest,
    # there is no legitimate owner-only scene to preserve in that history.
    # Read the shared loss at entry. Keep every local/registered earned
    # override; in particular, a returned wife never inherits a raw death veto.
    for scene in payload["Scenes"]:
        if scene.get("Kind") in ("memory", "dream") or postwar(scene):
            continue
        own_route = scene.get("Relationship", "tirabade")
        own = payload["Relationships"].get(own_route, {})
        own_overrides = {**own.get("UnavailableOverrides", {}), **scene.get("ForbidOverrides", {})}
        texts = [scene.get("Entry", ""), scene.get("ReturnText", "")]
        for node in scene["Nodes"]:
            texts.extend([node.get("Text", ""), *(p.get("Text", "") for p in node.get("Paragraphs", [])),
                          *(c.get("Text", "") for c in node["Choices"])])
        for woman, (route, pattern) in names.items():
            if (route == own_route or own_route.startswith(woman + ".")
                    or (payload.get("SeatWomen", {}).get(woman) or {}).get("Relationship") == own_route):
                continue
            if not (any(live_mentions(t, pattern, postwar(scene), scene["Id"]) for t in texts)
                    or any(pattern.fullmatch(n.get("Speaker", "")) for n in scene["Nodes"])):
                continue
            guest = payload["Relationships"][route]
            for loss in own.get("UnavailableFlags", []):
                if (loss in {"swarm", "true_lich", "inhuman"} and loss in guest.get("UnavailableFlags", []) and loss not in own_overrides
                        and loss not in guest.get("UnavailableOverrides", {})
                        and loss not in scene.setdefault("Forbids", [])):
                    scene["Forbids"].append(loss)
    # Split mixed ending narration once, considering every woman together.
    # Keep existing paragraph indices: each optional cameo appends at the end.
    import re
    for scene in payload["Scenes"]:
        if (not scene.get("Owner", "").endswith("Epilogue")
                or scene.get("Kind") in ("memory", "dream")):
            continue
        for node in scene["Nodes"]:
            units = re.split(r"(?<=\{/n\})\s*(?=\{n\})", node.get("Text", ""))
            variants, neutral = [], []
            for unit in units:
                guests = [(w, r) for w, (r, p) in names.items()
                          if r != scene.get("Relationship", "tirabade")
                          and (payload.get("SeatWomen", {}).get(w) or {}).get("Relationship") != scene.get("Relationship", "tirabade")
                          and not scene.get("Relationship", "tirabade").startswith(w + ".")
                          and live_mentions(unit, p, True, scene["Id"])]
                if guests:
                    variants.append(dict(Text=unit, Requires=[availability(payload, w, r, known) for w, r in guests]))
                else:
                    neutral.append(unit)
            if variants and any(t.strip() for t in neutral):
                node["Text"] = "\n".join(neutral).strip()
                node.setdefault("Paragraphs", []).extend(variants)
    # Rebuild after splitting so a second guest cannot accidentally gate the
    # owner's whole page, or escape the first guest's optional variant.
    model = verify.Model(copy.deepcopy(payload))
    scene_guests, pending_choices = set(), []
    contexts = {(b.scene["Id"], b.node["Id"], b.slot): b.context for b in blocks(model)}
    proof = Proof(model)
    def guard_scene(scene, woman, route, distant=False):
        original_forbids = set(scene.get("Forbids", []))
        scene_guard(scene, payload, woman, route, known, distant)
        closed = payload["Relationships"][route]["ClosedFlag"]
        root = scene["Nodes"][0]["Id"] if scene["Nodes"] else None
        context = contexts.get((scene["Id"], root, "text"))
        if (closed not in original_forbids and closed in scene.get("Forbids", [])
                and context is not None and proof.implies(context, lit(closed, False))):
            # Existing RouteOpen/entry contracts already exclude this closure.
            # Keep that indirect reader rather than adding forbidden foreign
            # romance-fate dependencies to a continuation's native schema.
            scene["Forbids"].remove(closed)
        scene_guests.add((scene["Id"], woman, distant))
    def guard_choice(choice, context, woman, route, distant=False):
        # Read native flags directly when the edge already proves every earned
        # override. This also honours a return recorded after a rules snapshot
        # was completed, instead of retaining its earlier composite absence.
        rel = payload["Relationships"][route]
        seat = (payload.get("SeatWomen") or {}).get(woman)
        other = {f for name, spec in (payload.get("SeatWomen") or {}).items()
                 if seat and spec["Relationship"] == route and name != woman
                 for f in spec.get("UnavailableFlags", [])}
        losses = [f for f in (*rel.get("UnavailableFlags", []), *PRESENCE_LOSSES.get(woman, []))
                  if f not in other and not (distant and f == woman + "_gone")]
        overrides = {**rel.get("UnavailableOverrides", {}), **(seat or {}).get("UnavailableOverrides", {})}
        required = (["trickster.ever", BODY_RETURNS[woman]] if woman in BODY_RETURNS else [])
        if (context is not None and (known is None or all(f in known for f in losses))
                and all(proof.implies(context, OR(lit(f, False), lit(overrides[f]))) for f in losses if f in overrides)
                and all(proof.implies(context, lit(f)) for f in required)):
            vetoes = [f for f in losses if f not in overrides]
            if woman in NATIVE_COMPANIONS and not proof.implies(context, presence_guard(model, route, woman)):
                absent = unavailability(payload, woman, route, known, distant)
                if absent not in choice.setdefault("Forbids", []):
                    choice["Forbids"].append(absent)
                return
            if woman not in LIVING_AFTER_ROMANCE_REFUSAL | NATIVE_COMPANIONS:
                vetoes.append(rel["ClosedFlag"])
            for flag in vetoes:
                if flag not in choice.setdefault("Forbids", []):
                    choice["Forbids"].append(flag)
        else:
            absent = unavailability(payload, woman, route, known, distant)
            if absent not in choice.setdefault("Forbids", []):
                choice["Forbids"].append(absent)
    def guard_branch(scene, nid, woman, route, distant=False):
        # Optional guest branches can be excluded without suppressing the
        # owner's neutral/refusal answers. Move the guard up a single-answer
        # chain until every incoming edge has a provably selectable alternative.
        window = set(scene.get("Chapters") or range(scene.get("MinChapter", 0), scene.get("MaxChapter", 99) + 1))
        if 0 in window:
            return False   # chapter composites do not exist in the Prologue
        indexed = model.walk_index()[scene["Id"]][2]
        key = availability(payload, woman, route, known, distant)
        absent = unavailability(payload, woman, route, known, distant)
        fallbacks = []
        def edges(target, trail=()):
            if target in trail or target == scene["Nodes"][0]["Id"]:
                return None
            proposed = []
            for parent in scene["Nodes"]:
                incoming = [(i, c) for i, c in enumerate(parent["Choices"])
                            if i < len(indexed[parent["Id"]]) and target in indexed[parent["Id"]][i][-1]]
                for i, choice in incoming:
                    others = [fields(c) for j, c in enumerate(parent["Choices"]) if j != i]
                    context = contexts.get((scene["Id"], parent["Id"], "text"))
                    # A native present etude can survive a later death. Retain
                    # the existing no-guest branch in that history by appending
                    # its answers, with only the obsolete presence veto lifted.
                    # No costs, targets or original answer indices change.
                    present = next((flag for flag in (woman + ".present", woman + "_gone")
                                    if flag in choice.get("Requires", []) and flag in payload.get("Etudes", {})), None)
                    alternates = []
                    if present:
                        for j, other in enumerate(parent["Choices"]):
                            if j == i or present not in other.get("Forbids", []):
                                continue
                            fallback_target = next((n for n in scene["Nodes"] if n["Id"] == other.get("Next")), None)
                            if fallback_target and (names[woman][1].fullmatch(fallback_target.get("Speaker", ""))
                                           or live_mentions(fallback_target.get("Text", ""), names[woman][1], postwar(scene), scene["Id"])):
                                continue   # an unavailable guest needs a neutral target
                            alternate = copy.deepcopy(other)
                            alternate["Forbids"].remove(present)
                            alternate.setdefault("Requires", []).extend([present, absent])
                            alternates.append(alternate)
                        # The proposed absence reader is equivalent to !key;
                        # the pre-pass Model does not yet contain its definition.
                        others.extend(AND(lit(key, False), fields(dict(c, Requires=[f for f in c["Requires"] if f != absent])))
                                      for c in alternates)
                    if context is not None and proof.implies(AND(context, lit(key, False)), OR(*others)):
                        proposed.append(choice)
                        fallbacks.extend((parent, c) for c in alternates)
                    else:
                        preceding = edges(parent["Id"], (*trail, target))
                        if preceding is None:
                            return None
                        proposed.extend(preceding)
            return proposed or None
        proposed = edges(nid)
        if proposed is None:
            return False
        for choice in proposed:
            for parent in scene["Nodes"]:
                if any(c is choice for c in parent["Choices"]):
                    index = next(i for i, c in enumerate(parent["Choices"]) if c is choice)
                    guard_choice(choice, contexts.get((scene["Id"], parent["Id"], "choice[%d]" % index)), woman, route, distant)
                    break
        for parent, alternate in fallbacks:
            if alternate not in parent["Choices"]:
                parent["Choices"].append(alternate)
        return True
    def authored_blocks():
        # Generation does not need SAT/path analysis: a syntactically live
        # claim always receives the same guard, including retired old nodes.
        for s in model.scenes:
            for field in ("Entry", "ReturnText"):
                if s.get(field):
                    yield Block(s, {"Id": "@" + field}, s, field, s[field], AND())
            for n in s["Nodes"]:
                yield Block(s, n, n, "text", n["Text"], AND())
                for i, p in enumerate(n["Paragraphs"]):
                    yield Block(s, n, p, "paragraph[%d]" % i, p.get("Text", ""), AND())
                for i, c in enumerate(n["Choices"]):
                    yield Block(s, n, c, "choice[%d]" % i, c["Text"], AND())
    for block in authored_blocks():
        if block.scene.get("Kind") in ("memory", "dream"):
            continue
        scene = originals[block.scene["Id"]]
        node = next((n for n in scene["Nodes"] if n["Id"] == block.node["Id"]), None)
        for woman, (route, pattern) in names.items():
            seat = (payload.get("SeatWomen") or {}).get(woman, {})
            if route == block.route or seat.get("Relationship") == block.route or block.route.startswith(woman + "."):
                continue
            native = native_contexts.get(block.scene["Id"], {})
            if any(pattern.fullmatch(name) for name in native.get("Speakers", [])) or pattern.search(native.get("Mentions", "")):
                continue  # inherited native participation, validated against the original cue graph
            speaking = block.slot == "text" and pattern.fullmatch(block.node.get("Speaker", ""))
            if not speaking and not live_mentions(block.text, pattern, postwar(block.scene), block.scene["Id"]):
                continue
            # An original branch may already exclude every live loss. Read
            # its incoming answers as well as its own fields before gating a
            # whole scene: a living-wife branch must not suppress mourning.
            distant = correspondence_reference(block, woman)
            availability(payload, woman, route, known, distant)
            context = contexts.get((block.scene["Id"], block.node["Id"], block.slot))
            if context is not None and proof.implies(context, presence_guard(model, route, woman, block)):
                continue
            # Existing live guards remain valid; add an explicit book meeting
            # contract for physical guest staging as well as missing losses.
            if block.slot.startswith("paragraph["):
                i = int(block.slot[10:-1])
                paragraph = node["Paragraphs"][i]
                key = availability(payload, woman, route, known)
                if key not in paragraph.setdefault("Requires", []):
                    paragraph["Requires"].append(key)
            elif block.scene["Owner"].endswith("Epilogue") and block.slot == "text" and not speaking:
                # Full narration units, not fragments of a sentence. Existing
                # paragraph indices remain untouched; new variants append.
                units = re.split(r"(?<=\{/n\})\s*(?=\{n\})", node.get("Text", ""))
                live, neutral = [], []
                for unit in units:
                    (live if live_mentions(unit, pattern, True, scene["Id"]) else neutral).append(unit)
                if live and neutral:
                    node["Text"] = "\n".join(neutral).strip()
                    node.setdefault("Paragraphs", []).append(dict(Text="\n".join(live).strip(),
                        Requires=[availability(payload, woman, route, known)]))
                else:
                    guard_scene(scene, woman, route)
            elif block.slot.startswith("choice["):
                i = int(block.slot[7:-1])
                choice = node["Choices"][i]
                pending_choices.append((scene["Id"], choice, woman, route, distant, block))
            else:
                if block.slot != "text" or not guard_branch(scene, block.node["Id"], woman, route, distant):
                    guard_scene(scene, woman, route, distant)
    # Existing guarded branches already establish life, including their
    # descendants. Preserve these answers instead of adding a redundant
    # positive composite which test traversal cannot refresh mid-scene.
    for sid, choice, woman, route, distant, block in pending_choices:
        # An entry guard already excludes this guest's losses. Do not require
        # a second composite on every Continue answer: book traversal need not
        # manufacture a ChapterFlag or refresh entry-only runtime inputs.
        if (sid, woman, distant) in scene_guests or (sid, woman, False) in scene_guests:
            continue
        for node in originals[sid]["Nodes"]:
            if any(c is choice for c in node["Choices"]):
                index = next(i for i, c in enumerate(node["Choices"]) if c is choice)
                context = contexts.get((sid, node["Id"], "choice[%d]" % index))
                if context is not None and proof.implies(context, presence_guard(model, route, woman, block)):
                    break
                guard_choice(choice, context, woman, route, distant)
                break

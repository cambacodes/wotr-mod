"""E15c: what a rest-delivered (Remote) scene IS, so the book page can present it truthfully.

`Remote` only says *when* a scene arrives (after a rest). It says nothing about *what* the player is looking at, and the
first live screenshots showed the cost of treating every remote scene as mail: "Seelah finds you at the Nexus" was
framed as a letter, and the Commander's own Last Call vigil was captioned "- Commander" under Anevia and Irabeth.

Kinds (Scene.Kind), applied to every Remote, non-epilogue scene at integrate time; ids never change (save-safe):
  letter   correspondence read on the page: the sender's small framed portrait, a "Letter from <Sender>" line.
  visit    she is there in person (the note, if any, was only the invitation): the full illustration.
  sending  a live conversation at a distance by magic (Jerribeth's charm frame, Vellexia's echo shell): the full
           illustration, with an "A sending from <Sender>" line.
  memory   the Commander alone with a keepsake or a recollection: a muted illustration and an "A memory" line.
  event    a framework or Commander-only beat (Last Call's vigil, a rest page): no partner portrait at all.

Classification is rule-based on the scene's own prose (opening node and body), then corrected by the reviewed
OVERRIDES below. Writer/handoffs/SCENE-KINDS.md is the review table (tools: python -m storylines.scene_kinds).
"""
import re

KINDS = ("letter", "visit", "sending", "memory", "event", "invitation")
# "invitation" is never inferred: it is authored (household.invitation(), 08 §8) and kind_of() keeps an authored Kind.

# Owners that are presentation labels rather than a person the player sees.
GENERIC_OWNERS = ("Memory", "Rest", "Commander")

_LETTER = re.compile(
    r"\b(a letter|letter from|letters?\b|packet|envelope|a note|note (reaches|arrives|waits)|carrier|courier|"
    r"reply (arrives|comes)|answer (arrives|comes)|among your (letters|messages|correspondence|belongings)|"
    r"folded (page|sheet|note)|a page|the page|sheet|her hand(writing)?|written|writes|wrote|ink|seal|postscript)\b",
    re.I)
_SENDING = re.compile(
    r"\b(echo shell|the shell|the glass clears|through the glass|the frame|the charm|projects?|projected|projection|"
    r"her image|the connection|sending|sleep brings|the dream|next dream|a dream|a thought arrives that is not yours)\b", re.I)
_PRESENCE = re.compile(
    r"\b(finds you|comes to (you|find you)|you find (her|\w+) (at|in|near|beneath|beside)|meets you|is waiting|waits (at|for you|outside|beneath)|"
    r"when you arrive|you arrive|arrives (at|before)|opens the door|door stands open|walks? in|sits (down )?(beside|across|next)|"
    r"stands (in front|before|beside)|across the table|takes your hand|touches your|leans (in|close)|in front of you|"
    r"at your door|knocks|beside you)\b", re.I)
_TOUCH = re.compile(r"\b(takes your hand|touches your (hand|face|cheek|arm|mouth|lips)|kisses you|her hand (on|in) yours|leans (in|close) to you)\b", re.I)
_MEMORY = re.compile(r"\b(you remember|remembers?|recall|a memory|years ago|long ago|keepsake|among your belongings)\b", re.I)

# Reviewed corrections (id -> kind), from reading each scene the rules could not settle. See SCENE-KINDS.md.
OVERRIDES = {
    # Invitations that are the hook for an in-person evening.
    "kiana.date": "visit",
    "konomi.private_reunion": "visit",
    "konomi.carriers": "visit",
    "konomi.private_history": "visit",
    "konomi.another_evening": "visit",
    "konomi.private_kept_hours": "visit",
    "konomi.private_last_visit": "visit",
    "kiana.later_incident": "visit",
    "kiana.bakery_stairs": "visit",
    "minachiv.two_answers": "visit",
    # Pages the Commander writes, keeps or rereads alone.
    "konomi.return_letter": "memory",
    "anevia.the_blank_half": "memory",
    "tirabade.negotiated_letter": "memory",
    "kiana.another_page": "memory",
    # Magical correspondence that is read, not spoken.
    "jerribeth.fate_letter": "letter",
    "targona.the_unscheduled_door": "letter",
    # Jerribeth speaks through her charm frame; the tenant is a thought that is not yours; Vellexia's shell calls.
    "jerribeth.price": "sending",
    "jerribeth.counterfeit_after": "sending",
    "jerribeth.farewell_review": "sending",
    "jerribeth.another_evening": "sending",
    "jerribeth.trickster.dead.backdated": "sending",
    "jerribeth.trickster.dead.tenant": "sending",
    "vellexia.two_unremarkable_pleasures": "sending",
    # The Commander alone.
    "irabeth.an_unposted_line": "event",
    # Reviewed after the first rule pass (2026-09-28): she is there, speaking or working beside the Commander.
    "seelah.letter_work": "visit",
    "konomi.return_second_visit": "visit",
    "kiana.parting": "visit",
    "kiana.ink_after": "visit",
    "ember.after_applause": "visit",
    "minachiv.the_remaining_customers": "visit",
    "minachiv.the_cost_in_daylight": "visit",
    "anevia.trickster.gone.confession": "visit",
    "aranka.trickster.failure.second_verse": "visit",
    "vellexia.trickster.mirrored.speaks": "visit",
    "vellexia.trickster.sword.late_portrait": "visit",
    # She speaks through her charm, or meets the Commander in Nocticula's dream harbour.
    "jerribeth.purchaser_answer": "sending",
    "noct.counterseal": "sending",
    "noct.counterseal.acquired.new": "sending",
    "noct.counterseal.acquired.refused": "sending",
    "noct.counterseal.acquired.prior": "sending",
    # The Commander alone with a page, a map or a mended pouch.
    "konomi.retained_attempt": "memory",
    "konomi.private_absence": "memory",
    # About her, but she is not there and did not write it: no partner portrait.
    "konomi.fate_post": "event",
    "irabeth.trickster.killed.late_step": "event",
    "aranka.trickster.failure.mocking_verse_any": "event",
    "seelah.trickster.dead.pickpocket_effects": "event",
    "seelah.trickster.dismissed.late": "event",
}


def _plain(text):
    return re.sub(r"\{[^}]*\}", "", text or "")


def classify(scene):
    """The rule-based kind of one Remote scene, before OVERRIDES."""
    rel = scene.get("Relationship") or "tirabade"
    owner = scene.get("Owner", "")
    if rel == "lastcall" or owner in ("Commander", "Rest"):
        return "event"
    nodes = scene.get("Nodes") or []
    first = _plain(nodes[0].get("Text", "")) if nodes else ""
    body = " ".join(_plain(n.get("Text", "")) for n in nodes)
    opening = first[:260]
    if _SENDING.search(opening):
        return "sending"
    if _PRESENCE.search(opening):
        return "visit"
    if _LETTER.search(opening):
        # A note that asks the Commander to come is the invitation to a visit, not the scene itself.
        rest = body[len(first):]
        return "visit" if (_PRESENCE.search(rest) or _TOUCH.search(body)) else "letter"
    if _MEMORY.search(opening):
        return "memory"
    return "visit" if _PRESENCE.search(body) else ("sending" if _SENDING.search(body) else "visit")


def kind_of(scene):
    authored = scene.get("Kind")
    if authored in KINDS:
        return authored
    return OVERRIDES.get(scene["Id"]) or classify(scene)


def content_fix(scene, kind):
    """A letter whose prose puts her physically beside the Commander contradicts itself (writing pass, not UI)."""
    if kind != "letter":
        return None
    body = " ".join(_plain(n.get("Text", "")) for n in scene.get("Nodes") or [])
    m = _TOUCH.search(body)
    return m.group(0) if m else None


def _senders(scenes):
    """The person behind each relationship, for scenes whose Owner is a presentation label."""
    counts = {}
    for s in scenes:
        owner = s.get("Owner", "")
        if owner in GENERIC_OWNERS or owner.endswith("Epilogue") or owner == "Together":
            continue
        rel = s.get("Relationship") or "tirabade"
        counts.setdefault(rel, {}).setdefault(owner, 0)
        counts[rel][owner] += 1
    names = {rel: max(owners, key=owners.get) for rel, owners in counts.items()}
    names["tirabade"] = "Anevia and Irabeth"
    names["minagho_chivarro"] = "Minagho and Chivarro"
    return names


def remote_scenes(scenes):
    # Mirrors Rules.IsRemote (Remote, or the "Memory" presentation owner), epilogue pages excluded.
    return [s for s in scenes if (s.get("Remote") or s.get("Owner") == "Memory") and not s.get("Owner", "").endswith("Epilogue")]


def integrate(payload):
    scenes = payload["Scenes"]
    senders = _senders(scenes)
    for s in remote_scenes(scenes):
        kind = kind_of(s)
        if kind not in KINDS:
            raise ValueError("Unknown scene kind %s for %s" % (kind, s["Id"]))
        s["Kind"] = kind
        owner = s.get("Owner", "")
        if kind != "event":
            s["Sender"] = "Anevia and Irabeth" if owner == "Together" else (
                senders.get(s.get("Relationship") or "tirabade", owner) if owner in GENERIC_OWNERS else owner)


def review_table(scenes):
    """Markdown rows for Writer/handoffs/SCENE-KINDS.md."""
    rows = []
    for s in remote_scenes(scenes):
        kind = kind_of(s)
        fix = content_fix(s, kind)
        first = _plain((s.get("Nodes") or [{}])[0].get("Text", "")).replace("\n", " ").replace("|", "/")
        source = "override" if s["Id"] in OVERRIDES else "rule"
        rows.append((s.get("Relationship") or "tirabade", s["Id"], kind, source, first[:90], fix))
    return rows

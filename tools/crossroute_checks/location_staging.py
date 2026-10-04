"""L3: place -> existing Area/Chapter window (authored setting, not mere mention).

BlueprintArea GUIDs verified in /wrath/blueprints.zip:
DrezenCapital 2570015799edf594daf2f076f2f975d8: campaign Chapters 3/5;
Nexus 7847c3e3537104f4694167af0b9fcd0e: Chapter 4;
TheIvoryLabyrinth 3538511f16d45f44f8249ff710777e2d: Chapter 5;
ThresholdOutdoor 10c4b0e2af186ba46ab4d238d00a40a8 / ThresholdIndoor
22c6a99913fe5bb46b2e6011aaf93368: Chapter 6.
Campaign epilogues may stage future Drezen without a campaign chapter gate.
Generic 'camp', 'room', 'window' alone cannot identify an area: camp/room/window
staging with a named setting uses that setting; citadel is the established
Drezen citadel used throughout this export. No invented room flags.
Named crusade/war camp: WarCamp 7a25c101fe6f7aa46b192db13373d03b,
Chapter 2 (the early route hooks already use that chapter window).
IvorySanctum 982abcee3e7b25f459bef22ea22b3ab5, Chapter 3/5;
Alushinyrra Higher/Medium/Lower city (see table), Chapter 4.
WintersunOutdoor 0a5654e7dc18f074d9356009d55eb51b, Chapter 3/5.
"""
import re
from .common import finding, sentences, postwar

PLACES = {
    "Drezen": (r"Drezen|(?:Drezen['’]s\s+)?citadel", ("2570015799edf594daf2f076f2f975d8",), (3, 5)),
    "Nexus": (r"(?:the\s+)?Nexus", ("7847c3e3537104f4694167af0b9fcd0e",), (4,)),
    "Ivory Labyrinth": (r"(?:the\s+)?Ivory Labyrinth", ("3538511f16d45f44f8249ff710777e2d",), (5,)),
    "Threshold": (r"(?-i:Threshold)", ("10c4b0e2af186ba46ab4d238d00a40a8", "22c6a99913fe5bb46b2e6011aaf93368"), (6,)),
    "Wintersun": (r"Wintersun", ("0a5654e7dc18f074d9356009d55eb51b",), (3, 5)),
    "crusade camp": (r"(?:crusade|crusaders?[’']?)\s+camp|war camp", ("7a25c101fe6f7aa46b192db13373d03b",), (2,)),
    "Ivory Sanctum": (r"Ivory Sanctum", ("982abcee3e7b25f459bef22ea22b3ab5", "9e7095c1bbd7444e9c91808c8d0ae620", "cb3fb43244053f04e910689a6481128e"), (3, 5)),
    "Alushinyrra": (r"Alushinyrra", ("8217b05e37078414981d994151f0ffb1", "180cdb4b48d561f4cb4ef9a066727960", "4f849f5683145d0489db4077e0d7eccf"), (4,)),
}
HISTORY = re.compile(r"\b(?:remembers?|recalls?|remembered|recalled|once|used to|had been|had stood|must have gone|you tell her about|dream|vision|portrait|painting|map of|letter from|report from|when we|when you|before we|before you|since|has pencilled|send up a complaint)\b", re.I)
MENTAL = re.compile(r"\b(?:being read|being searched|mind['’]s eye|inside your mind|in your thoughts|in her thoughts|in your memory)\b", re.I)
# An authored, explicit journey is a location variant: the scene begins where
# its ordinary gates allow and then stages the destination. This is DLC-tier
# travel (Binding context 4), not permission for a bare off-location room.
TRAVEL = re.compile(r"\b(?:room folds shut around.{0,110}opens again somewhere|you step through.{0,70}(?:portal|rift).{0,90}(?:arrive|emerge)|you step into the wardrobe.{0,180}open it again onto the Council chamber|through the purple door.{0,180}out of your own wardrobe)\b", re.I | re.S)


def staged(text, name):
    """Present setting grammar; past anecdotes, plans and destinations are not staging."""
    place = PLACES[name][0]
    paragraphs = re.findall(r"\{n\}(.*?)\{/n\}", text, re.S) or [text]
    lines = [line for paragraph in paragraphs if not MENTAL.search(paragraph) for line in sentences(paragraph)]
    for line in lines:
        # eng7-l12: remote cutaways and a traveller's origin do not relocate
        # the Commander. Keep checking the rest of the block independently.
        if (re.search(r"\bSomewhere\b.{0,65}\b(?:Drezen|Alushinyrra)\b", line, re.I)
                or re.search(r"\bfrom the camps outside Drezen\b", line, re.I)
                or re.search(r"\bas close to a royal seal as anything in Drezen gets\b", line, re.I)
                or re.search(r"\b(?:a mirror stands|mirror stands)\b.{0,90}\bempty salon\b", line, re.I)
                or re.search(r"\bThe rest of that ear is on a shelf in Alushinyrra\b", line, re.I)
                or TRAVEL.search(line)):
            continue
        if not re.search(r"\b(?:" + place + r")\b", line, re.I) or HISTORY.search(line):
            continue
        if (re.search(r"\b(?:here in|here at|in|inside|at|outside|above|beneath|through|over|across|under|back in|back at)\s+(?:the\s+)?(?:" + place + r")\b", line, re.I)
                and re.search(r"\b(?:stands?|sits?|leans?|waits?|walks?|steps?|watches?|opens?|window|room|chamber|door|table|bed|walls?|battlements|courtyard|camp|tent|air|wind|rain|fire|night|find|meet)\b", line, re.I)):
            if not re.search(r"\b(?:will|would|could|might|shall|should|if|going to|to return|to go|to visit)\b", line, re.I):
                yield line
        elif re.search(r"\b(?:" + place + r")[’']?s?\s+(?:window|walls?|room|citadel|battlements|courtyard|streets|camp|air|wind)\b", line, re.I):
            yield line


def check(model, blocks, proof):
    out = []
    for b in blocks:
        if b.slot.startswith("choice") or b.slot in ("Entry", "ReturnText"):
            continue  # an offered trip does not assert the present scene's setting
        if b.node.get("Speaker") != "Narrator" and "{n}" not in b.text:
            continue
        if b.scene.get("Kind") in ("memory", "dream"):
            continue
        if any(TRAVEL.search(model.nodes[b.scene["Id"]][nid]["Text"]) for nid in b.ancestors):
            continue
        for name, (_, areas, chapters) in PLACES.items():
            # Quoted NPC speech may describe a destination while narration stages
            # another place. Only scan the actual narrator portions of NPC nodes.
            matches = list(staged(b.text, name))
            if not matches:
                continue
            # Postwar authored visits describe their future setting, not the
            # player's area in the epilogue book. Threshold recalls the finale.
            if postwar(b.scene):
                continue
            window = set(b.scene.get("Chapters") or range(b.scene["MinChapter"], b.scene["MaxChapter"]+1))
            if b.scene.get("Areas") and set(b.scene["Areas"]) <= set(areas) and window <= set(chapters):
                continue
            out.append(finding("L3", b, "Areas subset %s and Chapters subset %s, or an explicit location variant" % (list(areas), list(chapters)),
                               name, matches[0][:240]))
    return out

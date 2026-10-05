"""L5: asserted ending facts -> verified native evidence (GUIDs cited below).

Source: /wrath/blueprints.zip, World/Etudes/Common/WrathOfTheRighteous/
Chapter06_Extra/Ending_*.jbp; TrueEnding/TE_Ascend*.jbp; Mythic*/PlayerIs*.jbp.
Ending_WoundClosed 10cf0442f31a4796af8b28281f35e944 is NOT implied by
Ending_Trickster_AllPlanes f7343e290a8d4ed887af8f04d1b3446b or
Ending_Trickster_AllPlanesAndFW 5f63f6d43c9b465f822db70af7d69b92.
The other Trickster finales are db5375333382d044089475d256f19582
(Ending_Trickster) and 6ff418aeda24e6e48be844e6258e3c5a (Ending_TricksterFull).
Ascension: 07ad18ffb08145b69522f8eee0230857 TE_AscendAll;
08e47548e25945e286fe77b896884b32 TE_AscendAlone;
63279a971792474ba0439b9f75795a7a TE_AscendAreelu;
9fc5161813f1497f8eaad1563ac54211 TE_AscendCompanions.
Kenabres rebuilding is not an ending switch: DLC6_Start_KTC/Cue_0008
fc65929e0c9e4a9fa03309418c2d29bb asserts it before the ending (enGB key
61f3a312-a927-4614-8dba-2ba45bc7753b). A registered SeenCues reading is
sufficient evidence; DLC installed alone isn't. No fictional 'rebuilt' flag.

Expressions in this table resolve registered keys by native GUID, allowing
aliases without silently accepting an unbound invented fact key.
"""
import re
from .common import OR, AND, lit, finding, postwar, sentences

PATH_GUIDS = {
    "angel": "3a82aba4de71b89458ac82949ed957c4", "aeon": "3a040afde22f4b742a2f607354ab17e7",
    "azata": "d3b47e973d65c6c46af1cce815d1f6ce", "demon": "9a3739370f84b0b4196d0e4d326ea3a8",
    "devil": "a1db9daf676b36f4d99c6a788a0fe1af", "dragon": "9b193d30c89a20b409fd3dda9bd109bf",
    "legend": "c6165efcd5571c442ae38d7c0601f2df", "lich": "11fc5662e0ce8074ea145a022282b879",
    "swarm": "439e63fed37f52048887d98f99255e40", "trickster": "9f486a9c0c9abfc4a952bb22e88a7e96",
}
TRICKSTER_FINALES = ("db5375333382d044089475d256f19582", "6ff418aeda24e6e48be844e6258e3c5a",
                    "f7343e290a8d4ed887af8f04d1b3446b", "5f63f6d43c9b465f822db70af7d69b92")
FACTS = {
    "Worldwound closed": (r"\b(?:Worldwound|Wound|rift)\b.{0,50}\b(?:is closed|was closed|had closed|has closed|closed|sealed|healed|shut)\b|\b(?:closed|sealed|healed|shut)\s+(?:the\s+)?(?:Worldwound|Wound|rift)\b",
                          ("10cf0442f31a4796af8b28281f35e944",)),
    "Crossroads of Worlds": (r"\b(?:Crossroads of Worlds|Worldwound.{0,40}(?:became|is now|turned into).{0,20}crossroads)\b",
                            ("f7343e290a8d4ed887af8f04d1b3446b", "5f63f6d43c9b465f822db70af7d69b92")),
    "Commander ascended": (r"\b(?:you|Commander)\b.{0,45}\b(?:ascended|became a god|became a deity|divinity|godhood)\b|\b(?:your ascension|your godhood)\b",
                           ("07ad18ffb08145b69522f8eee0230857", "08e47548e25945e286fe77b896884b32", "63279a971792474ba0439b9f75795a7a", "9fc5161813f1497f8eaad1563ac54211")),
    "Kenabres rebuilt": (r"\bKenabres\b.{0,40}\b(?:rebuilt|restored)\b|\b(?:rebuilt|restored)\s+Kenabres\b",
                         ("fc65929e0c9e4a9fa03309418c2d29bb",)),
}
NONASSERTION = re.compile(r"\b(?:if|unless|whether|might|would|could|should|will|hope|hoped|wish|wished|dream|imagined|not|never)\b", re.I)


def asserted(pattern, text):
    for match in re.finditer(pattern, text, re.I):
        # eng7-l12: a hand closed around a stone / eyes closed beside a scar
        # are not statements that the planar Wound closed. A following 'or
        # failed to' explicitly leaves the finale unresolved.
        tail = match.group() + text[match.end():match.end()+25]
        if re.search(r"\bclosed\s+(?:her|his|their|your)\s+eyes\b|\bclosed\s+it\s+round\b", tail, re.I):
            continue
        if re.match(r"\s*,?\s*or\s+failed\s+to\b", text[match.end():], re.I):
            continue
        if re.search(r"\bold wound from Kenabres\b", match.group(), re.I):
            continue
        # Qualifiers apply to the assertion's own clause. 'She never regretted
        # it' after an asserted closure does not erase the closure claim.
        prefix = re.split(r"[,;:]", text[:match.start()])[-1][-65:]
        if not NONASSERTION.search(prefix + match.group()):
            return True
    return False


def native_evidence(model, guids):
    keys = [k for section in ("Etudes", "SeenCues", "SelectedAnswers", "CompletedEtudes")
            for k, value in (model.story.get(section) or {}).items()
            if (isinstance(value, str) and value in guids)
            # An OR-binding containing unrelated cues does not prove the fact.
            or (isinstance(value, list) and value and set(value) <= set(guids))]
    return OR(*(lit(k) for k in keys))


def check(model, blocks, proof):
    out = []
    # Binding aliases are immutable within this inventory. Resolve each native
    # fact once, instead of rescanning every reader for every sentence.
    evidence = {}
    def target_for(guids):
        if guids not in evidence:
            evidence[guids] = native_evidence(model, guids)
        return evidence[guids]
    for b in blocks:
        if not postwar(b.scene) or b.slot in ("Entry", "ReturnText"):
            continue
        for line in sentences(b.text):
            clean = re.sub(r"\{[^}]*\}", "", line)
            for name, (pattern, guids) in FACTS.items():
                if asserted(pattern, clean):
                    target = target_for(guids)
                    if not proof.implies(b.context, target):
                        out.append(finding("L5", b, "native fact %s established by %s" % (name, ", ".join(guids)), name, line[:240], required=target))
            for path, guid in PATH_GUIDS.items():
                label = r"(?:Gold Dragon|golden dragon|dragon)" if path == "dragon" else path
                pattern = r"\b(?:you (?:are|remain|remained|became)|Commander (?:is|remains|remained|became))\s+(?:an?\s+|the\s+)?" + label + r"\b"
                if asserted(pattern, clean):
                    target = target_for((guid,))
                    if path == "trickster":
                        target = OR(target, lit("trickster.now"), target_for(TRICKSTER_FINALES))
                    if not proof.implies(b.context, target):
                        native_name = "Locust" if path == "swarm" else path.title()
                        out.append(finding("L5", b, "current mythic %s: PlayerIs%s %s" % (path, native_name, guid), path, line[:240], required=target))
    return out

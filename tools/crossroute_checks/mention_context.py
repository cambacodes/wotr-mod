"""L1's conservative distinction between a living participant and a reference.

An unclassified mention requires current route availability. Only a reference
whose wording establishes history, mourning, reputation, a relic or a title is
exempt. Past tense alone is not history: epilogues narrate future life in past
tense. Exemptions apply per occurrence, never to a whole mixed paragraph.
"""
import re

LIVE_ACTION = r"(?:stands?|waits?|sits?|leans?|steps?|enters?|joins?|arrives?|laughs?|smiles?|speaks?|says?|asks?|answers?|nods?|walks?|comes?|holds?|takes?|touches?|watches?|turns?|moves?|puts?|drinks?|sings?|offers?|grins?|lifts?|reaches?|pushes?|pulls?|folds?|sets?|kisses?|embraces?)\b"
LIVE_STATE = r"(?:is\s+(?:(?:now|still)\s+)?(?:here|alive|present|standing|sitting|waiting)|has returned|will\s+(?:meet|visit|come|join|arrive|return|wait))\b"


def live_continuation(after):
    """eng7-l14: a reference cannot swallow a claim about the same actor.

    Stay inside this sentence. Relative clauses and coordinated predicates
    can attach today's action to a memory, comparison, relic or reputation.
    Counterfactual past reactions ("would have laughed") remain references.
    """
    clause = re.split(r"[.!?]\s+|\n|\{/n\}", after)[0]
    action = LIVE_ACTION
    possessed = re.match(r"['’]s\b", clause)
    state = LIVE_STATE
    if re.match(r"\s*,?\s*who\s+(?:(?:now|still)\s+)?(?:" + action + "|" + state + ")", clause, re.I):
        return True
    if not possessed and re.search(r"\b(?:and|but)\s+(?:she\s+)?(?:(?:now|still)\s+)?" + action, clause, re.I):
        return True
    subject = r"she\s+" if possessed else r"(?:she\s+)?"
    if re.search(r"\b(?:and|but)\s+" + subject + r"(?:will|shall)\s+(?:meet|visit|come|join|arrive|return|wait)\b", clause, re.I):
        return True
    if re.search(r"\bshe\s+" + action + r"[^.!?;]{0,60}\b(?:here|now|tonight|tomorrow)\b", clause, re.I):
        return True
    if re.search(r";\s*she\s+(?:(?:now|still)\s+)?" + action, clause, re.I):
        return True
    if re.search(r"\bshe\s+" + state, clause, re.I):
        return True
    return False


def reference_reason(text, match, postwar=False):
    before = text[max(0, match.start() - 100):match.start()]
    after = text[match.end():match.end() + 140]
    clause = re.split(r"[.!?]\s+|\n", after)[0]
    narrated = text.rfind("{n}", 0, match.start()) > text.rfind("{/n}", 0, match.start())
    # The paid Shyka reading repeats a morning from the Commander's past.
    # Only the quoted recollection, before the narrated loss of that memory,
    # is historical. A subsequent live cameo cannot inherit this exemption.
    if (text.startswith("{n}Shyka reaches out, and does not touch you, and speaks in your voice: the voice you had that day,")
            and "{n}You hear" in text and match.start() < text.index("{n}You hear")
            and text.rfind("{n}", 0, match.start()) < text.rfind("{/n}", 0, match.start())):
        return "paid recollection of an earlier morning"
    if live_continuation(after):
        return None
    if (re.search(r"\bDuring the crusade,\s*$", before, re.I)
            and re.match(r"\s+(?:killed|executed|tortured|imprisoned|chained|sacrificed)\b", after, re.I)):
        return "explicit campaign harm recollection"
    # eng7-l14: the paid receipt records the prologue morning, not a new
    # visit by its dead dragon. Keep the memory price independent of return.
    if (re.search(r"\bwith a morning in Kenabres:\s*(?:the\s+)?$", before, re.I)
            and re.match(r"['’]s\s+promise in the festival square\b", after, re.I)):
        return "paid recollection of the prologue promise"
    if re.search(r"\b(?:but|and)\s+(?:she\s+)?(?:is here|is alive|has returned|will (?:join|come|visit)|waits here)\b", clause, re.I):
        return None
    if re.search(r"\bshe(?:['’]ll|\s+will)\s+(?:meet|visit|come|join|arrive|return)\b", after, re.I):
        return None
    if re.search(r"\b(?:was|is) a\s+$", before, re.I) and re.match(r"\s+on my menu\. A boy who wore her face\b", after, re.I):
        return "explicitly identified impersonator"
    if re.match(r"\s+who knelt over you in the festival square,?\s+and what she promised you\b", after, re.I):
        return "canonical prologue recollection"
    if re.search(r"\b(?:were|was|worked) under\s+$", before, re.I):
        return "former employer"
    if re.match(r"\s+has already had a word with me\b", after, re.I):
        return "completed earlier conversation"
    if re.search(r"\battribute(?:d)? to\s+$", before, re.I):
        return "attribution of a past cause"
    if re.search(r"\b(?:tell me about|speak about|what happened to)\s+$", before, re.I) and re.fullmatch(r"\s*[.!?]?[\"”'’]?\s*", after):
        return "request for history or reputation"
    if re.search(r"\bcalled\s+\*?$", before, re.I) and re.match(r"\*?\s+by\b", after, re.I):
        return "reported mistaken identity"
    if (re.search(r"\bkeep their distance from\s+\*?$", before, re.I)
            and re.search(r"I have been called\s+" + re.escape(match.group()), text, re.I)):
        return "reported mistaken identity"
    if re.search(r"\bby\s+$", before, re.I) and re.match(r"['’]s word\b", after, re.I) and re.search(r"\b(?:sent|arrived)\b", text, re.I):
        return "recalled consignment order"
    if re.match(r"\s+was the (?:cleverest|strongest|kindest)\b", after, re.I):
        return "past reputation"
    if not postwar and re.match(r"\s+came to visit,? the first year\b", after, re.I):
        return "dated earlier visit"
    if re.search(r"\bcorpse\b", before, re.I) and re.search(r"['‘\"]One\s+$", before, re.I) and re.match(r",\s+forever\.?['’\"]", after, re.I):
        return "recalled corpse contract"
    if re.search(r"\b(?:had loved|once loved|loved)\s+$", before, re.I):
        return "past love"
    if re.search(r"\bhad come back because\s+$", before, re.I) and re.match(r"\s+had fetched\b", after, re.I):
        return "earlier earned return"
    if re.search(r"\b(?:didn['’]t|did not) (?:come|save|rescue|bring)\b[^.!?]{0,65}\bfor\s+$", before, re.I):
        return "recalled failed rescue"
    if re.search(r"\b(?:don['’]t|do not) tell me about\s+$", before, re.I):
        return "refused discussion of a past fate"
    if re.search(r"\b(?:death at|killed by|slain by|murdered by)\s+$", before, re.I):
        return "historical perpetrator"
    if (re.search(r"\b(?:tell me where|ask where|wonder where|know where)\s+$", before, re.I)
            and re.match(r"\s+is\s*[.!?]", after, re.I)) or re.search(r"\bwhat happened to\s+$", before, re.I):
        return "question about unknown whereabouts or fate"
    if re.search(r"\bwhether she(?:['’]s| is) here\b[^.!?]{0,60}\bor not\b", after, re.I):
        return "explicitly holds in her absence"
    # A title names an institution/other person, not the goddess herself.
    if re.search(r"(?:church|paladin|priest|priestess|cleric|acolyte|temple|knight|servant|hand|herald|faith|order|sword|blade|blessing|shrine|image|statue|mark|sign)\s+of\s+(?:the\s+)?$", before, re.I):
        return "institution or title"
    if re.match(r"['’]s\s+(?:church|faith|temple|paladins|priests|knights|company|regiment|war|crusade|symbol|holy symbol|sword|court|courts)\b", after, re.I):
        return "institution or relic"
    if match.group().lower() == "iomedaean":
        return "religious adjective"
    if not postwar and not narrated and re.match(r"['’]s guests (?:spent|paid|died|were eaten)\b", after, re.I):
        return "reported past guests"
    if re.match(r"\s+(?:help|forgive|save|bless)\s+me\b", after, re.I):
        return "prayer"
    if match.group().lower() in ("iomedae", "inheritor"):
        if (re.search(r"\b(?:thank(?:s|ed)?|swear by|pray to|prayer to|before|for|by)\s+(?:the\s+)?$", before, re.I)
                or re.match(r"\s*[,!]\s*(?:yes|help|forgive|save|bless)\b", after, re.I)
                or re.match(r"\s+(?:will cope|gave me two legs)\b", after, re.I)):
            return "religious invocation"
        if (re.search(r"\b(?:serve|serves|served|serving|thank|thanked|pray|praying|prayers|chaplains|priests|churches|image|sign|swear|swore)\b[^.!?]{0,50}$", before, re.I)
                or re.match(r"['’]s\s+(?:court|door|army|little lamps)\b", after, re.I)
                or re.match(r"\s+(?:can take it up|has a plan|asks us to forgive|chooses her paladins|knows it|hears about it|saw that|is going to have words)\b", after, re.I)):
            return "religious belief or institution"
    if re.search(r"\b(?:remember(?:s|ed)?|recall(?:s|ed)?|memory of|memories of|mourn(?:s|ed)?|grieve(?:s|d)?|grave of|death of|killed|executed|buried|lost|losing)\s+(?:(?:the|a|her|my|your|with|how|when|of|Lady|Queen)\s+)*$", before, re.I):
        return "explicit memory or mourning"
    if (not postwar and not narrated
            and "the first time I ever saw you" in text[:match.start()]
            and re.search(r"\bDown in the caves\b", before)
            and re.match(r"\s+with her hand on her sword because she thought\b", after)):
        return "explicit recollection of the first cave encounter"
    if re.match(r"\s+(?:is dead|was dead|stayed dead|died|has died|had died|had been killed|was killed|was executed|is gone)\b", after, re.I):
        return "death or departure"
    if re.match(r"['’]s(?:[.!?]|[\"”])", after):
        return "remembered possession"
    if re.match(r"['’]s\s+(?:grave|death|absence|departure|disappearance|corpse|bones|memory|spare\s+surcoat|old\s+letter|old\s+letters|name|reputation|ledger|barrier|racks|smiths|work|house|palace|lair|refuge|laboratory|notes|secrets|quills|handwriting)\b", after, re.I):
        return "mourning, history or reputation"
    if (re.match(r"\s+(?:is (?:brave|loyal|cruel|notorious|merciless)|has a reputation)\b", after, re.I)
            and not re.search(r"\b(?:tonight|tomorrow|will|meet|visit|return)\b", clause, re.I)):
        return "reputation"
    if re.search(r"\b(?:if|as if|like|unlike|rather than|not|instead of|isn['’]t|try bein['’]?|being)\s+(?:(?:Lady|Queen)\s+)?$", before, re.I):
        # Conditional scheduling and comparisons with a living actor still
        # depend on her availability; a purely hypothetical likeness does not.
        if re.match(r"\s+(?:" + LIVE_ACTION + "|" + LIVE_STATE + r"|hasn['’]t got\b|has not got\b)", after, re.I):
            return None
        return "comparison or hypothetical"
    if re.search(r"\b(?:said|told|heard|seen)\b[^.!?]{0,60}\bsince\s+$", before, re.I):
        return "remembered earlier comparison"
    # Explicit campaign recollections remain historical even in an ending.
    sentence = re.split(r"[.!?]\s+|\n", before)[-1] + match.group() + clause
    if (re.search(r"\b(?:story|anecdote|recollection)\b", before, re.I)
            and re.match(r"\s+(?:swore|said|told|gave|kept|tried|had|was|were)\b", after, re.I)):
        return "retold past event"
    if re.search(r"\b(?:imitated|impersonated|lost|buried|killed|executed)\s+$", before, re.I):
        return "reported earlier action"
    if not postwar and not narrated and re.search(r"\b(?:distracted|wore|rescued|chose|out-argued)\s+$", before, re.I):
        return "reported earlier shared action"
    if re.match(r"\s+(?:would have (?:a fit|a stroke|laughed|smiled|known|approved|disapproved)|never could|could never)\b", after, re.I):
        return "hypothetical or remembered character"
    if (re.match(r"\s+(?:would (?:tell|say|notice|eat|be proud|have drawn|try)|never told me)\b", after, re.I)
            and not re.search(r"\b(?:tonight|tomorrow|will|meet|visit|return)\b", sentence, re.I)):
        return "remembered habits or hypothetical reaction"
    if re.search(r"\bthe way\s+$", before, re.I):
        return "comparison"
    if not re.search(r"\b(?:will|tonight|tomorrow|still|every morning|every night)\b", sentence, re.I):
        if re.search(r"\b(?:back in|back at|used to|all those years|years ago|before (?:the|her|his|my))\b", sentence, re.I):
            return "explicit earlier event"
        if (not postwar and re.search(r"\b(?:once|an hour ago)\b", sentence, re.I)
                or re.search(r"\bin (?:Kenabres|the Fane)\b", sentence, re.I)) and re.match(
                r"\s+(?:(?:once|had|has)\s+)?(?:gave|kept|said|told|rescued|was|wore|found|wanted|chose|tried)\b", after, re.I):
            return "reported earlier campaign event"
    if not postwar and not narrated and re.match(r"\s+(?:killed|executed|tortured|imprisoned|chained|sacrificed)\b", after, re.I):
        return "past harm"
    if (re.match(r"(?:['’]s| has| had)\s+(?:told|warned|taught|said)\b", after, re.I)
            and not re.search(r"\b(?:will|tonight|tomorrow|now|still|meet|visit|come|arrive)\b|['’]ll\b", sentence, re.I)):
        return "reported earlier conversation"
    if re.search(r"\bI (?:asked|told|met|warned|spoke with)\s+$", before, re.I):
        return "reported earlier conversation"
    if (not postwar and not narrated
            and re.search(r"\bI (?:held|fought|stood|waited|carried|brought|made|kept|saved)\b[^.!?]{0,70}\b(?:for|with|beside)\s+$", before, re.I)):
        return "reported earlier shared action"
    if not postwar and not narrated and re.match(r"\s+(?:gave|kept|wanted|loved|left|read|served|tortured|imprisoned|held|broke|made|offered|told|taught|showed|found|said|asked|had|warned|tried|healed)\b", after, re.I):
        # Reported past action does not promise another meeting. A current or
        # future assertion in the same sentence is still independently checked.
        if not re.search(r"\b(?:will|tonight|tomorrow|now|still|meet|visit|come|arrive)\b|['’]ll\b", sentence, re.I):
            return "reported past event"
    return None


def live_mentions(text, pattern, postwar=False):
    return [m for m in pattern.finditer(text) if not reference_reason(text, m, postwar)]
